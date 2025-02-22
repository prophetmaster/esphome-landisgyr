"""Landis+Gyr smart meter component for ESPHome."""
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor"]

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

landisgyr_ns = cg.esphome_ns.namespace("landisgyr")
LandisGyrComponent = landisgyr_ns.class_("LandisGyrComponent", cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(LandisGyrComponent),
    cv.Optional(CONF_ERROR_CODE): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_CUSTOMER_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_FIRMWARE_VERSION): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_METER_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_MANUFACTURING_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_STATUS_FLAG): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_EVENT_POWER_DOWN_COUNTER): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_TERMINAL_COVER_REMOVAL_COUNTER): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_DC_FIELD_COUNT): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_POSITIVE_ACTIVE_ENERGY_TOTAL): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_POSITIVE_ACTIVE_ENERGY_T1): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_POSITIVE_ACTIVE_ENERGY_T2): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_NEGATIVE_ACTIVE_ENERGY_TOTAL): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_NEGATIVE_ACTIVE_ENERGY_T1): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_NEGATIVE_ACTIVE_ENERGY_T2): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_VOLTAGE_P1): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_VOLTAGE_P2): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_VOLTAGE_P3): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_CURRENT_P1): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_CURRENT_P2): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_CURRENT_P3): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR_P1): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR_P2): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR_P3): cv.use_id(sensor.Sensor),
}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_ERROR_CODE in config:
        sens = await cg.get_variable(config[CONF_ERROR_CODE])
        cg.add(var.set_error_code_sensor(sens))
    if CONF_CUSTOMER_ID in config:
        sens = await cg.get_variable(config[CONF_CUSTOMER_ID])
        cg.add(var.set_customer_id_sensor(sens))
    if CONF_FIRMWARE_VERSION in config:
        sens = await cg.get_variable(config[CONF_FIRMWARE_VERSION])
        cg.add(var.set_firmware_version_sensor(sens))
    # ... Add all other sensors similarly
