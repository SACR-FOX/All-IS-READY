from django.test import TestCase

from datetime import datetime
# Create your tests here.
import uuid
print(uuid.uuid4())

import random
roster=[]
for i in range(10):
    u=random.randrange(1,46)
    if not roster.__contains__(u):
        roster.append(u)
    else:
        i-=1
print(roster)