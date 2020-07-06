#print("Hello World")

#a = 10; b = 20; ab = a + b;
#print(ab)
"""
a = 25
b = 50
h = 4
area = (a + b) * 4 / 2
print(area)

from random import randint
score = randint(40, 100)

if score  > 90:
    message = "great"
elif score > 80:
    message = "good"
elif score > 60:
    message = "ok"
else:
    message = "bad"


info = "スコア{},評価{}"
text = info.format(score, message)
print(text)

i = 0
while i < 10:
    print(str(i) + "回目：ヨシ！")
    i += 1
else:
    print("どうして...")


for i in range(10):
    from random import randint
    import math

    n = input("x=")

    try :
        lg = math.log10(int(n))
        print(str(i) + "回目")
        print("y = log10(x):" + "x=" + str(n),"y=" + str(lg))
    except ValueError:
        print("設定値：" + str(n))
        print("対数関数のxは0を取れません")
        break

numbers = [2, 4, -55, 22, 9, -10]

sum = 0
for num in numbers:
    if num > 0:
        sum += num

print(sum)

namesf = ["鈴木", "田中", "木村", "西園寺"]
namess = ["一郎", "正造", "拓哉", "公望"]

fullname = []

for n1, n2, in zip(namesf, namess) :
    fullname.append(n1 + n2)
print(fullname)

import math
nums = [2, 3, 4, 5, 6]
nums_double = [math.log10(num) for num in nums]
print(nums_double)

nums = [2, 3, 4, "", 5, 6, "あああ"]
numbers = [num for num in nums if isinstance(num, (int, float))]
print(numbers)

data = [[1, 2], [3, 4], [5, 6], [7, 8]]
result = [num * 2 for alist in data for num in alist]
print(result)

"""

data = [[1, 2], [3, 4], [5, 6], [7, 8]]
result = []
for alist in data :
    temp = []
    for num in alist :
        temp.append(num * 2)
    else :
        result.append(temp)
print(result)
