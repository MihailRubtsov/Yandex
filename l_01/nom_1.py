import sys
class Snow:
    def fall(self):
        print("*", end='')


class Fallout:
    def snow(self):
        print("*", end='')
    
    def rain(self):
        print("o", end='')

for i in range(5):
    print(5)

class Controller:
    def __init__(self):
        self.channel = 1
        self.nom = 0

    def click(self):
        if self.channel == 5:
            self.channel = 1
        else:
            self.channel += 1

class Rainbow:
    def __init__(self, typik = 1):
        self.typik = typik
        self.arr = ["red", "orange", "yellow", "green", "light blue", "blue", "violet"]
    
    def next_color(self, col):
        if self.typik == 1 or self.typik == 3:
            if self.arr.index(col) == 6:
                return self.arr[0]
            else:
                return self.arr[self.arr.index(col) + 1]
        else:
            if self.arr.index(col) == 0:
                return self.arr[6]
            else:
                return self.arr[self.arr.index(col) - 1]



class Cabbage:
    def __init__(self, ver, shag, kor):
        self.ver = ver
        self.shag = shag
        self.kor = kor
    
    def leaf(self):
        if self.ver - self.shag < self.kor:
            print(self.kor)
        else:
            self.ver -= self.shag
            print(self.ver)



def main():
    rb = Rainbow()
    print(rb.next_color('green'))


    return 0






if __name__ == "__main__":
    main()