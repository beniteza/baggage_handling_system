import time
import requests
import random

while(True):
    time.sleep(10)

    if(random.randint(0, 100) <= 5):
        requests.post(
            "http://localhost:5000/jammed")
        print('\nCONVEYOR BELT JAMMED\n')

    requests.post(
        "http://localhost:5000/routeBags")
    print('\n...Routing Bags...\n')
