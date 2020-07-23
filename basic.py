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

import exchange

yen = 250000
rate = 114.22
charge = 1.0
dollar = exchange.yen2dollar(yen, rate, charge)
print(f"{yen}円：{dollar :,.2f}ドル")

num = (lambda w, h : w * h)(3, 4)
print(num)

price = lambda burger = 1, potato = 0 : burger*240 + potato*100
order = price(potato = 2)
print(order)

sizelist = ["xs", "s", "m", "l"]
data = ["s","xs","l","s","m","m","xs","l"]
data.sort(key = lambda item : sizelist.index(item))
print(data)

def double(x) :
    return x * 2

nums = [4, 3, 8, 7, 3]
nums2 = list(map(double, nums))
print(nums2)

nums = [4, -3, 8, -7, -3]
nums2 = list(filter(lambda x : x > 0, nums))

print(nums2)

def num_generator() :
    n = 0
    while True :
        num = n*n + 2*n + 3
        yield num
        n += 1

def do_something(num) :
    return (num%2, num%3)

gen = num_generator()
for i in range(1, 10) :
    num = next(gen)
    result = do_something(num)
    print(result)

def fizzbuzz() :
    n = 1
    while True:
        if n % 15 == 0 :
            yield "FizzBuzz"
        elif n % 3 == 0 :
            yield "Fizz"
        elif n % 5 == 0 :
            yield "Buzz"
        else :
            yield str(n)
        n = n + 1

game = fizzbuzz()
for i in range(1, 20) :
    print(next(game))

def word_quiz(word) :
    hint = ""
    for letter in word :
        hint += letter
        yield hint

ans = "Python"
quiz = word_quiz(ans)
while True :
    try :
        hint = next(quiz)
        print(hint)
        word = input("この単語は?：")
        if ans.lower() == word.lower() :
            point = len(ans) - len(hint)
            print(f"正解です！得点:{point}")
            break
        else :
            print("違います")
    except :
        print("終了です：0円")
        break

class Car :
    maker = "PEACE"
    count = 0
    @classmethod
    def countup(cls) :
        cls.count += 1
        print(f"出荷台数：{cls.count}")

    def __init__(self, color = "white") :
        Car.countup()
        self.mynumber = Car.count
        self.color = color
        self.mileage = 0

    def drive(self, km) :
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです。"
        print(msg)


car1 = Car()
car2 = Car()

print(car1.mileage)
print(car1.color)

car1.color = "green"
print(car1.color)

print(car1.drive(15))
print(car1.drive(45))
print(Car.maker)
print(Car.count)
print(car1.mynumber)

class Simple :
    pass

Simple.x = 100
print(Simple.x * 2)

def hello(msg = "ハロー") :
    print(msg)

Simple.greeting = hello
print(Simple.greeting("おはよう"))

obj1 = Simple()
obj2 = Simple()

def drum(beat = "とことこ") :
    print(beat)

def sax(phrase = "ぷーぷー") :
    print(phrase)

obj1.play = drum
obj2.play = sax

print(obj1.play())
print(obj2.play())
print(obj1.play("ドンドコ"))

class A :
    def hello(self) :
        print("ハロー")

class B(A) :
    def bye(self) :
        print("グッバイ")

obj = B()
print(obj.hello())
print(obj.bye())

from exchange import Datalog

#Datalogクラスを継承したMydataクラス
class Mydata(Datalog) :
    def printlog(self) :
        #スーパークラスのインスタンス変数の値を取る
        for date, data in self.loglist :
            print(date, data)

obj = Mydata()
obj.log("abc")
obj.log("123")
obj.log("あいう")
obj.printlog()

from exchange import Greet2

obj = Greet2()
obj.hello()
obj.hello("井上")

from exchange import Player

player1 = Player("青木", "16", "10", "MF")
print(player1.name)
print(player1.age)
print(player1.number)
print(player1.position)

class Person():
    def __init__(self, name) :
        self.__name = name

    def who(self) :
        print(self.__name + "です")

man = Person("宇佐美")
man.who()

man.__name #直接アクセスするとエラー

class Goods :
    def __init__(self, name, price) :

        self.__data = {"name": name, "price": price}

    @property
    def name(self) :
        return self.__data["name"]

    @name.setter
    def name(self, value) :
        self.__data["name"] = value

    @property
    def price(self) :
        price = self.__data["price"]
        price_str = f"{price:,}円"
        return price_str

shoes = Goods("dream", 6800)
print(shoes.name)
shoes.name = "Dream 9"
print(shoes.name)
print(shoes.price)
shoes.price = 9800 #エラー セッターが定義されていない

class Goods :
    def __init__(self, name, price) :
        self.__data = {"name": name, "price": price}

    def get_name(self) :
        return self.__data["name"]

    def set_name(self, value) :
        self.__data["name"] = value

    def get_price(self) :
        price = self.__data["price"]
        price_str = f"{price:,}円"
        return price_str

    name = property(get_name, set_name)
    price = property(get_price)

shoes = Goods("nike", 6800)

print(shoes.name)
print(shoes.price)

file = "./data/python.txt"
fileobj = open(file)
text = fileobj.read()
fileobj.close()
print(text)

price = [200, 300, 400, 500, 600]
count = [31, 29, 25, 28, 26]
plt.plot(price, count, marker = "o")
plt.title("count - price")
plt.xlabel("price")
plt.ylabel("count")
plt.grid(True)

import math
X = range(0, 360)
S = [math.sin(math.radians(d)) for d in X]
C = [math.cos(math.radians(d)) for d in X]

price1 = [200, 300, 400, 500, 600]
price2 = [24, 33, 40, 55, 69]
price3 = [17, 38, 99, 115, 170]
count1 = [27, 29, 25, 28, 26]
count2 = [38, 66, 88, 109, 126]
count3 = [111, 129, 130, 150, 176]

