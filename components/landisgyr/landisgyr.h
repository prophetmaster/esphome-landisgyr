#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"
#include <vector>
#include <cstring>
#include <string>

namespace esphome {
namespace landisgyr {

class LandisGyrComponent : public Component, public uart::UARTDevice {
 public:
  void setup() override;
  void loop() override;

  void set_error_code_sensor(sensor::Sensor *sensor) { error_code_ = sensor; }
  void set_customer_id_sensor(sensor::Sensor *sensor) { customer_id_ = sensor; }
  void set_firmware_version_sensor(sensor::Sensor *sensor) { firmware_version_ = sensor; }
  void set_meter_id_sensor(sensor::Sensor *sensor) { meter_id_ = sensor; }
  void set_manufacturing_id_sensor(sensor::Sensor *sensor) { manufacturing_id_ = sensor; }
  void set_status_flag_sensor(sensor::Sensor *sensor) { status_flag_ = sensor; }
  void set_event_power_down_counter_sensor(sensor::Sensor *sensor) { event_power_down_counter_ = sensor; }
  void set_terminal_cover_removal_counter_sensor(sensor::Sensor *sensor) { terminal_cover_removal_counter_ = sensor; }
  void set_dc_field_count_sensor(sensor::Sensor *sensor) { dc_field_count_ = sensor; }
  void set_positive_active_energy_total_sensor(sensor::Sensor *sensor) { positive_active_energy_total_ = sensor; }
  void set_positive_active_energy_t1_sensor(sensor::Sensor *sensor) { positive_active_energy_t1_ = sensor; }
  void set_positive_active_energy_t2_sensor(sensor::Sensor *sensor) { positive_active_energy_t2_ = sensor; }
  void set_negative_active_energy_total_sensor(sensor::Sensor *sensor) { negative_active_energy_total_ = sensor; }
  void set_negative_active_energy_t1_sensor(sensor::Sensor *sensor) { negative_active_energy_t1_ = sensor; }
  void set_negative_active_energy_t2_sensor(sensor::Sensor *sensor) { negative_active_energy_t2_ = sensor; }
  void set_imported_inductive_reactive_energy_total_sensor(sensor::Sensor *sensor) { imported_inductive_reactive_energy_total_ = sensor; }
  void set_imported_inductive_reactive_energy_t1_sensor(sensor::Sensor *sensor) { imported_inductive_reactive_energy_t1_ = sensor; }
  void set_imported_inductive_reactive_energy_t2_sensor(sensor::Sensor *sensor) { imported_inductive_reactive_energy_t2_ = sensor; }
  void set_imported_capacitive_reactive_energy_total_sensor(sensor::Sensor *sensor) { imported_capacitive_reactive_energy_total_ = sensor; }
  void set_imported_capacitive_reactive_energy_t1_sensor(sensor::Sensor *sensor) { imported_capacitive_reactive_energy_t1_ = sensor; }
  void set_imported_capacitive_reactive_energy_t2_sensor(sensor::Sensor *sensor) { imported_capacitive_reactive_energy_t2_ = sensor; }
  void set_exported_inductive_reactive_energy_total_sensor(sensor::Sensor *sensor) { exported_inductive_reactive_energy_total_ = sensor; }
  void set_exported_inductive_reactive_energy_t1_sensor(sensor::Sensor *sensor) { exported_inductive_reactive_energy_t1_ = sensor; }
  void set_exported_inductive_reactive_energy_t2_sensor(sensor::Sensor *sensor) { exported_inductive_reactive_energy_t2_ = sensor; }
  void set_exported_capacitive_reactive_energy_total_sensor(sensor::Sensor *sensor) { exported_capacitive_reactive_energy_total_ = sensor; }
  void set_exported_capacitive_reactive_energy_t1_sensor(sensor::Sensor *sensor) { exported_capacitive_reactive_energy_t1_ = sensor; }
  void set_exported_capacitive_reactive_energy_t2_sensor(sensor::Sensor *sensor) { exported_capacitive_reactive_energy_t2_ = sensor; }
  void set_instantaneous_voltage_p1_sensor(sensor::Sensor *sensor) { instantaneous_voltage_p1_ = sensor; }
  void set_instantaneous_voltage_p2_sensor(sensor::Sensor *sensor) { instantaneous_voltage_p2_ = sensor; }
  void set_instantaneous_voltage_p3_sensor(sensor::Sensor *sensor) { instantaneous_voltage_p3_ = sensor; }
  void set_instantaneous_current_p1_sensor(sensor::Sensor *sensor) { instantaneous_current_p1_ = sensor; }
  void set_instantaneous_current_p2_sensor(sensor::Sensor *sensor) { instantaneous_current_p2_ = sensor; }
  void set_instantaneous_current_p3_sensor(sensor::Sensor *sensor) { instantaneous_current_p3_ = sensor; }
  void set_instantaneous_power_factor_sensor(sensor::Sensor *sensor) { instantaneous_power_factor_ = sensor; }
  void set_instantaneous_power_factor_p1_sensor(sensor::Sensor *sensor) { instantaneous_power_factor_p1_ = sensor; }
  void set_instantaneous_power_factor_p2_sensor(sensor::Sensor *sensor) { instantaneous_power_factor_p2_ = sensor; }
  void set_instantaneous_power_factor_p3_sensor(sensor::Sensor *sensor) { instantaneous_power_factor_p3_ = sensor; }

