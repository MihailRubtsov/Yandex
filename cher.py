class Avalanche:
    def __init__(self):
        self.ona = ""
        
    def go(self):
        if self.ona == "":
            self.ona = "O"
            print(self.ona)
        else:
            rez = ''
            for i in self.ona:
                if i == "O":
                    rez += "ooOoo"
                else:
                    rez += "oOo"
            self.ona = rez
            print(self.ona)


ava = Avalanche()
ava.go()
ava.go()
ava.go()

