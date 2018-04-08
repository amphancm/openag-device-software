# Set system path to project root directory via relative imports
import sys
sys.path.append("../")

# Import standard python modules
import time, logging

# Import device comms
from device.comms.i2c import I2C

# Run main
if __name__ == "__main__":
    """ Runs sht25 temperature and humidity sensor for hardware testing. """

    # Initialize command line args
    no_mux = False
    set_mux = False
    logging_enabled = False

    # Get device config from command line args
    if "--fs1" in sys.argv:
        print("Config: Food Server Rack v1")
        bus = 2
        mux =0x77
        channel = 1
        address = 0x40
    elif "--edu1" in sys.argv:
        print("Config: PFC-EDU v1")
        bus = 2
        mux =0x77
        channel = 1
        address = 0x40
    else:
        print("Config: Default")
        bus = 2
        mux =0x77
        channel = 1
        address = 0x40

    # Get run options from command line args
    if '--no-mux' in sys.argv:
        print("Running with no mux!")
        no_mux = True
    if "--set-mux" in sys.argv:
        print("Setting mux!")
        set_mux = True
    if "--logging" in sys.argv:
        logging_enabled = True
        print("Logging enabled!")

    # Activate logging if enabled
    if logging_enabled:
        logging.basicConfig(level=logging.DEBUG)

    # Initialize i2c communication
    if set_mux:
        # Initialize i2c communication directly with mux
        dev = I2C(bus=bus, address=mux)
    elif no_mux:
        # Initialize i2c communication directly with sensor
        dev = I2C(bus=bus, address=address)
    else:
        # Initialize i2c communication via mux with sensor
        dev = I2C(bus=bus, mux=mux, channel=channel, address=address)

    # Set mux then return if enabled
    if set_mux:
        # Set mux channel
        dev.write([channel])
        sys.exit()

    # Get temperature
    if logging_enabled: print("Getting temperature")
    dev.write([0xF3]) # Send get temperature command (no hold master)
    time.sleep(0.5) # Wait for sensor to process
    msb, lsb = dev.read(2) # Read sensor data
    raw = msb * 256 + lsb  # Convert temperature data
    temperature = -46.85 + ((raw * 175.72) / 65536.0)
    temperature = float("{:.0f}".format(temperature)) # Set significant figures # Set significant figures
    print("Temperature: {}".format(temperature))

    # Get humidity
    if logging_enabled: print("Getting humidity")
    dev.write([0xF5]) # Send get humidity command (no hold master)
    time.sleep(0.5) # Wait for sensor to process
    msb, lsb = dev.read(2) # Read sensor data
    raw = msb * 256 + lsb # Convert humidity data
    humidity = -6 + ((raw * 125.0) / 65536.0)
    humidity = float("{:.0f}".format(humidity)) # Set significant figures # Set significant figures
    print("Humidity: {}".format(humidity))