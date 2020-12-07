
from time import time
def secondary():
    print("sec")

def add(a, b):
    # return a + b
    print("Add", a, b)
    res = a + b
    print("Result:", res)
    return res

def div(a, b):
    if b == 0:
        return
    return a / b

def rain_today():
    res = ...
    if res.status_code == "OK":
        return res.dat.will_rain # True/False
    # print("status not ok")
    return None

def demo_lines():
    multiline = """ Zero line
    First line
    Seconde line
    123456
    """
    one_line = "line1\nline2"

    print(multiline)
    print(one_line)

def greet(name="Dudes"):
    print("Hello,", name)

def multiply_lines(input_line, times, lines=None):
    if lines is None:
        lines = {}
        print("id of dict", id(lines))
    for i in range(1, times + 1):
        lines[i] = input_line * i
    return lines

# def counter(a):
#     return a

def power(a, pow=5):
    return a ** pow

def count_values(counter, *args, as_list=False):
    print(counter)
    print(args)
    if as_list:
        # l = []
        # for v in args:
        #     l.append(counter(v))
        # return l
        return[counter(v) for v in args]

    # d = {}
    # for v in args:
    #     d[v] = counter(v)
    # return d
    return {v: counter(v) for v in args}

def my_range(start, end=None, step = 1):
    if end is None:
        end = start
        start = 0

    print('entering cycle')
    while start < end:
        print('yielding', start)
        yield  start
        # v = v + step
        start += step
        print('increased v to', start)

def main():
    print("HELLO MY DUDES")
    # secondary()
    # add(5, 3)
    # div_res = div(10, 2)
    # print("div_res 2:", div_res)
    # div_res = div(10, 0)
    # print("div_res 0:", div_res)
    greet("John")
    greet()
    lines = multiply_lines("foo", 5)
    print(lines)
    print(multiply_lines("spam", 4, lines))
    print(multiply_lines("spam and eggs", 2))

    res = count_values(power, 1, 2, 3, 4, 5, 6)
    print(res)
    res = count_values(power, 1, 2, 3, 4, 5, 6, 7, 8, 9, as_list=True)
    print(res)

    r = range(10)
    print(r)
    print(list(r))
    print(tuple(r))
    for i in r:
        print(i, end=" ")
    print()
    s = {v for v in r}
    print(s)
    t = (power(v, 3) for v in r)
    print(t)
    print('first', next(t))
    print('second', next(t))
    for i in t:
        print(i)

    range_q = my_range(10)
    print(range_q)
    print("next val:", next(range_q))
    print("first next done")
    print('doing next again')
    print("next val:", next(range_q))
    print('doing next again 2')
    print("next val:", next(range_q))
    print(list(range_q))

def time_func(func, *args):
    start_time = time()
    print("time befor", start_time)
    res = func(*args)
    end_time = time()
    print("time after", end_time)
    print('computed in', end_time - start_time)
    print("result", res)
    return res

def demo_decor():
    time_func(power, 1000, 1000)
# main()

# demo_decor()


values = list(range(10))
print("values", values)
powered_gen = map(power, values)
print("powered_gen", powered_gen)
print("res", list(powered_gen))

only_even = filter(lambda  v: v % 2 == 0, values)
print("only_even_gen", only_even)
print("only_even", list(only_even))