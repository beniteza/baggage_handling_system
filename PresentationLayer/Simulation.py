import time
import requests
import random

while(True):
    time.sleep(10)
    requests.post(
        "http://localhost:5000/bagsReachedLoadingArea")
    print('\nBAGS REACHED AIRLINE LOADING AREA!\n')

    if(random.randint(0, 100) <= 5):
        requests.post(
            "http://localhost:5000/jammed")
        print('\nCONVEYOR BELT JAMMED\n')
