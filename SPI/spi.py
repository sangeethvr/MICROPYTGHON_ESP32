import machine
import time

# Initialize SPI
spi = machine.SPI(1)  # Use SPI bus number 1
spi.init(baudrate=1000000, polarity=0, phase=0)  # Set baudrate, polarity, and phase

# Chip Select (CS) pin
cs_pin = machine.Pin(15, machine.Pin.OUT)  # Adjust pin number as needed

# Function to read data from SPI device
def read_spi_data():
    cs_pin.value(0)  # Set CS low to select the device
    data = spi.read(10)  # Read 10 bytes of data from the SPI device
    cs_pin.value(1)  # Set CS high to deselect the device
    return data

# Main loop
while True:
    spi_data = read_spi_data()
    print("SPI Data:", spi_data)
    time.sleep(1)
