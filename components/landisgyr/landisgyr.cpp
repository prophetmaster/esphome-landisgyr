#include "landisgyr.h"
#include "esphome/core/log.h"

namespace esphome {
namespace landisgyr {

static const char *TAG = "landisgyr";

void LandisGyrComponent::setup() {
  // Initialization code if needed
}

void LandisGyrComponent::loop() {
  // While ir serial
  while (available()) {
    // Read serial buffer
    response_ = read();
    
    if (unit_flag_) {
      // Reset flag for next round
      unit_flag_ = false;
      ESP_LOGD("HEX", "unitFlag == true");
      // Reset serial buffer
      serial_buffer_.clear();
    }

    if (response_ == POINT) {
      unit_flag_ = false;
      meter_id_buffer_ = serial_buffer_;
    }

    if (response_ == SLASH) {
      unit_flag_ = true;
    }

    if (ack_flag_) {
      // Reset flag for next round
      ack_flag_ = false;
      ESP_LOGD("HEX", "response == STX");
      // Reset serial buffer
      serial_buffer_.clear();
    }

    // Received <STX>
    if (response_ == STX) {
      ack_flag_ = true;
    }
    
    if (etx_flag_) {
      // Reset flags for next round
      ack_flag_ = false;
      etx_flag_ = false;

      // Store received checksum
      received_checksum_ = response_;
      
      // Checksum calculation
      str_len_crc_ = serial_buffer_.length();
      checksum_ = crc_calculation((uint8_t *)serial_buffer_.data(), str_len_crc_);

      if (checksum_) {
        // Decoding values
        decode_ir_serial(const_cast<char*>(serial_buffer_.c_str()));
        a_ = true;
        ESP_LOGD("A", "a=1");
      } else {
        ESP_LOGD("ERR", "BAD CHECKSUM");
      }
    }

    // Received <ETX>
    if (response_ == ETX) {
      etx_flag_ = true;
    }

    // Add response to serial buffer
    serial_buffer_ += response_;

    // Debug
    ESP_LOGD("HEX", " 0x%02X", response_);
  }
  
  if (a_) {
    a_ = false;
    ESP_LOGD("A", "OK");
    uint8_t test_array[5] = {0x2F, 0x3F, 0x21, 0x8D, 0x0A};
    uint8_t test_array_2[6] = {0x06, 0x30, 0x30, 0x30, 0x8D, 0x0A};
    
    write_array(test_array, sizeof(test_array));
    delayMicroseconds(3000);
    write_array(test_array_2, sizeof(test_array_2));
  }
}

bool LandisGyrComponent::crc_calculation(uint8_t *data, size_t len) {
  uint8_t crc = 0;
  
  for (size_t i = 0; i < len; i++) {
    // ESP_LOGD(TAG, "0x%02X", data[i]);
    crc ^= data[i];
  }

  ESP_LOGD(TAG, "Received CRC 0x%02X calculated CRC 0x%02X", received_checksum_, crc);

  if (received_checksum_ == crc) {
    ESP_LOGD(TAG, "CHECKSUM OK");
    return true;
  }
  
  ESP_LOGD(TAG, "CHECKSUM ERROR");
  return false;
}

void LandisGyrComponent::decode_ir_serial(char *pointer) {
  while (*pointer) {
    if (strcmp(pointer, "!\r\n") == 0) break; // Fin du message

    // Trouver les séparateurs
    char *parentheseOuvrante = strchr(pointer, '(');
    char *parentheseFermante = strchr(pointer, ')');
    char *etoile = strchr(pointer, '*');
    char *finDeLigne = strchr(pointer, '\n');

    if ((parentheseOuvrante == nullptr) ||
        (parentheseFermante == nullptr) ||
        (finDeLigne == nullptr) ||
        (parentheseOuvrante > parentheseFermante)) {
      break; // Format invalide
    }

    // Extraire l'étiquette
    size_t nbCaracteres = parentheseOuvrante - pointer;
    if (nbCaracteres > MAX_DATA) {
      break; // Donnée trop longue
    }
    strncpy(etiquette_, pointer, nbCaracteres);
    etiquette_[nbCaracteres] = '\0';

    // Passer à la valeur
    pointer = parentheseOuvrante + 1;

    // Extraire la valeur et l'unité (si elle existe)
    if ((etoile == nullptr) || (etoile > finDeLigne)) {
      // Pas d'unité
      nbCaracteres = parentheseFermante - pointer;
      if (nbCaracteres > MAX_DATA) {
        break; // Donnée trop longue
      }
      strncpy(valeur_, pointer, nbCaracteres);
      valeur_[nbCaracteres] = '\0';
      unite_[0] = '\0'; // Pas d'unité
    } else {
      // Avec unité
      nbCaracteres = etoile - pointer;
      if (nbCaracteres > MAX_DATA) {
        break; // Donnée trop longue
      }
      strncpy(valeur_, pointer, nbCaracteres);
      valeur_[nbCaracteres] = '\0';

      pointer = etoile + 1;
      nbCaracteres = parentheseFermante - pointer;
      if (nbCaracteres > MAX_DATA) {
        break; // Donnée trop longue
      }
      strncpy(unite_, pointer, nbCaracteres);
      unite_[nbCaracteres] = '\0';
    }

    // Passer au champ suivant
    pointer = finDeLigne + 1;

    // Publier les valeurs en fonction de l'étiquette
    if (strcmp(etiquette_, "F.F") == 0 && error_code_ != nullptr) {
      error_code_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "0.0") == 0 && customer_id_ != nullptr) {
      customer_id_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "0.2.0") == 0 && firmware_version_ != nullptr) {
      firmware_version_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "C.1.0") == 0 && meter_id_ != nullptr) {
      meter_id_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "C.1.1") == 0 && manufacturing_id_ != nullptr) {
      manufacturing_id_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "C.5.0") == 0 && status_flag_ != nullptr) {
      status_flag_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "C.7.0") == 0 && event_power_down_counter_ != nullptr) {
      event_power_down_counter_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "82.8.1") == 0 && terminal_cover_removal_counter_ != nullptr) {
      terminal_cover_removal_counter_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "82.8.2") == 0 && dc_field_count_ != nullptr) {
      dc_field_count_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "1.8.0") == 0 && positive_active_energy_total_ != nullptr) {
      positive_active_energy_total_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "1.8.1") == 0 && positive_active_energy_t1_ != nullptr) {
      positive_active_energy_t1_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "1.8.2") == 0 && positive_active_energy_t2_ != nullptr) {
      positive_active_energy_t2_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "2.8.0") == 0 && negative_active_energy_total_ != nullptr) {
      negative_active_energy_total_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "2.8.1") == 0 && negative_active_energy_t1_ != nullptr) {
      negative_active_energy_t1_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "2.8.2") == 0 && negative_active_energy_t2_ != nullptr) {
      negative_active_energy_t2_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "5.8.0") == 0 && imported_inductive_reactive_energy_total_ != nullptr) {
      imported_inductive_reactive_energy_total_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "5.8.1") == 0 && imported_inductive_reactive_energy_t1_ != nullptr) {
      imported_inductive_reactive_energy_t1_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "5.8.2") == 0 && imported_inductive_reactive_energy_t2_ != nullptr) {
      imported_inductive_reactive_energy_t2_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "6.8.0") == 0 && imported_capacitive_reactive_energy_total_ != nullptr) {
      imported_capacitive_reactive_energy_total_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "6.8.1") == 0 && imported_capacitive_reactive_energy_t1_ != nullptr) {
      imported_capacitive_reactive_energy_t1_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "6.8.2") == 0 && imported_capacitive_reactive_energy_t2_ != nullptr) {
      imported_capacitive_reactive_energy_t2_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "7.8.0") == 0 && exported_inductive_reactive_energy_total_ != nullptr) {
      exported_inductive_reactive_energy_total_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "7.8.1") == 0 && exported_inductive_reactive_energy_t1_ != nullptr) {
      exported_inductive_reactive_energy_t1_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "7.8.2") == 0 && exported_inductive_reactive_energy_t2_ != nullptr) {
      exported_inductive_reactive_energy_t2_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "8.8.0") == 0 && exported_capacitive_reactive_energy_total_ != nullptr) {
      exported_capacitive_reactive_energy_total_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "8.8.1") == 0 && exported_capacitive_reactive_energy_t1_ != nullptr) {
      exported_capacitive_reactive_energy_t1_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "8.8.2") == 0 && exported_capacitive_reactive_energy_t2_ != nullptr) {
      exported_capacitive_reactive_energy_t2_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "32.7") == 0 && instantaneous_voltage_p1_ != nullptr) {
      instantaneous_voltage_p1_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "52.7") == 0 && instantaneous_voltage_p2_ != nullptr) {
      instantaneous_voltage_p2_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "72.7") == 0 && instantaneous_voltage_p3_ != nullptr) {
      instantaneous_voltage_p3_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "31.7") == 0 && instantaneous_current_p1_ != nullptr) {
      instantaneous_current_p1_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "51.7") == 0 && instantaneous_current_p2_ != nullptr) {
      instantaneous_current_p2_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "71.7") == 0 && instantaneous_current_p3_ != nullptr) {
      instantaneous_current_p3_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "13.7") == 0 && instantaneous_power_factor_ != nullptr) {
      instantaneous_power_factor_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "33.7") == 0 && instantaneous_power_factor_p1_ != nullptr) {
      instantaneous_power_factor_p1_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "53.7") == 0 && instantaneous_power_factor_p2_ != nullptr) {
      instantaneous_power_factor_p2_->publish_state(atof(valeur_));
    } else if (strcmp(etiquette_, "73.7") == 0 && instantaneous_power_factor_p3_ != nullptr) {
      instantaneous_power_factor_p3_->publish_state(atof(valeur_));
    }
  }
}

}  // namespace landisgyr
}  // namespace esphome