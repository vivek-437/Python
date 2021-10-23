import time
from plyer import notification

reltime=input("Input time in 24hr format(HH:MM:SS):-")
relmssg=input("Enter your message:-")
while True:
    current_time=time.strftime("%H:%M:%S")
    if current_time==reltime:
        print(current_time)
        break
title="Notification"

notification.notify(title=title,message=relmssg,timeout=10,toast=False)