"""Sensor platform for Landis+Gyr smart meter."""
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_POWER_FACTOR,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_AMPERE,
    UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
    UNIT_KILOWATT_HOURS,
    UNIT_VOLT,
)
from . import (
    CONF_ERROR_CODE,
    CONF_CUSTOMER_ID,
    CONF_FIRMWARE_VERSION,
    CONF_METER_ID,
    CONF_MANUFACTURING_ID,
    CONF_STATUS_FLAG,
    CONF_EVENT_POWER_DOWN_COUNTER,
    CONF_TERMINAL_COVER_REMOVAL_COUNTER,
    CONF_DC_FIELD_COUNT,
    CONF_POSITIVE_ACTIVE_ENERGY_TOTAL,
    CONF_POSITIVE_ACTIVE_ENERGY_T1,
    CONF_POSITIVE_ACTIVE_ENERGY_T2,
    CONF_NEGATIVE_ACTIVE_ENERGY_TOTAL,
    CONF_NEGATIVE_ACTIVE_ENERGY_T1,
    CONF_NEGATIVE_ACTIVE_ENERGY_T2,
    CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL,
    CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL,
    CONF_INSTANTANEOUS_VOLTAGE_P1,
    CONF_INSTANTANEOUS_VOLTAGE_P2,
    CONF_INSTANTANEOUS_VOLTAGE_P3,
    CONF_INSTANTANEOUS_CURRENT_P1,
    CONF_INSTANTANEOUS_CURRENT_P2,
    CONF_INSTANTANEOUS_CURRENT_P3,
    CONF_INSTANTANEOUS_POWER_FACTOR,
    CONF_INSTANTANEOUS_POWER_FACTOR_P1,
    CONF_INSTANTANEOUS_POWER_FACTOR_P2,
    CONF_INSTANTANEOUS_POWER_FACTOR_P3,
    LandisGyrComponent,
)

CONF_LANDISGYR_ID = "landisgyr_id"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_LANDISGYR_ID): cv.use_id(LandisGyrComponent),
    cv.Optional(CONF_ERROR_CODE): sensor.sensor_schema(),
    cv.Optional(CONF_CUSTOMER_ID): sensor.sensor_schema(),
    cv.Optional(CONF_FIRMWARE_VERSION): sensor.sensor_schema(),
    cv.Optional(CONF_METER_ID): sensor.sensor_schema(),
    cv.Optional(CONF_MANUFACTURING_ID): sensor.sensor_schema(),
    cv.Optional(CONF_STATUS_FLAG): sensor.sensor_schema(),
    cv.Optional(CONF_EVENT_POWER_DOWN_COUNTER): sensor.sensor_schema(
        state_class=STATE_CLASS_TOTAL_INCREASING
    ),
    cv.Optional(CONF_TERMINAL_COVER_REMOVAL_COUNTER): sensor.sensor_schema(
        state_class=STATE_CLASS_TOTAL_INCREASING
    ),
    cv.Optional(CONF_DC_FIELD_COUNT): sensor.sensor_schema(
        state_class=STATE_CLASS_TOTAL_INCREASING
    ),
    cv.Optional(CONF_POSITIVE_ACTIVE_ENERGY_TOTAL): sensor.sensor_schema(
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        unit_of_measurement=UNIT_KILOWATT_HOURS,
    ),
    cv.Optional(CONF_POSITIVE_ACTIVE_ENERGY_T1): sensor.sensor_schema(
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        unit_of_measurement=UNIT_KILOWATT_HOURS,
    ),
    cv.Optional(CONF_POSITIVE_ACTIVE_ENERGY_T2): sensor.sensor_schema(
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        unit_of_measurement=UNIT_KILOWATT_HOURS,
    ),
    cv.Optional(CONF_NEGATIVE_ACTIVE_ENERGY_TOTAL): sensor.sensor_schema(
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        unit_of_measurement=UNIT_KILOWATT_HOURS,
    ),
    cv.Optional(CONF_NEGATIVE_ACTIVE_ENERGY_T1): sensor.sensor_schema(
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        unit_of_measurement=UNIT_KILOWATT_HOURS,
    ),
    cv.Optional(CONF_NEGATIVE_ACTIVE_ENERGY_T2): sensor.sensor_schema(
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        unit_of_measurement=UNIT_KILOWATT_HOURS,
    ),
    cv.Optional(CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL): sensor.sensor_schema(
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
    ),
    cv.Optional(CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL): sensor.sensor_schema(
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
    ),
    cv.Optional(CONF_INSTANTANEOUS_VOLTAGE_P1): sensor.sensor_schema(
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_of_measurement=UNIT_VOLT,
    ),
    cv.Optional(CONF_INSTANTANEOUS_VOLTAGE_P2): sensor.sensor_schema(
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_of_measurement=UNIT_VOLT,
    ),
    cv.Optional(CONF_INSTANTANEOUS_VOLTAGE_P3): sensor.sensor_schema(
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_of_measurement=UNIT_VOLT,
    ),
    cv.Optional(CONF_INSTANTANEOUS_CURRENT_P1): sensor.sensor_schema(
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_of_measurement=UNIT_AMPERE,
    ),
    cv.Optional(CONF_INSTANTANEOUS_CURRENT_P2): sensor.sensor_schema(
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_of_measurement=UNIT_AMPERE,
    ),
    cv.Optional(CONF_INSTANTANEOUS_CURRENT_P3): sensor.sensor_schema(
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_of_measurement=UNIT_AMPERE,
    ),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR): sensor.sensor_schema(
        device_class=DEVICE_CLASS_POWER_FACTOR,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR_P1): sensor.sensor_schema(
        device_class=DEVICE_CLASS_POWER_FACTOR,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR_P2): sensor.sensor_schema(
        device_class=DEVICE_CLASS_POWER_FACTOR,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_INSTANTANEOUS_POWER_FACTOR_P3): sensor.sensor_schema(
        device_class=DEVICE_CLASS_POWER_FACTOR,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
})

async def to_code(config):
    hub = await cg.get_variable(config[CONF_LANDISGYR_ID])
    for key, conf in config.items():
        if key == CONF_LANDISGYR_ID:
            continue
        sens = await sensor.new_sensor(conf)
        cg.add(getattr(hub, f"set_{key}_sensor")(sens))
