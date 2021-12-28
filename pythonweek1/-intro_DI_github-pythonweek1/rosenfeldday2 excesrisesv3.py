1

import math

numbers = input("Provide D: ")
numbers = numbers.split(',')
print((numbers))
result_list = []
for D in numbers:
    C = 50
    H = 30
    Q = round(math.sqrt(2 * C * int(D) / H))
    result_list.append(Q)

print(result_list)

2

var1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
var2 =[44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
var3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
var4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

var5 = var1 + var2 + var3 + var4
var5.sort(reverse=True)
print(var5)

print(sum(var5))

print(var5[0:1:])
print(var5[-2:-1:])

var6= []
for n in var5:
    if n >= 50:
        var6.append(n)
print(var6)

var7 =[]
for t in var5:
    if t <= 10:
        var7.append(t)
print(var7)

var8= []
for z in var5:
    squared = z*z
    var8.append(squared)
print(var8)

var9 = []
for g in var5:
    if g not in var9:
        var9.append(g)
print(var9)
print(len(var9))

avg1 = sum(var5)//len(var5)
print(avg1)

var5.sort()
print(var5[-1])
print(var5[0])


var10 = [int(x) for x in input("Please enter a number: ").split(",")]

print(var10)
user_input1 = input("Please enter a number: ").split(",")
var11 = []
for x in user_input1:
    if not x in user_input1:
        var11.append(x)

print(var11)


text1 = "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged"

print(len(text1))
print("There are {} sentances in this text".format(len(text1.split("."))))
print("There are {} words in this text".format(len(text1.split(" "))))

avg2 = (len(text1.split(" "))) // (len(text1.split(".")))
print("The average amount of words per sentance is {}".format(avg2))

text2 = text1.split()
set1 = set(text2)
print(f"The amount of unique words in this text is {len(set1)}")

non_unique = len(text1.split(" ")) - len(set1)
print(f"The amount of non-unique words in this sentance are {non_unique}")

spaces_in_text = []
for w in text1:
    if w == " ":
        spaces_in_text.append(w)
print(len(spaces_in_text))



spaces = []
count = 0
for words in range(0,len(text1)):
    if text1[words] == " ":
        count += 1
        spaces.append(words)
    break

    print(len(spaces))


string8 = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

word_dict = {}

for words in string8:
    word_dict[words] = word_dict.get(words,0) + 1

for words2 in sorted(word_dict):
    print("{} : {}".format(words2,word_dict[words2]))

print(word_dict)











