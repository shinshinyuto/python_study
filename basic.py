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

metro = {
 "G":"銀座線",
 "M":"丸ノ内線",
 "H":"日比谷線",
 "T":"東西線",
 "C":"千代田線",
 "H":"半蔵門線",
 "N":"南北線",
 "F":"副都心線"
}

print(metro)

data = dict([("one",1), ("two",2),("three",3)])
print(data)

datas = dict(yellow = 3, blue = 7, green = 5)
print(datas)

stock = dict.fromkeys(["s","m","l"],0)
print(stock)

newdata = dict([("one",10), ("two",20),("three",30)])
data.update(newdata)
print(data)

del data["one"]
print(data)
data.clear()
print(data)

cities = dict(kagoshima = 49, hakata = 29, hiroshima = 55, osaka = 83)
city = input("都市を入力:")

try :
    value = cities[city]
    print(f"{city}の値は{value}です")
except KeyError :
    print(f"{city}のデータはありません")
    city_key = list(cities.keys())
    city_value = list(cities.values())
    print(city_key)
    print(city_value)
except Exeption as error :
    print(error)

city_sum = sum(cities.values())
print(city_sum)

fruit = {"apple":3, "banana":8, "orange":5, "peach": 9}

while fruit :
    key = input("取り出すフルーツを選んでね：")
    if key == "" :
        continue
    elif key == "exit" :
        print("取り出し終了")
        break
    try :
        value = fruit.pop(key)
        print(f"{key}は{value}個です")
        print(fruit)
    except KeyError :
        print(f"{key}はありません")
    except Exeption as erroe :
        print(error)
        break
else :
    print("空になりました")

fruit = {"apple":3, "banana":8, "orange":5, "peach": 9}

while fruit :
    ans = input("フルーツを取り出しますか？(y/n)：")
    if ans == "y" :
        key, value = fruit.popitem()
        print(f"{key}は{value}個")
        print(fruit)
    elif ans == "n" :
        print("終了しました")
        break
else :
    print("もう空っぽです")

from random import randint
def dice() :
    num = randint(1, 6)
    return num

for i in range(5) :
    dice1 = dice()
    dice2 = dice()
    sum = dice1 + dice2
    print(f"{dice1}と{dice2}で合計{sum}")

def mile_meter(mile) :
    meter = mile * 1609.344
    return meter

distance = mile_meter(20)
print(str(distance) + "m")

from random import randint

def dice() :
    num = randint(1, 6)
    return num

def something() :
    pass

def dicegame() :
    dice1 = dice()
    dice2 = dice()
    sum = dice1 + dice2
    if sum % 2 == 0 :
        print(f"{dice1}と{dice2}で合計{sum}：偶数")
    else :
        print(f"{dice1}と{dice2}で合計{sum}：奇数")

for i in range(5) :
    dicegame()

print("ゲーム終了")
def calc(num) :
    unit_price = 180
    try :
        num = float(num)
        return num * unit_price
    except :
        return None

while True :
    num = input("個数を選んでください：")
    if num == "" :
        continue
    elif num == "exit" :
        break

    result = calc(num)
    print(result)

v = 2
def calc() :
    v_local = 10 * v
    ans = 3 * v_local
    print(ans)

calc()

def price(adult, child) :
    return (adult * 1200)+(child * 500)

a = price(1, 2)
print(a)

def calc(size, num = 4) :
    unit_price = {"s": 120, "m": 150, "l": 180}
    price = unit_price[size] * num
    return (size, num, price)

a = calc("m", 5)
b = calc("l")

print(a, b)

def route(start, end, *args) :
    route_list = [start]
    route_list += list(args)
    route_list += [end]

    route_str = "→".join(route_list)
    print(route_str)

start = "東京"
end = "鹿児島"
route(start, end, "香川", "広島", "福岡")

"""

import exchange

yen = 250000
rate = 114.22
charge = 1.0
dollar = exchange.yen2dollar(yen, rate, charge)
print(f"{yen}円：{dollar :,.2f}ドル")
