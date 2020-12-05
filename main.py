import sys
print("Hello world!")

print(1 + 2)
print(3 - 1)
print(3 ** 5)
print("size of 2^64", sys.getsizeof(2 ** 64), "bytes")
print('span' + 'eggs')
print(10 / 2)
print(10 // 2)
print(15 % 4)

CONSTANT_PI = 3.1415
print('constant pi:', CONSTANT_PI)


l_from_list = list()
print(l_from_list)
l = []
print(l)
print(l_from_list == l)

l1 = [1, 2, 3]
l2 = l1
l2 = [4, 5, 6]
print('l1', l1, 'l2', l2)
print('last elem l2:', l2[-1])
print('last elem l2:', l2[len(l2) - 1])
array = [1, 2, 3, 4, 5, 6, 7]
print("array[1:3]", array[1:3])
print("array[1:3]", array[0:3])
print("array[:]", array[:])

array_copy = array[:]
array_copy.append(8)
array_copy_list = list(array_copy)
array_copy_list.append(9)
print(array, array_copy, array_copy_list)
print(list('abcdef'))

num = 5

if (num % 2 == 0):
    print("4 is even")
else:
    print('num is odd')

res = 2 - 3

if res > 0:
    print('greated than zero')
elif res < 0:
    print("smaller then zero")
else:
    print("is zero")

for i in "abcdef":
    print(i)

line = "spam eggs foo bar baz"
print("words in line:", line.split())
print("separate:")
for word in line.split():
    print(word)

print("empty list:", bool([]))
print("not empty list:", bool([0]))

array_of_words = line.split()

while array_of_words:
    word = array_of_words.pop()
    print('removed', word)
    print('remains', array_of_words)

d= {
    1: 'a',
    2: 'B',
    3: "C",
}
d2 = d
d[4] = "D"
print(d)
print(d[1])
print(d[2])
print(d2[4])
d2['foo'] = 'bar'
print(d2)
print('pop foo', d2.pop('foo'))
print(d2)

for k in d:
    print(k, '=', d[k])

for k, v in d.items():
    print  (k, '=', v)

s = {1, 2, 3, 3, 3}
print(s)

for i in s:
    print(i)

# t = tuple()
t = (1, 2, 3)
print(t)
dct = {
    (1, 2, 3): [4, 5, 6],
    (7, 8, 9): [0],
}

print(dct)
print(dct[(7, 8, 9)])

country_codes = {'RU', "US", "FR"}
print("ES?", "ES" in country_codes)
print("RU?", "RU" in country_codes)

country_codes_main = {'RU', "US", "FR"}
country_codes_secondary = {'ES', "GE", "RU"}
print(country_codes_main.difference(country_codes_secondary))

for i in [2, 11, 13, 4, 6, 7, 8, 9]:
    if i > 10:
        continue
    print(i)
    if i % 2 != 0:
        break

for i in [1, 4, 6]:
    if i % 2 != 0:
        break
    print(i)
else:
    print('did not break')