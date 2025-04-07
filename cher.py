class Megalith:
    def __init__(self, data):
        self.data = data
    
    def middle(self):
        return self.data[len(self.data) // 2]

    def lowest(self):
        return min(self.data)

    def highest(self):
        return max(self.data)
    
    def median(self):
        a = sorted(self.data)
        return a[len(a) // 2]




data = [1, 2, 3, 5, 1, 7, 9]
ml = Megalith(data)
print(ml.middle())
print(ml.lowest())
print(ml.highest())
print(ml.median())