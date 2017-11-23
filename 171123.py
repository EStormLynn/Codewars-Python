def sort_array(source_array):
    pos = []
    odd = []
    for i in range (0,len(source_array)):
        if(source_array[i] % 2 == 1):
            odd.append(source_array[i])
            pos.append(i)

    odd.sort()

    for i in range (0,len(odd)):
        source_array[pos[i]]=odd[i]

    return source_array


def reverseWords(str):
    strlist = str.split(' ')
    strlist.reverse()

    ans=""
    for s in strlist:
        ans += s + ' '

    return ans[0:-1]


def unique_in_order(iterable):
    ans=[]
    if(len(iterable)==0):
        return ans
    ans.append(iterable[0])
    for i in range(1,len(iterable)):
        if(iterable[i] != iterable[i-1]):
            ans.append(iterable[i])

    return ans


def divisors(integer):
    res=[]
    for i in range(2,integer):
        if(integer % i == 0):
            res.append(i)

    if(len(res)==0):
        return str(integer) +" is prime"
    else:
        return res


def solution(s):
    res=[]
    for i in range(0,int(len(s) / 2)):
        res.append(s[2 * i] + s[2 * i + 1])
    if(len(s) % 2 != 0):
        res.append(s[-1] + '_')
    return res


print (sort_array([5, 3, 2, 8, 1, 4]))
print (unique_in_order(''))
print (divisors(15))
print (solution("fdfdfdf"))
