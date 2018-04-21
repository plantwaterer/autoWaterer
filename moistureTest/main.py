import RPi.GPIO as gpio
import time
import logging

import Adafruit

# Setup logger
logger = logging.getLogger('moisture-test-log')
logger.setLevel(logging.debug)
handler = logging.FileHandler('moistureTest.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)10s - %(message)s')
