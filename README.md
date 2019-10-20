Requirements

1. Python (3.7 or greater) and pip
    <https://www.python.org/downloads/windows/>

2. Teraterm
    <https://filehippo.com/download_tera_term/>

3. Python packages
    pip install esptool.py
    pip install adafruit-ampy

4. CP210x driver
    <https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers>

5. Micropython firmware
    <http://micropython.org/download>

Burning Bootloader

1. Erase existing flash
    esptool.py --port PORT erase_flash

2. Burn micropython firmware
    esptool.py --port PORT --baud 460800 write_flash --flash_size=detect 0 PATH_TO_FIRMWARE
    esptool.py --chip esp32 --port PORT write_flash -z 0x1000 PATH_TO_FIRMWARE

3. Transfer files
    ampy -p PORT put PATH_TO_FILE

Basic Commands

1. Chip id
    esptool.py -p PORT chip_id 

2. Hello World
    print("Hello World")

3. Check firmware
    import esp
    esp.check_fw()
    esp.hall_sensor()
    esp.raw_temperature()
