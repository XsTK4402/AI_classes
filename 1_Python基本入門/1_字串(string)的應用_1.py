print("哈囉 \n我是小白")
# \n 為字串換行用途

print("哈囉\"我是小白")
# \後加任何符號，表示該符號為字串內容，而非該字串之引號

phrase = "Hello Mr.White"
print(phrase.lower())
# .lower() 函式用途為將字串轉換為"小寫"並且回傳

print(phrase.upper())
# .upper() 函式用途為將字串轉換為"大寫"並且回傳

print(phrase.isupper())
# .isupper() 函式用途為判定字串是否全為大寫，若是則回傳true，否則回傳False

print(phrase.islower())
# .isupper() 函式用途為判定字串是否全為小寫，若是則回傳true，否則回傳False

print(phrase.lower().islower())
# 函式的疊加，此串為先用.lower()將字串轉會為小寫，再用.islower()判斷是否全為小寫，則結果為True
