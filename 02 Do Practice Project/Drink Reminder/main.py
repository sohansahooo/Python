import time
from plyer import notification

while True:
    print("Drink Water!")
    notification.notify(
        title="Drink Water!",
        message="It's time to drink water!",
    )
    time.sleep(3)
