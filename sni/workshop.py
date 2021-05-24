from datetime import datetime, timezone
import pytz
import time

# UTC = pytz.cat
now = datetime.now()
result = now.strftime("%a") + ', ' + now.strftime("%B") + ' ' + now.strftime("%d") + ', ' + now.strftime("%Y") + ' ' + \
         now.strftime("%X") + ' ' + time.strftime("%Z %z")
print(result)

print(now.strftime("%X"))
