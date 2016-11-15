import time
def pause(t):
    def wrapper(func):
        def tmp(*args, **kwargs):
            time.sleep(t)
            return func(*args, **kwargs)
        tmp.__name__ = func.__name__
        tmp.__module__ = func.__module__
        tmp.__doc__ = func.__doc__
        return tmp
    return wrapper

def timer(func):
    def tmp(*args, **kwargs):
        tstart = time.time()
        result = func(*args, **kwargs)
        tend = time.time()
        print ("Function [",func.__name__,"] completed its work of", (tend-tstart), "sek")
        return result
    tmp.__name__ = func.__name__
    tmp.__module__ = func.__module__
    tmp.__doc__ = func.__doc__
    return tmp

def morefunc(func):
    def tmp(*args, **kwargs):
        print ("\n\rFunction Name: [",func.__name__,"] -- args", args)
        result = func(*args, **kwargs)
        return result
    
    tmp.__name__ = func.__name__
    tmp.__module__ = func.__module__
    tmp.__doc__ = func.__doc__
    return tmp


@timer
@pause(3)
def func3():
    pass

func3()

@timer
@pause(2)
def func2():
    pass

func2()


@morefunc
@timer
@pause(1)
def func1(arg1, arg2,arg3):
    print("Result:")
    pass
func1("1arg", "2arg","3arg" )

#region
#import functools
#def trace (func):
#    def inner(*args, **kwargs):
#        return func(*args, **kwargs)
#    return inner


#import time
#class timer:
#    def __init__(self):
#        self.timestart = timestart
#        return self.timestart

#    def starttimer(self):
#        self.timestart = time.time()
#        return self

#    def stoptimer():
#        time = time.time()
#        return time - self.timestart

#import time
#class timer(object):
#    def __init__(self):
#        self.timestart = None

#    def starttimer(self):
#        return self.timestart = time.time()
        

#    def stoptimer(self):
#        rtime = time.time()
#        result = rtime - self.timestart
#        return result
#def timer(func):
#    def tmp(*args, **kwargs):
#        timer.starttimer()
#        result = func(*args, **kwargs)
#        resulttime = timer.stoptimer()
#        print (func.__name__, args, kwargs, resulttime)
#        return result
#    return tmp
#endregion


