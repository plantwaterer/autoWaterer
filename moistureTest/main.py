import RPi.GPIO as gpio
import time
import logging
import traceback

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Setup logger
logger = logging.getLogger('moisture-test-log')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('moistureTest.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)10s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Setup ADC
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
logger.info("ADC Setup")

try:
	while(1):
		with open('moisture.log', 'a') as f:
			f.write(str(mcp.read_adc(0)) + "," + str(mcp.read_adc(1)) + "," + str(mcp.read_adc(2)) + "\n")
			time.sleep(1)

except:
	logger.error("Failure!")
	logger.error(traceback.print_exc())
