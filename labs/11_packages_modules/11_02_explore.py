'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

'''
# Tested 14-08-2019
import requests
import numpy as np

r = requests.get('https://github.com/timeline.json')
print(r)

a = np.arange(15).reshape(3, 5)
print(a)
