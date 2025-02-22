"""Landis+Gyr smart meter component for ESPHome."""
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor
from esphome.const import CONF_ID

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor"]

landisgyr_ns = cg.esphome_ns.namespace("landisgyr")
LandisGyrComponent = landisgyr_ns.class_("LandisGyrComponent", cg.Component, uart.UARTDevice)

# Configuration constants
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
CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL = "exported_inductive_reactive_energy_total"
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
    cv.Optional(CONF_ERROR_CODE): sensor.sensor_schema(),
    cv.Optional(CONF_CUSTOMER_ID): sensor.sensor_schema(),
    cv.Optional(CONF_FIRMWARE_VERSION): sensor.sensor_schema(),
    cv.Optional(CONF_METER_ID): sensor.sensor_schema(),
    cv.Optional(CONF_MANUFACTURING_ID): sensor.sensor_schema(),
    cv.Optional(CONF_STATUS_FLAG): sensor.sensor_schema(),
    cv.Optional(CONF_EVENT_POWER_DOWN_COUNTER): sensor.sensor_schema(),
    cv.Optional(CONF_TERMINAL_COVER_REMOVAL_COUNTER): sensor.sensor_schema(),
    cv.Optional(CONF_DC_FIELD_COUNT): sensor.sensor_schema(),
    cv.Optional(CONF_POSITIVE_ACTIVE_ENERGY_TOTAL): sensor.sensor_schema(),
    cv.Optional(CONF_POSITIVE_ACTIVE_ENERGY_T1): sensor.sensor_schema(),
    cv.Optional(CONF_POSITIVE_ACTIVE_ENERGY_T2): sensor.sensor_schema(),
    cv.Optional(CONF_NEGATIVE_ACTIVE_ENERGY_TOTAL): sensor.sensor_schema(),
    cv.Optional(CONF_NEGATIVE_ACTIVE_ENERGY_T1): sensor.sensor_schema(),
    cv.Optional(CONF_NEGATIVE_ACTIVE_ENERGY_T2): sensor.sensor_schema(),
    cv.Optional(CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL): sensor.sensor_schema(),
    cv.Optional(CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_VOLTAGE_P1): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_VOLTAGE_P2): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_VOLTAGE_P3): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_CURRENT_P1): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_CURRENT_P2): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_CURRENT_P3): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR_P1): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR_P2): sensor.sensor_schema(),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR_P3): sensor.sensor_schema(),
}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_ERROR_CODE in config:
        sens = await sensor.new_sensor(config[CONF_ERROR_CODE])
        cg.add(var.set_error_code_sensor(sens))
    if CONF_CUSTOMER_ID in config:
        sens = await sensor.new_sensor(config[CONF_CUSTOMER_ID])
        cg.add(var.set_customer_id_sensor(sens))
    if CONF_FIRMWARE_VERSION in config:
        sens = await sensor.new_sensor(config[CONF_FIRMWARE_VERSION])
        cg.add(var.set_firmware_version_sensor(sens))
    if CONF_METER_ID in config:
        sens = await sensor.new_sensor(config[CONF_METER_ID])
        cg.add(var.set_meter_id_sensor(sens))
    if CONF_MANUFACTURING_ID in config:
        sens = await sensor.new_sensor(config[CONF_MANUFACTURING_ID])
        cg.add(var.set_manufacturing_id_sensor(sens))
    if CONF_STATUS_FLAG in config:
        sens = await sensor.new_sensor(config[CONF_STATUS_FLAG])
        cg.add(var.set_status_flag_sensor(sens))
    if CONF_EVENT_POWER_DOWN_COUNTER in config:
        sens = await sensor.new_sensor(config[CONF_EVENT_POWER_DOWN_COUNTER])
        cg.add(var.set_event_power_down_counter_sensor(sens))
    if CONF_TERMINAL_COVER_REMOVAL_COUNTER in config:
        sens = await sensor.new_sensor(config[CONF_TERMINAL_COVER_REMOVAL_COUNTER])
        cg.add(var.set_terminal_cover_removal_counter_sensor(sens))
    if CONF_DC_FIELD_COUNT in config:
        sens = await sensor.new_sensor(config[CONF_DC_FIELD_COUNT])
        cg.add(var.set_dc_field_count_sensor(sens))
    if CONF_POSITIVE_ACTIVE_ENERGY_TOTAL in config:
        sens = await sensor.new_sensor(config[CONF_POSITIVE_ACTIVE_ENERGY_TOTAL])
        cg.add(var.set_positive_active_energy_total_sensor(sens))
    if CONF_POSITIVE_ACTIVE_ENERGY_T1 in config:
        sens = await sensor.new_sensor(config[CONF_POSITIVE_ACTIVE_ENERGY_T1])
        cg.add(var.set_positive_active_energy_t1_sensor(sens))
    if CONF_POSITIVE_ACTIVE_ENERGY_T2 in config:
        sens = await sensor.new_sensor(config[CONF_POSITIVE_ACTIVE_ENERGY_T2])
        cg.add(var.set_positive_active_energy_t2_sensor(sens))
    if CONF_NEGATIVE_ACTIVE_ENERGY_TOTAL in config:
        sens = await sensor.new_sensor(config[CONF_NEGATIVE_ACTIVE_ENERGY_TOTAL])
        cg.add(var.set_negative_active_energy_total_sensor(sens))
    if CONF_NEGATIVE_ACTIVE_ENERGY_T1 in config:
        sens = await sensor.new_sensor(config[CONF_NEGATIVE_ACTIVE_ENERGY_T1])
        cg.add(var.set_negative_active_energy_t1_sensor(sens))
    if CONF_NEGATIVE_ACTIVE_ENERGY_T2 in config:
        sens = await sensor.new_sensor(config[CONF_NEGATIVE_ACTIVE_ENERGY_T2])
        cg.add(var.set_negative_active_energy_t2_sensor(sens))
    if CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL in config:
        sens = await sensor.new_sensor(config[CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL])
        cg.add(var.set_imported_inductive_reactive_energy_total_sensor(sens))
    if CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL in config:
        sens = await sensor.new_sensor(config[CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL])
        cg.add(var.set_exported_inductive_reactive_energy_total_sensor(sens))
    if CONF_INSTANTANEOUS_VOLTAGE_P1 in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_VOLTAGE_P1])
        cg.add(var.set_instantaneous_voltage_p1_sensor(sens))
    if CONF_INSTANTANEOUS_VOLTAGE_P2 in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_VOLTAGE_P2])
        cg.add(var.set_instantaneous_voltage_p2_sensor(sens))
    if CONF_INSTANTANEOUS_VOLTAGE_P3 in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_VOLTAGE_P3])
        cg.add(var.set_instantaneous_voltage_p3_sensor(sens))
    if CONF_INSTANTANEOUS_CURRENT_P1 in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_CURRENT_P1])
        cg.add(var.set_instantaneous_current_p1_sensor(sens))
    if CONF_INSTANTANEOUS_CURRENT_P2 in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_CURRENT_P2])
        cg.add(var.set_instantaneous_current_p2_sensor(sens))
    if CONF_INSTANTANEOUS_CURRENT_P3 in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_CURRENT_P3])
        cg.add(var.set_instantaneous_current_p3_sensor(sens))
    if CONF_INSTANTANEOUS_POWER_FACTOR in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_POWER_FACTOR])
        cg.add(var.set_instantaneous_power_factor_sensor(sens))
    if CONF_INSTANTANEOUS_POWER_FACTOR_P1 in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_POWER_FACTOR_P1])
        cg.add(var.set_instantaneous_power_factor_p1_sensor(sens))
    if CONF_INSTANTANEOUS_POWER_FACTOR_P2 in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_POWER_FACTOR_P2])
        cg.add(var.set_instantaneous_power_factor_p2_sensor(sens))
    if CONF_INSTANTANEOUS_POWER_FACTOR_P3 in config:
        sens = await sensor.new_sensor(config[CONF_INSTANTANEOUS_POWER_FACTOR_P3])
        cg.add(var.set_instantaneous_power_factor_p3_sensor(sens))
