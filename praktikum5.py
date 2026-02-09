def Aufgabe1():
    numbers = "12345"
    res = 0
    for i in numbers:
        res += int(i)
    print(res)


def Aufgabe2():
    numbers = "1 2 3 4 5"[::-1]
    res = []
    for i in numbers.split():
        res.append(int(i))
    print(res)

def Aufgabe3():
    numbers = [-1, 8, 2, 0, -3, -9, -1, 10, 7, -4]
    chet = 0
    nechet = 0
    for i in numbers:
        if i % 2 == 0:
            chet += i
        else:
            nechet += i
    print(chet, nechet)

def Aufgabe4():
    numbers =  [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
    max_numer = 0
    for i in numbers:
        if i > max_numer:
            max_numer = i
    print(max_numer, numbers.index(max_numer))


def Aufgabe5():
    numbers = [1,2,3,4,5]
    for i in range(0,len(numbers)-1,2):
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
    print(numbers)

def Aufgabe6():
    text = "apple 42 banana 3 100 orange"
    spisik = []
    for i in text.split():
        if i.isdigit():
            spisik.append(int(i))
        else:
            spisik.append(i.title())
    print(spisik)

def Aufgabe7():
    text =  "aaaabbcchu"
    new_text = ""
    count = 0
    x = text[0]
    for i in text:
        if x == i:
            count += 1
        else:
            new_text += x + str(count)
            count = 1
            x = i
    new_text += x + str(count)
    print(new_text)

def Aufgabe8():
    emeil = "user@example.com"
    res = emeil[0].isalpha() and  "@" in emeil  and (emeil.endswith(".com") or emeil.endswith(".de"))
    print(res)

def Aufgabe9():
    text = "My number is 123-456-789 "
    result = ""
    for char in text:
        if char.isdigit():
            result += "*"
        else:
            result += char
    print("Результат:", result)

def Aufgabe10():
    text = "Python is fun".split()
    new_text = []

    for item in text:
        new_text.append(item[::-1])

    result = " ".join(new_text)
    print(result)


def Aufgabe11():
    text = "Python 3.12 is awesome!"
    letters = 0
    digits = 0
    spaces = 0
    other = 0
    for i in text:
        if i.isdigit():
            digits += 1
        elif i.isalpha():
            letters += 1
        elif i.isspace():
            spaces += 1
        else:
            other += 1
    print(letters, digits, spaces, other)


def Aufgabe12():
    text = " Hello, World! How  are you? "
    new_text = text.split()
    print(" ".join(new_text))


def Aufgabe13():
    text =  "Banana bAnana baNAna ".lower()
    for i in range(len(text)):
        pos = text.find("ban", i)
        if pos == i:
            print(pos)



Aufgabe13()