#!/usr/bin/python

import screen
import time
import Adafruit_GPIO.SPI as SPI
from Adafruit_MAX31856 import MAX31856 as MAX31856

READY_FLOOR = 200
SOFTWARE_SPI = {"clk": 13, "cs": 0, "do": 6, "di": 5}

class Coffee:
  def __init__(self):
    self.screen = screen.Screen(180)
    self.last_ready = time.time()
    self.last_temp = 0
    self.thermocouple = MAX31856(software_spi=SOFTWARE_SPI)

  def start(self):
    while True:
      temp = int(self.__get_f(self.thermocouple.read_temp_c()))

      if temp >= READY_FLOOR:
        self.last_ready = time.time()

      self.last_temp = temp

      self.screen.update_header(self.__get_header_message(temp))
      self.screen.update_body(self.__get_body_message(temp))
      self.screen.update_footer(self.__get_footer_message(temp))
      self.screen.write()

      time.sleep(10)

  def __get_header_message(self, temp):
    if temp > READY_FLOOR:
      return "Ready :D"
    else:
      return u"Heating\u2026"

  def __get_body_message(self, temp):
    if temp < READY_FLOOR:
      mins_ago = int((time.time() - self.last_ready) / 60)
      hours_ago = int(mins_ago / 60)

      if mins_ago == 0:
        return "Just brewed"
      elif hours_ago > 1
        return "Brewed {0} hours ago".format(hours_ago)
      else:
        return "Brewed {0} mins ago".format(mins_ago)
    else:
      return ""

  def __get_footer_message(self, temp):
    if temp > READY_FLOOR:
      return "Water Temp: {0}*F".format(temp)
    else:
      return "Temp: {0}* / {1}*F".format(temp, READY_FLOOR)

  def __get_f(self, celcius_temp):
    return celcius_temp * 9.0 / 5.0 + 32.0


coffee = Coffee()
coffee.start()
