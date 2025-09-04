import time
def calculate_time(func):
    def wrapper(*args,**kwargs):
        time_start=time.time()
        result=func(*args,**kwargs)
        time_end=time.time()
        print(f"Time taken: {time_end-time_start} seconds")
        return result
    return wrapper

@calculate_time
def say_hi_slow():
    print("Hi, how are you?")
    time.sleep(1)
    print("I'm fine, thank you!")

say_hi_slow()




