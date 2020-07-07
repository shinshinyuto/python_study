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

names = ["鈴木一郎", "田中正造", "木村拓哉", "西園寺公望", "阿良々木里美"]
name = "里美"
result = False


for item in names :
        if name in item :
            result = True
            break
print(result)

id_list = ["abc74", "uis22", "iii54", "pjs20"]
while True :
    id = input("idを入力してください(exitで中止)")
    if id == "exit" :
        print("検索終了")
        break
    try :
        pos = id_list.index(id)
        print(str(pos + 1) + "番目のメンバーです")
    except :
        print("該当なし")

result = [1,2,1,2,1,2,1,2,2,2,1,2,1,]
half = len(result) / 2
point = result.count(1)

if point >= half :
    print("合格")
else :
    print("不合格")

import random
datas = [2, 4, -55, 22, 9, -10]
data = random.choice(datas)
data_sum = sum(datas)
data_max = max(datas)
data_min = min(datas)

info = ["チョイス : " + str(data),"合計 : " + str(data_sum),"最大値 : " + str(data_max),"最小値 : " + str(data_min)]
print(info)

data = (
  11, 12, 13,
  20, 27,
  34, 35, 36
)

print(data)

data = tuple(range(-5, 6))
print(data)

week = tuple("日月火水木金土")
print(week)

color = ["red","blue","yellow","green"]
colors = tuple(color)
print(colors)

pre3 = week[4]
print(pre3)

(a,b) = (100,200)
print(a)
print(b)

data = (12,15)
(boy, girl) = data
all = boy + girl
print(boy, girl, all)

clears = (4, 8, 19, 21, 38)
num = int(input("受験番号を入れてください："))
if num in clears :
    print("合格です")
else :
    print("不合格です")

namesf = ["鈴木", "田中", "木村", "西園寺"]
namess = ["一郎", "正造", "拓哉", "公望"]
fullname = []
for n1, n2 in zip(namesf, namess) :
    fullname.append(n1 + n2)
print(fullname)
"""

color_set1 = {"red","blue","yellow","green"}
color_set2 = {"black","green","white","blue"}

colors = color_set1 | color_set2
colorlist = set.union(color_set1, color_set2)
print(colors)
print(colorlist)

colorcommon = color_set1 & color_set2
colorsame = color_set1.intersection(color_set2)
print(colorcommon)
print(colorsame)

colordiff = color_set1 - color_set2
colorminus = color_set1.difference(color_set2)
print(colordiff)
print(colorminus)

colorsymmetric = color_set1 ^ color_set2
colorside = color_set1.symmetric_difference(color_set2)
print(colorsymmetric)
print(colorside)
