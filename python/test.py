from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/1615966'
weather = get(url).json()
#print(weather)
print(weather['items'])