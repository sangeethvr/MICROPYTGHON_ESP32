import machine
import uos
import ustruct

# Configuration for I2S
SAMPLE_RATE = 44100
BITS_PER_SAMPLE = 16
CHANNELS = 1
BUFFER_SIZE = 512

# Initialize I2S
i2s = machine.I2S(
    I2S_NUM=0,                   # I2S port number
    sample_rate=SAMPLE_RATE,     # Sampling rate
    bits=BITS_PER_SAMPLE,        # Bits per sample
    channel_num=CHANNELS,        # Number of channels
    data_format=machine.I2S.MONO # MONO or STEREO
)

# Create a buffer for audio data
audio_buffer = bytearray(BUFFER_SIZE)

# Loop to read and process audio data from the microphone
while True:
    i2s.readinto(audio_buffer)  # Read audio data from I2S

    # Process the audio data (you can replace this with your processing logic)
    # For example, you can save the audio data to a file, analyze it, etc.

    # Sleep for a short duration to control the rate of data processing
    uos.sleep_ms(10)
