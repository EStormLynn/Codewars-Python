# -*- coding:utf-8 -*-
#  Perimeter of squares in a rectangle
def fib(n):
    a, b = 0, 1

    for i in range(n + 1):
        if i == 0:
            yield b
        else:
            a, b = b, a + b
            yield b


def perimeter(n):
    return sum(fib(n)) * 4


# Counting Change Combinations
def count_change(money, coins):
    table = [0 for k in range(money + 1)]
    table[0] = 1

    for i in range(0, len(coins)):
        for j in range(coins[i], money + 1):
            table[j] += table[j - coins[i]]

    return table[money]


# A Chain adding function
def add(m):
    class AddNum(int):
        def __call__(self, x):
            return AddNum(self.numerator + x)
    return AddNum(m)

# Python中，如果在创建class的时候写了call（）方法， 那么该class实例化出实例后， 实例名()就是调用call（）方法。


# IP Validation
def is_valid_IP(strng):
    l = strng.split('.')
    if len(l) != 4:
        return False
    for i in l:
        if not i.isdigit() or int(i) > 255 or int(i) < 0 or i != str(int(i)):
            return False
    return True

def format_duration(seconds):
    if seconds == 0: return "now"
    origin = seconds
    dic = {
        'year': 60 * 60 * 24 * 365,
        'day': 60 * 60 * 24,
        'hour': 60 * 60,
        'minute': 60,
        'second': 1
    }
    spent = {}
    ans = ""
    for x in ['year','day','hour','minute','second']:
        spent[x] = seconds // dic[x]
        ans += "{}{} {}{}".format('' if seconds == origin else ' and ' if seconds % dic[x] == 0 else ', ',spent[x],x,'s' if spent[x] > 1 else '') if spent[x] > 0 else ''
        seconds %= dic[x]
    return  ans


    #your code here

print(add(1)(2)(4)(5))
print(count_change(4, [1,2]))
print(is_valid_IP('12.255.56.1'))
print(format_duration(3662))
