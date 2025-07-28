# VSDSquadron PRO RISC-V Development Board

![VSDSquadron PRO](https://www.vlsisystemdesign.com/wp-content/uploads/2024/09/fe310-g002-datasheet-v1p2.pdf)

## Overview

The **VSDSquadron PRO** is a powerful RISC-V-based development board, powered by the SiFive FE310-G002 SoC. 
It is tailored for **IoT**, **Edge Computing**, **AI**, and **Machine Learning** projects, offering an educational and hands-on platform to explore open-source hardware.

---

## Key Features

- **RISC-V Core**: 32-bit RV32IMAC (SiFive E3 Series Core)
- **Memory**:
  - 16KB L1 Instruction Cache
  - 16KB Data SRAM
- **Clock Speed**: 320 MHz
- **Power Efficiency**: Low-power standby mode, multiple power domains
- **Debugging**: RISC-V debug spec 0.13 compliant
- **USB Interface**: USB Type-C for programming, serial communication, and debugging
- **I/O**:
  - 19 Digital IOs
  - 9 PWM pins
  - 2 UART, 1 I2C, SPI with multiple chip selects
- **Flash Memory**: 32Mbit ISSI SPI Flash
- **Form Factor**: 84mm x 52mm

---

## Kit Contents

- VSDSquadron PRO RISC-V Board (x1)

---

## Getting Started

1. **Driver Installation**  
   Use [Zadig](https://zadig.akeo.ie/) to install `libusb-win32` for `Dual RS-232-HS`.

2. **Download & Extract IDE**  
   - Download [Freedom Studio](https://vsd-labs.sgp1.cdn.digitaloceanspaces.com/vsd-labs/VSDSquadronPRO.tar.gz)
   - Extract to `C:\` or `D:\`

3. **Running sifive-welcome Example**  
   - Launch Freedom Studio
   - Create a new workspace
   - Import the `sifive-welcome` example project
   - Start a debug session via OpenOCD
   - View output on COM port; the onboard LED should blink

---

## Hardware Overview

- **USB-C Interface**
- **FE310-G002 SoC**
- **GPIO/I2C/UART/SPI Pin Assignments**
- **Silkscreen Views**:
  - Top and Bottom component placements included in documentation

---

## Operating Guidelines

- **Temperature**: 20°C to 35°C (Room Temperature)
- **Power Supply**: 5V input via USB
- **ESD Handling**: Use antistatic precautions when handling the board

---

## Documentation

- 📘 [FE310-G002 Datasheet](https://www.vlsisystemdesign.com/wp-content/uploads/2024/09/fe310-g002-datasheet-v1p2.pdf)
- 📘 [FE310-G002 Manual](https://www.vlsisystemdesign.com/wp-content/uploads/2024/09/fe310-g002-v1p5.pdf)

---

## Help & Support

- 📧 Email: [vsd@vlsisystemdesign.com](mailto:vsd@vlsisystemdesign.com)
- 💬 Slack: [vsdsquadron.slack.com](https://vsdsquadron.slack.com/)

---

## License

© 2024 VLSI System Design (VSD). All rights reserved.

---

## Revision History

- **v1.0** – Initial release of VSDSquadron PRO Documentation

