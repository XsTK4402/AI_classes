a = "A B C D E"
print(a,type(a)) #A B C D E <class 'str'>

b = a.split()
print(b,type(b)) #['A', 'B', 'C', 'D', 'E'] <class 'list'>

c = "--".join(b)
print(c,type(c)) #A--B--C--D--E <class 'str'>

d = c.split()
print(d,type(d)) #['A--B--C--D--E'] <class 'list'>

e = "".join(d)
print(e,type(e)) #A--B--C--D--E <class 'str'>




a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
a_set = set(a)
b_set = set(b)

result_set1 = a_set & b_set  #(交集) [3, 4, 5]
result_set2 = a_set | b_set  #(聯集) [1, 2, 3, 4, 5, 6, 7]
result_set3 = a_set ^ b_set  #(反交集) [1, 2, 6, 7]

result1 = list(result_set1)
result2 = list(result_set2)
result3 = list(result_set3)

print(result1)
print(result2)
print(result3)