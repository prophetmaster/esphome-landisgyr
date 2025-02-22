# Landis+Gyr ESPHome Component

ESPHome component for reading Landis+Gyr smart meters via their optical interface. Compatible with ESPHome and Home Assistant.

## Quick Start

1. Add the external component to your ESPHome configuration:
```yaml
external_components:
  - source: github://prophetmaster/esphome-landisgyr
    components: [ landisgyr ]
```

2. Configure UART for your optical probe:
```yaml
uart:
  tx_pin: GPIO17  # Adjust according to your setup
  rx_pin: GPIO16  # Adjust according to your setup
  baud_rate: 300
  data_bits: 7
  parity: EVEN
  stop_bits: 1
```

3. Add sensors you want to monitor:
```yaml
sensor:
  - platform: landisgyr
    positive_active_energy_total:
      name: "Total Active Energy"
      unit_of_measurement: "kWh"
    voltage_p1:
      name: "Phase 1 Voltage"
      unit_of_measurement: "V"
```

See [example_landisgyr.yaml](example_landisgyr.yaml) for a complete configuration with all available sensors.

## Hardware Setup

1. Required components:
   - ESP32 board
   - Optical probe compatible with Landis+Gyr meters
   - USB cable for flashing

2. Connections:
   - Connect optical probe TX to ESP32 RX (default: GPIO16)
   - Connect optical probe RX to ESP32 TX (default: GPIO17)
   - Power your ESP32 via USB or external power supply

3. Physical setup:
   - Align the optical probe with the meter's IR interface
   - Ensure stable mounting to prevent misalignment
   - Keep the probe away from strong light sources

## Available Measurements

### Energy Values
- **Total Active Energy**: Import/Export (kWh)
- **Tariff Energy**: T1/T2 readings (kWh)
- **Reactive Energy**: Import/Export (kvarh)

### Instantaneous Readings
- **Voltage**: Per phase (V)
- **Current**: Per phase (A)
- **Power Factor**: Total and per phase

### Status Information
- Error codes
- Customer ID
- Firmware version
- Meter ID
- Manufacturing ID
- Status flags
- Event counters

## Troubleshooting

1. Enable debug logging in your configuration:
```yaml
logger:
  level: DEBUG
  logs:
    landisgyr: DEBUG
```

2. Common issues:
   - No readings: Check optical probe alignment
   - Communication errors: Verify UART settings
   - Invalid values: Check checksum validation logs

## Support

- Report issues on GitHub
- Join ESPHome Discord for community support
- Check ESPHome documentation for general setup help

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.