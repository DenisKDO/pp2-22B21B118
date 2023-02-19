import datetime
print(f"Current-{datetime.datetime.now()}\nYesterday-{datetime.datetime.now()-datetime.timedelta(days=1)}\nToday-{datetime.datetime.now()+datetime.timedelta(days=1)}")