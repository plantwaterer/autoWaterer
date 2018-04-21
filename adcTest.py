import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Hardware SPI Config:
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

while True:
	value = mcp.read_adc(1)
	print("Value: " + str(value))
	time.sleep(0.5)
