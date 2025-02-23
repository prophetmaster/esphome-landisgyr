import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_POWER_FACTOR,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_KILOWATT_HOURS,
    UNIT_AMPERE,
    UNIT_VOLT,
)

CODEOWNERS = ["@prophetmaster"]
DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor"]

landisgyr_ns = cg.esphome_ns.namespace("landisgyr")
LandisGyrComponent = landisgyr_ns.class_("LandisGyrComponent", cg.Component, uart.UARTDevice)

CONF_ERROR_CODE = "error_code"
CONF_CUSTOMER_ID = "customer_id"
CONF_FIRMWARE_VERSION = "firmware_version"
CONF_METER_ID = "meter_id"
CONF_MANUFACTURING_ID = "manufacturing_id"
CONF_STATUS_FLAG = "status_flag"
CONF_EVENT_POWER_DOWN_COUNTER = "event_power_down_counter"
CONF_TERMINAL_COVER_REMOVAL_COUNTER = "terminal_cover_removal_counter"
CONF_DC_FIELD_COUNT = "dc_field_count"
CONF_POSITIVE_ACTIVE_ENERGY_TOTAL = "positive_active_energy_total"
CONF_POSITIVE_ACTIVE_ENERGY_T1 = "positive_active_energy_t1"
CONF_POSITIVE_ACTIVE_ENERGY_T2 = "positive_active_energy_t2"
CONF_NEGATIVE_ACTIVE_ENERGY_TOTAL = "negative_active_energy_total"
CONF_NEGATIVE_ACTIVE_ENERGY_T1 = "negative_active_energy_t1"
CONF_NEGATIVE_ACTIVE_ENERGY_T2 = "negative_active_energy_t2"
CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL = "imported_inductive_reactive_energy_total"
CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_T1 = "imported_inductive_reactive_energy_t1"
CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_T2 = "imported_inductive_reactive_energy_t2"
CONF_IMPORTED_CAPACITIVE_REACTIVE_ENERGY_TOTAL = "imported_capacitive_reactive_energy_total"
CONF_IMPORTED_CAPACITIVE_REACTIVE_ENERGY_T1 = "imported_capacitive_reactive_energy_t1"
CONF_IMPORTED_CAPACITIVE_REACTIVE_ENERGY_T2 = "imported_capacitive_reactive_energy_t2"
CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL = "exported_inductive_reactive_energy_total"
CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_T1 = "exported_inductive_reactive_energy_t1"
CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_T2 = "exported_inductive_reactive_energy_t2"
CONF_EXPORTED_CAPACITIVE_REACTIVE_ENERGY_TOTAL = "exported_capacitive_reactive_energy_total"
CONF_EXPORTED_CAPACITIVE_REACTIVE_ENERGY_T1 = "exported_capacitive_reactive_energy_t1"
CONF_EXPORTED_CAPACITIVE_REACTIVE_ENERGY_T2 = "exported_capacitive_reactive_energy_t2"
CONF_INSTANTANEOUS_VOLTAGE_P1 = "instantaneous_voltage_p1"
CONF_INSTANTANEOUS_VOLTAGE_P2 = "instantaneous_voltage_p2"
CONF_INSTANTANEOUS_VOLTAGE_P3 = "instantaneous_voltage_p3"
CONF_INSTANTANEOUS_CURRENT_P1 = "instantaneous_current_p1"
CONF_INSTANTANEOUS_CURRENT_P2 = "instantaneous_current_p2"
CONF_INSTANTANEOUS_CURRENT_P3 = "instantaneous_current_p3"
CONF_INSTANTANEOUS_POWER_FACTOR = "instantaneous_power_factor"
CONF_INSTANTANEOUS_POWER_FACTOR_P1 = "instantaneous_power_factor_p1"
CONF_INSTANTANEOUS_POWER_FACTOR_P2 = "instantaneous_power_factor_p2"
CONF_INSTANTANEOUS_POWER_FACTOR_P3 = "instantaneous_power_factor_p3"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(LandisGyrComponent),
    cv.GenerateID(uart.CONF_UART_ID): cv.use_id(uart.UARTComponent),
    cv.Optional("error_code"): sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    cv.Optional("customer_id"): sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    cv.Optional("firmware_version"): sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    cv.Optional("meter_id"): sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    cv.Optional("manufacturing_id"): sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    cv.Optional("status_flag"): sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    cv.Optional("event_power_down_counter"): sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    cv.Optional("terminal_cover_removal_counter"): sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    cv.Optional("dc_field_count"): sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    cv.Optional("positive_active_energy_total"): sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("positive_active_energy_t1"): sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("positive_active_energy_t2"): sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("negative_active_energy_total"): sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("negative_active_energy_t1"): sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("negative_active_energy_t2"): sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("imported_inductive_reactive_energy_total"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("imported_inductive_reactive_energy_t1"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("imported_inductive_reactive_energy_t2"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("imported_capacitive_reactive_energy_total"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("imported_capacitive_reactive_energy_t1"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("imported_capacitive_reactive_energy_t2"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("exported_inductive_reactive_energy_total"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("exported_inductive_reactive_energy_t1"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("exported_inductive_reactive_energy_t2"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("exported_capacitive_reactive_energy_total"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("exported_capacitive_reactive_energy_t1"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("exported_capacitive_reactive_energy_t2"): sensor.sensor_schema(
        unit_of_measurement="kvarh",
        icon="mdi:counter",
        accuracy_decimals=5,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    cv.Optional("instantaneous_voltage_p1"): sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        icon="mdi:lightning-bolt",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("instantaneous_voltage_p2"): sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        icon="mdi:lightning-bolt",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("instantaneous_voltage_p3"): sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        icon="mdi:lightning-bolt",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("instantaneous_current_p1"): sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        icon="mdi:current-ac",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("instantaneous_current_p2"): sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        icon="mdi:current-ac",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("instantaneous_current_p3"): sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        icon="mdi:current-ac",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("instantaneous_power_factor"): sensor.sensor_schema(
        icon="mdi:power-plug",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_POWER_FACTOR,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("instantaneous_power_factor_p1"): sensor.sensor_schema(
        icon="mdi:power-plug",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_POWER_FACTOR,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("instantaneous_power_factor_p2"): sensor.sensor_schema(
        icon="mdi:power-plug",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_POWER_FACTOR,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("instantaneous_power_factor_p3"): sensor.sensor_schema(
        icon="mdi:power-plug",
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_POWER_FACTOR,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
})

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    
    uart_component = yield cg.get_variable(config[uart.CONF_UART_ID])
    cg.add(var.set_uart_parent(uart_component))

    if "error_code" in config:
        sens = yield sensor.new_sensor(config["error_code"])
        cg.add(var.set_error_code_sensor(sens))
    if "customer_id" in config:
        sens = yield sensor.new_sensor(config["customer_id"])
        cg.add(var.set_customer_id_sensor(sens))
    if "firmware_version" in config:
        sens = yield sensor.new_sensor(config["firmware_version"])
        cg.add(var.set_firmware_version_sensor(sens))
    if "meter_id" in config:
        sens = yield sensor.new_sensor(config["meter_id"])
        cg.add(var.set_meter_id_sensor(sens))
    if "manufacturing_id" in config:
        sens = yield sensor.new_sensor(config["manufacturing_id"])
        cg.add(var.set_manufacturing_id_sensor(sens))
    if "status_flag" in config:
        sens = yield sensor.new_sensor(config["status_flag"])
        cg.add(var.set_status_flag_sensor(sens))
    if "event_power_down_counter" in config:
        sens = yield sensor.new_sensor(config["event_power_down_counter"])
        cg.add(var.set_event_power_down_counter_sensor(sens))
    if "terminal_cover_removal_counter" in config:
        sens = yield sensor.new_sensor(config["terminal_cover_removal_counter"])
        cg.add(var.set_terminal_cover_removal_counter_sensor(sens))
    if "dc_field_count" in config:
        sens = yield sensor.new_sensor(config["dc_field_count"])
        cg.add(var.set_dc_field_count_sensor(sens))
    if "positive_active_energy_total" in config:
        sens = yield sensor.new_sensor(config["positive_active_energy_total"])
        cg.add(var.set_positive_active_energy_total_sensor(sens))
    if "positive_active_energy_t1" in config:
        sens = yield sensor.new_sensor(config["positive_active_energy_t1"])
        cg.add(var.set_positive_active_energy_t1_sensor(sens))
    if "positive_active_energy_t2" in config:
        sens = yield sensor.new_sensor(config["positive_active_energy_t2"])
        cg.add(var.set_positive_active_energy_t2_sensor(sens))
    if "negative_active_energy_total" in config:
        sens = yield sensor.new_sensor(config["negative_active_energy_total"])
        cg.add(var.set_negative_active_energy_total_sensor(sens))
    if "negative_active_energy_t1" in config:
        sens = yield sensor.new_sensor(config["negative_active_energy_t1"])
        cg.add(var.set_negative_active_energy_t1_sensor(sens))
    if "negative_active_energy_t2" in config:
        sens = yield sensor.new_sensor(config["negative_active_energy_t2"])
        cg.add(var.set_negative_active_energy_t2_sensor(sens))
    if "imported_inductive_reactive_energy_total" in config:
        sens = yield sensor.new_sensor(config["imported_inductive_reactive_energy_total"])
        cg.add(var.set_imported_inductive_reactive_energy_total_sensor(sens))
    if "imported_inductive_reactive_energy_t1" in config:
        sens = yield sensor.new_sensor(config["imported_inductive_reactive_energy_t1"])
        cg.add(var.set_imported_inductive_reactive_energy_t1_sensor(sens))
    if "imported_inductive_reactive_energy_t2" in config:
        sens = yield sensor.new_sensor(config["imported_inductive_reactive_energy_t2"])
        cg.add(var.set_imported_inductive_reactive_energy_t2_sensor(sens))
    if "imported_capacitive_reactive_energy_total" in config:
        sens = yield sensor.new_sensor(config["imported_capacitive_reactive_energy_total"])
        cg.add(var.set_imported_capacitive_reactive_energy_total_sensor(sens))
    if "imported_capacitive_reactive_energy_t1" in config:
        sens = yield sensor.new_sensor(config["imported_capacitive_reactive_energy_t1"])
        cg.add(var.set_imported_capacitive_reactive_energy_t1_sensor(sens))
    if "imported_capacitive_reactive_energy_t2" in config:
        sens = yield sensor.new_sensor(config["imported_capacitive_reactive_energy_t2"])
        cg.add(var.set_imported_capacitive_reactive_energy_t2_sensor(sens))
    if "exported_inductive_reactive_energy_total" in config:
        sens = yield sensor.new_sensor(config["exported_inductive_reactive_energy_total"])
        cg.add(var.set_exported_inductive_reactive_energy_total_sensor(sens))
    if "exported_inductive_reactive_energy_t1" in config:
        sens = yield sensor.new_sensor(config["exported_inductive_reactive_energy_t1"])
        cg.add(var.set_exported_inductive_reactive_energy_t1_sensor(sens))
    if "exported_inductive_reactive_energy_t2" in config:
        sens = yield sensor.new_sensor(config["exported_inductive_reactive_energy_t2"])
        cg.add(var.set_exported_inductive_reactive_energy_t2_sensor(sens))
    if "exported_capacitive_reactive_energy_total" in config:
        sens = yield sensor.new_sensor(config["exported_capacitive_reactive_energy_total"])
        cg.add(var.set_exported_capacitive_reactive_energy_total_sensor(sens))
    if "exported_capacitive_reactive_energy_t1" in config:
        sens = yield sensor.new_sensor(config["exported_capacitive_reactive_energy_t1"])
        cg.add(var.set_exported_capacitive_reactive_energy_t1_sensor(sens))
    if "exported_capacitive_reactive_energy_t2" in config:
        sens = yield sensor.new_sensor(config["exported_capacitive_reactive_energy_t2"])
        cg.add(var.set_exported_capacitive_reactive_energy_t2_sensor(sens))
    if "instantaneous_voltage_p1" in config:
        sens = yield sensor.new_sensor(config["instantaneous_voltage_p1"])
        cg.add(var.set_instantaneous_voltage_p1_sensor(sens))
    if "instantaneous_voltage_p2" in config:
        sens = yield sensor.new_sensor(config["instantaneous_voltage_p2"])
        cg.add(var.set_instantaneous_voltage_p2_sensor(sens))
    if "instantaneous_voltage_p3" in config:
        sens = yield sensor.new_sensor(config["instantaneous_voltage_p3"])
        cg.add(var.set_instantaneous_voltage_p3_sensor(sens))
    if "instantaneous_current_p1" in config:
        sens = yield sensor.new_sensor(config["instantaneous_current_p1"])
        cg.add(var.set_instantaneous_current_p1_sensor(sens))
    if "instantaneous_current_p2" in config:
        sens = yield sensor.new_sensor(config["instantaneous_current_p2"])
        cg.add(var.set_instantaneous_current_p2_sensor(sens))
    if "instantaneous_current_p3" in config:
        sens = yield sensor.new_sensor(config["instantaneous_current_p3"])
        cg.add(var.set_instantaneous_current_p3_sensor(sens))
    if "instantaneous_power_factor" in config:
        sens = yield sensor.new_sensor(config["instantaneous_power_factor"])
        cg.add(var.set_instantaneous_power_factor_sensor(sens))
    if "instantaneous_power_factor_p1" in config:
        sens = yield sensor.new_sensor(config["instantaneous_power_factor_p1"])
        cg.add(var.set_instantaneous_power_factor_p1_sensor(sens))
    if "instantaneous_power_factor_p2" in config:
        sens = yield sensor.new_sensor(config["instantaneous_power_factor_p2"])
        cg.add(var.set_instantaneous_power_factor_p2_sensor(sens))
    if "instantaneous_power_factor_p3" in config:
        sens = yield sensor.new_sensor(config["instantaneous_power_factor_p3"])
        cg.add(var.set_instantaneous_power_factor_p3_sensor(sens))