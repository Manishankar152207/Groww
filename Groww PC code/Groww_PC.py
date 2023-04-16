import requests
from nsepython import *
from datetime import datetime
from time import sleep
import pandas as pd
import os

class Groww:
  def __init__(self) -> None:
    self.flag = 0
    self.url = "https://groww.in/v1/api/stocks_data/v1/tr_live_indices/exchange/NSE/segment/CASH/BANKNIFTY/latest"
    self.payload={}
    self.price_collect()

  def price_collect(self):
    while(True):
      if running_status():
        try:
          headers = {
              'Cookie': '__cf_bm=MbFaVnWQYJ_KkCMXRh32of30MMn4uVDhBeBe6CQrXC4-1670571100-0-AY0WQ2nP67WxOLxd3ZBzhWQClyiZ+tyuE9wTidmDEJLVdvPi31r9AcL0rLIr00fc58g2kT8/6owWx3lCyYv6QDI=; __cfruid=ffc27536aaac2ac875f77e9f9811707136500b2c-1670571100; _cfuvid=fgHY8fAaWy0fGoDF1S5L42GdJluCa4kG_yq6J_m5IJ8-1670571100864-0-604800000'
            }
          response = json.loads(requests.request("GET", self.url, headers=headers, data=self.payload).text)
          response.update({'Time':str(datetime.now().time())})
          filename = str(datetime.now().date())
          if os.path.isfile(f"{filename}.txt"):
            with open(f"{filename}.txt", "a") as f:
              f.write(f"{response['type']},{response['symbol']},{response['open']},{response['high']},{response['low']},{response['close']},{response['value']},{response['dayChange']},{response['dayChangePerc']},{response['tsInMillis']},{response['Time']}\n")
          else:
            with open(f"{filename}.txt", "a") as f:
              f.write(f"type,symbol,open,high,low,close,value,dayChange,dayChangePerc,tsInMillis,Time\n")
              f.write(f"{response['type']},{response['symbol']},{response['open']},{response['high']},{response['low']},{response['close']},{response['value']},{response['dayChange']},{response['dayChangePerc']},{response['tsInMillis']},{response['Time']}\n")
          sleep(1)
        except Exception as e:
          with open("GrowwErr.txt", "a") as f:
            f.write(str(e)+"\n")
            print(e)

ob = Groww()