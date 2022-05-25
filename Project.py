class RepeatException(Exception):
    enter = False


key = []
string = ""
def fill (t, t1):
    global key
    global string
    enter_text = True
    enter = False
    while(not enter):
        print('Введите ключ')
        key = input().split()
        enter = check()
    if (enter_text):
        match t:
            case "1": 
                stringm = []
                print('Введите строку')
                string = input()
                for i in string:
                    stringm.append(i)
                enter_text = False
                return stringm
            case "2":
                stringm = []
                print('Введите строку')
                string = input()
                enter_text = False
                print('Введите Кол-во символов')
                item = int(input())
                if (t1 == 1):
                    for i in range (0, len(string), item):
                        stringm.append(string[i:i+item])
                else:
                    if (len(string)%item == 0):
                        for i in range (0, len(string), item):
                            stringm.append(string[i:i+item])
                    else:
                        stringm = block(string, key, item)
                print(stringm)
                return stringm
            case "3":
                stringm = []
                print('Введите строку')
                string = input()
                enter_text = False
                stringm = string.split()
                return stringm
                


def check ():
    k = [int(item) for item in key]
    for i in range (max(k) + 1):
        if (k.count(i) > 1 or k.count(i) < 1):
            print("Ключ не корректен")
            return False
    else:
        return True


def Encryption (s, k):
    if (len(s) % len(k) != 0):
        for i in range (len(k) - (len(s) % len(k))):
            s.append("\0")
    #print(s)
    str_new = [0]*len(s)
    p = 0
    for i in range (len(s)):
        str_new[int(k[i%len(k)]) + (p)] = s[i]
        if ((i+1)%len(k) == 0):
            p += len(k)
    return str_new

def reverse_key (k):
    rk = [0]*len(k)
    for i in range (len(k)):
        rk[int(k[i])] = i
    # print(rk)
    return rk

def full_str (s, k):
    p = True
    n = len(k) - (len(s)%len(k))
    new_str = ["0"]*(len(s)+n)
    for i in range (n):
        a = int(k[-i-1])+(len(k)*(len(s)//len(k)))
        new_str[int(k[-i-1])+(len(k)*(len(s)//len(k)))] = "\0"
    for item in s:
        p = True
        for i in range(len(new_str)):
            if (new_str[i] == "0" and p):
                new_str[i] = item
                p = False
    print(new_str)
    return new_str


def block (s, k, n):
    p = 0
    i2 = 0
    a = len(s) % n
    b = (len(s) // n)
    c = (((len(s) // n) + 1) // len(k))
    sm = ['']*(b+1)
    for i in range (0, len(s), n):
        if(p == (b - 1)):
            sm[p] = s[i2:i2+(len(s)%n)]
            i2-= n - 1
        else:
            sm[p] = s[i2:i2+n]
        p+=1
        i2+=n
    print(sm)
    return sm

def prt (str):
    print("".join(str))

def prt_word (str):
    print(" ".join(str))

print('Шифровать - 1')
print('Разшифровать - 2')
s = int(input())
match s:
    case 1:
        print('По буквам - 1')
        print('По группе букв - 2')
        print('По словам - 3')
        cs = input()
        match cs:
            case "1":
                strr = fill(cs, s)
                str2 = Encryption(strr, key)
                prt(str2)


            case "2":
                strr = fill(cs, s)
                str2 = Encryption(strr, key)
                prt(str2)
            case "3":
                strr = fill(cs, s)
                str2 = Encryption(strr, key)
                prt_word(str2)
    case 2:
        print('По буквам - 1')
        print('По группе букв - 2')
        print('По словам - 3')
        cs = input()
        match cs:
            case "1":
                strr = fill(cs, s)
                new_string = full_str(strr, key)
                rekey = reverse_key(key)
                str2 = Encryption(new_string, rekey)
                prt(str2)

            case "2":
                strr = fill(cs, s)
                new_string = full_str(strr, key)
                rekey = reverse_key(key)
                str2 = Encryption(new_string, rekey)
                prt(str2)

            case "3":
                strr = fill(cs, s)
                new_string = full_str(strr, key)
                rekey = reverse_key(key)
                str2 = Encryption(new_string, rekey)
                prt_word(str2)

