phrase = "Hello Mr.White"
print(phrase[0])
print(phrase[0:5])
print(phrase[6:])
# []的應用，指的是字串中的第?個字符，0為第一位、1為第二位、2為第三位以此類推

print(phrase.index("H"))
# .index("") 函式用途為判定字串的對應順序數值，以上範例"H"就為"Hello Mr.White"中的第0位，若字串有重複字符，則回傳第一位的順序數值。

print(phrase.replace("l", "L"))
# .replace("","") 函式用途為取代字串中的內容。前者為取代前原字符，後者為取代者。
