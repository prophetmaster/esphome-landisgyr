import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_VOLTAGE,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_AMPERE,
    UNIT_VOLT,
    UNIT_KILOWATT_HOURS,
    UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
)
from . import CONF_LANDISGYR_ID, LandisGyrComponent

DEPENDENCIES = ["landisgyr"]

# Configuration keys for special values
CONF_ERROR_CODE = "error_code"
CONF_CUSTOMER_ID = "customer_id"
CONF_FIRMWARE_VERSION = "firmware_version"
CONF_METER_ID = "meter_id"
CONF_MANUFACTURING_ID = "manufacturing_id"
CONF_STATUS_FLAG = "status_flag"
CONF_EVENT_POWER_DOWN_COUNTER = "event_power_down_counter"

# Configuration keys for security sensors
CONF_TERMINAL_COVER_REMOVAL_COUNTER = "terminal_cover_removal_counter"
CONF_DC_FIELD_COUNT = "dc_field_count"

# Configuration keys for energy measurements
CONF_POSITIVE_ACTIVE_ENERGY_TOTAL = "positive_active_energy_total"
CONF_POSITIVE_ACTIVE_ENERGY_T1 = "positive_active_energy_t1"
CONF_POSITIVE_ACTIVE_ENERGY_T2 = "positive_active_energy_t2"
CONF_NEGATIVE_ACTIVE_ENERGY_TOTAL = "negative_active_energy_total"
CONF_NEGATIVE_ACTIVE_ENERGY_T1 = "negative_active_energy_t1"
CONF_NEGATIVE_ACTIVE_ENERGY_T2 = "negative_active_energy_t2"

# Configuration keys for reactive energy
CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL = "imported_inductive_reactive_energy_total"
CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_T1 = "imported_inductive_reactive_energy_t1"
CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_T2 = "imported_inductive_reactive_energy_t2"
CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL = "exported_inductive_reactive_energy_total"
CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_T1 = "exported_inductive_reactive_energy_t1"
CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_T2 = "exported_inductive_reactive_energy_t2"

# Configuration keys for instantaneous values
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

# Sensor schema configurations
SENSORS = {
    CONF_ERROR_CODE: sensor.sensor_schema(),
    CONF_CUSTOMER_ID: sensor.sensor_schema(),
    CONF_FIRMWARE_VERSION: sensor.sensor_schema(),
    CONF_METER_ID: sensor.sensor_schema(),
    CONF_MANUFACTURING_ID: sensor.sensor_schema(),
    CONF_STATUS_FLAG: sensor.sensor_schema(),
    CONF_EVENT_POWER_DOWN_COUNTER: sensor.sensor_schema(),
    CONF_TERMINAL_COVER_REMOVAL_COUNTER: sensor.sensor_schema(),
    CONF_DC_FIELD_COUNT: sensor.sensor_schema(),
    
    # Energy measurements with proper units and classes
    CONF_POSITIVE_ACTIVE_ENERGY_TOTAL: sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    CONF_POSITIVE_ACTIVE_ENERGY_T1: sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    CONF_POSITIVE_ACTIVE_ENERGY_T2: sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    CONF_NEGATIVE_ACTIVE_ENERGY_TOTAL: sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    
    # Reactive energy measurements
    CONF_IMPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL: sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    CONF_EXPORTED_INDUCTIVE_REACTIVE_ENERGY_TOTAL: sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    
    # Voltage measurements
    CONF_INSTANTANEOUS_VOLTAGE_P1: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_INSTANTANEOUS_VOLTAGE_P2: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_INSTANTANEOUS_VOLTAGE_P3: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    
    # Current measurements
    CONF_INSTANTANEOUS_CURRENT_P1: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_INSTANTANEOUS_CURRENT_P2: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_INSTANTANEOUS_CURRENT_P3: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    
    # Power factor measurements
    CONF_INSTANTANEOUS_POWER_FACTOR: sensor.sensor_schema(
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_INSTANTANEOUS_POWER_FACTOR_P1: sensor.sensor_schema(
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_INSTANTANEOUS_POWER_FACTOR_P2: sensor.sensor_schema(
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_INSTANTANEOUS_POWER_FACTOR_P3: sensor.sensor_schema(
        state_class=STATE_CLASS_MEASUREMENT,
    ),
}

async def setup_sensor(config, key, hub):
    """Set up a Landis+Gyr sensor."""
    if key not in config:
        return None
    var = await sensor.new_sensor(config[key])
    cg.add(getattr(hub, f"set_{key}_sensor")(var))
    return var

async def to_code(config):
    """Set up the Landis+Gyr component."""
    hub = await cg.get_variable(config[CONF_LANDISGYR_ID])
    for key in SENSORS:
        await setup_sensor(config, key, hub)