import time

def timer(func):
    def new_func(*args,**kw):
        start = time.time()
        result = func(*args,**kw)
        end = time.time()
        print(time.strftime('%H:%M:%S',time.gmtime(end-start)))
        return result
    return new_func