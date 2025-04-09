class Robot:
    def __init__(self, pop):
        self.x = pop[0]
        self.y = pop[1]
        self.spis = [(self.x, self.y)]
    
    def move(self, com):
        self.spis = [(self.x, self.y)]
        for i in com:
            if i == "N":
                self.y += 1
            elif i == "S":
                self.y -= 1
            elif i == "E":
                self.x += 1
            elif i == "W":
                self.x -= 1
            


            self.spis.append((self.x, self.y))
        return self.spis[-1]
    
    def path(self):
        return self.spis



# class SnowFlakes:
#     def __init__(self, razm):
#         self.razm = razm
#         self.snej = []
#         for i in range()

