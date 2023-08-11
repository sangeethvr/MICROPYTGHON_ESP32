import machine

# I2C configuration
I2C_SCL_PIN = 22  # GPIO pin for the I2C clock signal
I2C_SDA_PIN = 21  # GPIO pin for the I2C data signal
I2C_FREQ = 100000 # I2C frequency in Hz (usually 100 kHz for standard mode)

# Initialize I2C bus
i2c = machine.I2C(
    scl=machine.Pin(I2C_SCL_PIN),
    sda=machine.Pin(I2C_SDA_PIN),
    freq=I2C_FREQ
)

# I2C device address
DEVICE_ADDR = 0x48  # Replace with your device's actual address

# Read data from the I2C device
def read_i2c_data():
    data = i2c.readfrom(DEVICE_ADDR, 2)  # Read 2 bytes of data
    # Interpret the data based on your sensor's datasheet
    # For example, if you're reading a temperature sensor like TMP102:
    # temperature = ((data[0] << 8) | data[1]) >> 4
    return data

# Main loop
while True:
    i2c_data = read_i2c_data()
    print("I2C Data:", i2c_data)
    machine.delay(1000)  # Delay for a second before reading again
