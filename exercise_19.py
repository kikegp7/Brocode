# Datetime

import datetime
import time


date = datetime.date(2024,11,11)
today = datetime.date.today()

while True:

    now =  datetime.datetime.now()
    now = now.strftime("%H:%M:%S")
    print(now)
    time.sleep(1)