def uglify(text):
    count = 1
    result = ''
    for i in text:
        if text.index(i) % 2 == 0:
            result += i.upper()
            count += 1
        else:
            result += i.lower()
            count += 1
        print(text.index(i), end=", ")
    return result

print(uglify("Привет мир"))