import requests, time, sys
from lxml import etree

class YR:
  url = 'https://www.yr.no/place/'
  url_prefix = '/forecast.xml'

  # location  as Geonames: Sweden/Södermanland/Himlinge 
  def __init__(self, location):
    self.location = location
    self.getData()

  def getData(self):
    try:
      # request/parsing
      r = requests.get(self.url + self.location + self.url_prefix)
      xml = lxml.etree.XML(r.content)

      self.latest_data_fetched = time.time()

      self.current_period = xml.xpath('(/weatherdata/forecast/tabular/time/@period)[1]')[0]

      # period 0 (00-06)
      self.p0_tempature = xml.xpath('(/weatherdata/forecast/tabular//time[@period="0"])[1]/temperature/@value')[0]
      self.p0_weather = xml.xpath('(/weatherdata/forecast/tabular//time[@period="0"])[1]/symbol/@name')[0].lower()
      # period 1 (06-12)
      self.p1_tempature = xml.xpath('(/weatherdata/forecast/tabular//time[@period="1"])[1]/temperature/@value')[0]
      self.p1_weather = xml.xpath('(/weatherdata/forecast/tabular//time[@period="0"])[1]/symbol/@name')[0].lower()
      # period 1 (12-18)
      self.p2_tempature = xml.xpath('(/weatherdata/forecast/tabular//time[@period="2"])[1]/temperature/@value')[0]
      self.p2_weather = xml.xpath('(/weatherdata/forecast/tabular//time[@period="0"])[1]/symbol/@name')[0].lower()
      # period 3 (18-24)
      self.p3_tempature = xml.xpath('(/weatherdata/forecast/tabular//time[@period="3"])[1]/temperature/@value')[0]
      self.p3_weather = xml.xpath('(/weatherdata/forecast/tabular//time[@period="0"])[1]/symbol/@name')[0].lower()
    except:
      raise error.with_traceback(sys.exc_info()[2])

  def getPeriodWeather(self, period):
    # check if the data is more then 15 minutes old
    diff = time.time() - self.latest_data_fetched
    if ((int(diff) / 60) > 15):
      self.getData()
    
    if (period == 0):
      return self.p0_weather
    elif (period == 1):
      return self.p1_weather
    elif (period == 2):
      return self.p2_weather
    elif (period == 3):
      return self.p3_weather

  def getPeriodTempature(self, period):
    # check if the data is more then 15 minutes old
    diff = time.time() - self.latest_data_fetched
    if ((int(diff) / 60) > 15):
      self.getData()

    if (period == 0):
      return self.p0_tempature
    elif (period == 1):
      return self.p1_tempature
    elif (period == 2):
      return self.p2_tempature
    elif (period == 3):
      return self.p3_tempature

  def getCurrentWeather(self):
    return self.getPeriodWeather(int(self.current_period))

  def getCurrentTempature(self):
    return self.getPeriodTempature(int(self.current_period))
