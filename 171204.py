# -*- coding:utf-8 -*-
def unique_in_order(iterable):
    l = []
    for i in iterable:
        if len(l) == 0 or i != l[-1]:
            l.append(i)
    return l


# Integers: Recreation One
def find_ans(n):
    sum = 0
    for i in range(1, n/2+1):
        if n%i == 0:
            sum += i * i
    sum += n*n
    if int(sum**0.5) == sum ** 0.5:
        return 1, [n, sum]
    else:
        return 0,

def list_squared(m, n):
    res = []
    for i in range(m, n):
        t = find_ans(i)
        if t[0]:
            res.append(t[1])
    return res

# String incrementer
def increment_string(s):
    if s and s[-1].isdigit():
        num = s[len(s.rstrip("0123456789")):]
        return s[:-len(num)] + str(int(num) + 1).zfill(len(num))

    return s + "1"

# str.zfill(width)  width -- 指定字符串的长度。原字符串右对齐，前面填充0。
"""
str = "     this is string example....wow!!!     ";
print str.rstrip();
str = "88888888this is string example....wow!!!8888888";
print str.rstrip('8')

     this is string example....wow!!!
88888888this is string example....wow!!!
"""

# str.rstrip([chars])
# rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.



print(unique_in_order('AAAABBBCCDAABBB'))
print(list_squared(250,500))
print(increment_string("fr00"))