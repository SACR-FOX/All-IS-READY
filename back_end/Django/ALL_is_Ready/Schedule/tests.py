import datetime
import time

from django.test import TestCase
now = int (time.time ())
day_time =now- now % 86400 + time. timezone
past=now-day_time
print(past)

