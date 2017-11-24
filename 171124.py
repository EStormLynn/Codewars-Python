def openOrSenior(data):
    ans = []
    for item in data:
        a = min(item[0], item[1])
        b = max(item[0], item[1])

        if (b < 55 or a < 7):
            ans.append('Open')
        else:
            ans.append('Senior')

    return ans


def find_short(s):
    wordlist = s.split(' ')
    l = 1e9+7
    for word in wordlist:
        l = min(len(word), l)

    return l


def order(sentence):
    a = ['']*10
    ans = ''
    wordlist = sentence.split(' ')

    for item in wordlist:
        for i in range(1, 10):
            if(str(i) in item):
                a[i] = item
    for item in a:
        if(item != ''):
            ans+=item+' '
    return ans[0:-1]

MORSE_CODE=[]
def decodeMorse(morseCode):
    ans=""
    words = morseCode.split("   ")
    for word in words:
        c = word.split(' ')
        for ic in c:
            if(ic==''):
                continue
            ans+=MORSE_CODE[ic]
        ans+=' '

    return ans[0:-1]

    # ToDo: Accept dots, dashes and spaces, return human-readable message

def cmp(s1,s2):
    count1 = 0
    count2 = 0
    for c in s1:
        count1 += int(c)
    for c in s2:
        count2 += int(c)
    if count1!=count2:
        if count1 > count2:
            return 1
        else:
            return -1
    else:
        if s1 < s2:
            return -1
        else:
            return 1


def order_weight(strng):
    strings = strng.split(' ')
    strings.sort(cmp)

    ans=""
    for item in strings:
        ans += item + ' '
    return ans[0:-1]


print openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]])
print find_short("bitcoin take over the world maybe who knows perhaps")
print order("is2 Thi1s T4est 3a")
print order_weight("4 2 5 1 6")
print order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")

