import time
import re

def sanitize_url(url):
    return re.sub("[^-A-Za-z0-9+&@#/%?=~_|!:,.;\(\)]", "", url)
    
def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        val = func(*args, **kwargs)
        exe_time = time.time() - begin
        print("Total time taken in ms: ",func.__name__, exe_time*1000)
        return val
    return inner1