plt.plot(price1, count1, marker = "o", color = "blue", linestyle = "-", label = "p1")
plt.plot(price2, count2, marker = "v", color = "red", linestyle = "--", label = "p2")
plt.plot(price3, count3, marker = "d", color = "#000000", linestyle = ":", label = "p3")
plt.legend(loc = "upper left")
plt.show()

labels = ["A","B","C","E","D","F","G","H","I","J"]
x_pos = range(0, 10)
y_pos = range(0, 10)
v = [91, 45, 17, 88, 47, 87, 49, 56, 67, 77]
plt.barh(y_pos, v, tick_label = labels)
plt.show()

labels = ["Green","Red","Yellow","Blue","Black","White"]
x_pos = range(0, 6)
A = [34, 46, 45, 56, 37, 44]
B = [17, 47, 55, 67, 49, 29]

bar1 = plt.bar(x_pos, A, color = "g")
bar2 = plt.bar(x_pos, B, color = "c", bottom = A)
plt.xticks(x_pos, labels, rotation = "vertical")
plt.legend((bar1, bar2), ("man", "woman"), loc = "upper right")
plt.show()

X1 = [91, 45, 17, 88, 47, 87, 49, 56, 67, 77]
Y1 = [57, 52, 92, 58, 27, 48, 55, 30, 99, 63]
X2 = [38, 47, 30, 38, 20, 36, 54, 73, 82, 39]
Y2 = [20, 88, 73, 93, 47, 63, 42, 89, 40, 16]
plt.scatter(X1, Y1, marker = "+", color = "red")
plt.scatter(X2, Y2, marker = "^", color = "green")
plt.show()

X, Y = np.random.rand(100), np.random.rand(100)
V = np.random.rand(100)*1000 + 50
W = np.random.rand(100)
plt.scatter(X, Y, marker = "o", s = V,c = W, cmap = "hot", alpha = 0.5, linewidths = 1, edgecolors = "b")
plt.colorbar()
plt.grid(True)
plt.show()

import numpy as np
labels = ["E","D","C","B","A"]
V = [17, 25, 37, 68, 89]
ex = [0, 0, 0.1, 0, 0]
plt.pie(V, explode = ex, labels = labels, autopct = '%1.1f%%', startangle = 90)
plt.show()

import matplotlib.pyplot as plt
X1, Y1 = range(0, 7), [61, 45, 82, 47, 27, 83, 59]
X2, Y2 = range(0, 5), [29, 62, 46, 82, 37]
X3, Y3 = range(0, 4), [49, 30, 61, 43]
labels = ["A","B","C","D","E","F","G"]

fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax1.bar(X1, Y1, color = "b", tick_label = labels)
ax1.set_title("snake")

ax2 = fig.add_subplot(2,2,3)
ax2.bar(X2, Y2, color = "g", tick_label = labels[:5])
ax2.set_title("fish")

ax3 = fig.add_subplot(2,2,4)
ax3.bar(X3, Y3, color = "c", tick_label = labels[:4])
ax3.set_title("bird")

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
X1, Y1 = range(0, 5), [61, 45, 82, 47, 27]
X2, Y2 = range(0, 5), [29, 62, 46, 82, 37]

labels = ["A","B","C","D","E"]

fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
ax1.bar(X1, Y1, color = "b", tick_label = labels)
ax1.set_title("snake")

ymin, ymax = plt.ylim()

ax2 = fig.add_subplot(1,2,2)
ax2.bar(X2, Y2, color = "g", tick_label = labels[:5])
ax2.set_title("fish")

plt.ylim(ymin, ymax)

plt.show()

a = np.array([1, 2, 3])
print(a)

data = (1, 2, 3)
b = np.array(data)
print(b)

print(type(a))
print(type(b))
print(a.dtype)

c = np.array([2, 8, 4], dtype = float)
print(c)
c_str = np.array(c, dtype = "<U")
print(c_str)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

line1 = [10, 20, 30]
line2 = [40, 50, 60]
line3 = [70, 80, 90]

b = np.array([line1, line2, line3])
print(b)

data = [1, 2, 3, 4, 5, 6]
c = np.array(data).reshape(2, 3)
print(c)

d = np.array([[0, 1], [2, 3], [4, 5]])
d.ravel()
print(d)
d.flatten()
print(d)
print(d.shape)
print(d.ndim)
print(d.size)

a = np.array([0, 1, 2])
b = np.append(a, [3, 4, 5])
print(b)
c = np.array([1, 2, 3, 4, 5, 6]).reshape(2,3)
d = np.append(a, [7, 8, 9], axis = 0)
print(c)
print(d)

a = np.array([0, 1, 2])
b = np.insert(a, 1, [99, 88])
print(b)

words = np.array(["dog", "car", "bird"])
new_words = np.insert(words, 0, "snake")
cut_words = np.delete(words, len(words)-1)
print(new_words)
print(cut_words)

a = np.array([[0, 1], [2, 3], [4, 5]])
print(a)

print(np.transpose(a))
print(a.T)

b = np.array([1, 2, 3, 4, 5])
c = b[:, np.newaxis]
print(c)

print(b[3])
print(b[-1])
b[1] = 100
print(b)

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = np.array(data).reshape(3,3)

print(a)
print(a[0,0])
print(a[1,2])
print(a[2,1])

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(data[:])
print(data[:4])
print(data[4:])
print(data[3:7])
print(data[::2])
print(data[::-1])

"""

import numpy as np

data = [2.1, 3.5, 2.5, 4.3, 5.1, 1.6]
a = np.array(data).reshape(3,2)
print(a)

a1 = a[:2,].astype(int)
print(a1)