 protected:
  static constexpr uint8_t MAX_DATA = 30;
  char etiquette_[MAX_DATA];  // Keep as char arrays for strncpy
  char valeur_[MAX_DATA];     // Keep as char arrays for strncpy
  char unite_[MAX_DATA];      // Keep as char arrays for strncpy
  char message_[300];         // Keep as char array
  
  enum : uint8_t { ANALYSE_OK, ERREUR_FORMAT, ERREUR_DONNEE_TROP_LONGUE } erreur_;

  size_t nb_caracteres_;
  int str_len_decode_ = 0;

  // Define flags
  bool unit_flag_{false};
  bool firmware_version_flag_{false};
  bool ack_flag_{false};
  bool etx_flag_{false};
  bool checksum_{false};
  // bool a_{false};

  // Constants
  static const char NUL = 0;    // null
  static const char SOH = 1;    // start of heading
  static const char STX = 2;    // start of text
  static const char ETX = 3;    // end of text
  static const char EOT = 4;    // end of transmission
  static const char ENQ = 5;    // enquiry
  static const char ACK = 6;    // acknowledge
  static const char BEL = 7;    // bell
  static const char BS = 8;     // backspace
  static const char TAB = 9;    // horizontal tab
  static const char LF = 10;    // NL line feed
  static const char VT = 11;    // vertical tab
  static const char FF = 12;    // NP form feed
  static const char CR = 13;    // carriage return
  static const char SO = 14;    // shift out
  static const char SI = 15;    // shift in
  static const char DLE = 16;   // data link escape
  static const char DC1 = 17;   // device control 1
  static const char DC2 = 18;   // device control 2
  static const char DC3 = 19;   // device control 3
  static const char DC4 = 20;   // device control 4
  static const char NAK = 21;   // negative acknowledge
  static const char SYN = 22;   // synchronius idle
  static const char ETB = 23;   // end of trans. block
  static const char CAN = 24;   // cancel
  static const char EM = 25;    // end of medium
  static const char SUB = 26;   // substitute
  static const char ESC = 27;   // escape
  static const char FS = 28;    // file separator
  static const char GS = 29;    // group separator
  static const char RS = 30;    // record separator
  static const char US = 31;    // unit separator
  static const char POINT = 46; // . point
  static const char SLASH = 47; // / slash
  static const char HELP = 63;  // ? help

  // Buffers and state
  std::string serial_buffer_;
  std::string meter_id_buffer_;
  char response_{0};
  char received_checksum_{0};
  int str_len_crc_{0};

  bool crc_calculation(uint8_t *data, size_t len);
  void decode_ir_serial(char *pointer);

  sensor::Sensor *error_code_{nullptr};
  sensor::Sensor *customer_id_{nullptr};
  sensor::Sensor *firmware_version_{nullptr};
  sensor::Sensor *meter_id_{nullptr};
  sensor::Sensor *manufacturing_id_{nullptr};
  sensor::Sensor *status_flag_{nullptr};
  sensor::Sensor *event_power_down_counter_{nullptr};
  sensor::Sensor *terminal_cover_removal_counter_{nullptr};
  sensor::Sensor *dc_field_count_{nullptr};
  sensor::Sensor *positive_active_energy_total_{nullptr};
  sensor::Sensor *positive_active_energy_t1_{nullptr};
  sensor::Sensor *positive_active_energy_t2_{nullptr};
  sensor::Sensor *negative_active_energy_total_{nullptr};
  sensor::Sensor *negative_active_energy_t1_{nullptr};
  sensor::Sensor *negative_active_energy_t2_{nullptr};
  sensor::Sensor *imported_inductive_reactive_energy_total_{nullptr};
  sensor::Sensor *imported_inductive_reactive_energy_t1_{nullptr};
  sensor::Sensor *imported_inductive_reactive_energy_t2_{nullptr};
  sensor::Sensor *imported_capacitive_reactive_energy_total_{nullptr};
  sensor::Sensor *imported_capacitive_reactive_energy_t1_{nullptr};
  sensor::Sensor *imported_capacitive_reactive_energy_t2_{nullptr};
  sensor::Sensor *exported_inductive_reactive_energy_total_{nullptr};
  sensor::Sensor *exported_inductive_reactive_energy_t1_{nullptr};
  sensor::Sensor *exported_inductive_reactive_energy_t2_{nullptr};
  sensor::Sensor *exported_capacitive_reactive_energy_total_{nullptr};
  sensor::Sensor *exported_capacitive_reactive_energy_t1_{nullptr};
  sensor::Sensor *exported_capacitive_reactive_energy_t2_{nullptr};
  sensor::Sensor *instantaneous_voltage_p1_{nullptr};
  sensor::Sensor *instantaneous_voltage_p2_{nullptr};
  sensor::Sensor *instantaneous_voltage_p3_{nullptr};
  sensor::Sensor *instantaneous_current_p1_{nullptr};
  sensor::Sensor *instantaneous_current_p2_{nullptr};
  sensor::Sensor *instantaneous_current_p3_{nullptr};
  sensor::Sensor *instantaneous_power_factor_{nullptr};
  sensor::Sensor *instantaneous_power_factor_p1_{nullptr};
  sensor::Sensor *instantaneous_power_factor_p2_{nullptr};
  sensor::Sensor *instantaneous_power_factor_p3_{nullptr};
};

}  // namespace landisgyr
}  // namespace esphome