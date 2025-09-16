import timeit 
'''The timeit module is used to measure execution time of small
bits of Python code. It's part of the Python Standard Library (no need to install 
anything extra).'''

print(dir(timeit))

print(timeit.timeit("'Elzero' * 1000")) # returning the time that this line will take
'''
name = "Elzero"

print(name * 1000)

print(timeit.timeit("name = 'Elzero'; name * 1000")) # This line means that name * 1000 will 
 take how much time to be executed
'''

# print(random.randint(0, 50))

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))
'''
* stmt => statement to be measured time.
* random.randint(0, 50) => This string is executed 
 repeatedly to measure how long it takes.
* setup => This code is executed once before timing starts.
* It's used to set up the environment, so that random is available
 when the statement runs.
* Without this, random would be undefined in stmt.
* Default Behavior of timeit.timeit() => It runs the stmt 1 million times
 (by default) and returns the total time (in seconds) taken to execute it 
 that many times.
* So, this code tells you: "How long does it take to call 
 random.randint(0, 50) a million times?"

'''

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4)) 
# [0.594870199999832, 0.7048074000001634, 0.5623093000001518, 0.5767918999999893]
'''
* timeit.repeat() runs the same timing test multiple times and
 returns a list of timings.

* It's useful when you want to see variability in timing, 
 for example due to CPU load or other system factors.
'''
