# Landis+Gyr ESPHome Component

This ESPHome component enables communication with Landis+Gyr smart meters via their optical interface. It supports reading various meter values including energy consumption, voltage, current, and power factor measurements.

## Features

- Serial communication at 300 baud with 7E1 configuration
- Automatic message framing and checksum validation
- Support for multiple meter values and measurements
- Real-time data reading and publishing to Home Assistant

## Supported Measurements

### Special Values
- Error code (F.F)
- Customer identification (0.0)
- Firmware Version (0.2.0)
- Meter ID (C.1.0)
- Manufacturing ID (C.1.1)
- Status Flag (C.5.0)
- Event power down counter (C.7.0)

### Security
- Terminal cover removal counter (82.8.1)
- DC Field Count (82.8.2)

### Energy Measurements
- Positive active energy (A+) total and tariffs T1/T2 (1.8.0/1/2)
- Negative active energy (A-) total and tariffs T1/T2 (2.8.0/1/2)
- Imported/Exported reactive energy for all quadrants (5.8.0/1/2 through 8.8.0/1/2)

### Instantaneous Values
- Voltage per phase (32.7, 52.7, 72.7)
- Current per phase (31.7, 51.7, 71.7)
- Power factor total and per phase (13.7, 33.7, 53.7, 73.7)

## Configuration

Example configuration in your ESPHome YAML file:

```yaml
uart:
  id: uart_bus
  tx_pin: GPIO1
  rx_pin: GPIO3
  baud_rate: 300
  data_bits: 7
  parity: EVEN
  stop_bits: 1

landisgyr:
  uart_id: uart_bus
  # Define sensors you want to monitor
  error_code:
    name: "Meter Error Code"
  customer_id:
    name: "Customer ID"
  positive_active_energy_total:
    name: "Total Active Energy"
    unit_of_measurement: "kWh"
  voltage_p1:
    name: "Phase 1 Voltage"
    unit_of_measurement: "V"
```

## Protocol Details

The component implements the IEC 62056-21 protocol for communication with the meter:

1. Initialization sequence with `/?!` command
2. Baud rate acknowledgment with `<ACK>000`
3. Message framing with STX/ETX
4. XOR checksum validation

## Hardware Setup

1. Connect an optical probe to your ESP32's UART pins
2. Ensure proper alignment with the meter's optical interface
3. Use appropriate voltage levels (typically 3.3V)

## Debugging

The component includes detailed logging for troubleshooting:
- Message reception and parsing
- Checksum validation
- Sensor value updates

## License

This component is open source and available under the MIT license.

## Contributing

Feel free to submit issues and pull requests for improvements or bug fixes.