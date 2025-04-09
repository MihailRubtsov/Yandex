class Human:
    def __init__(self, naaame):
        self.name = naaame
    
    def get_name(self):
        return self.name


class Student(Human):
    def __init__(self, name, uni):
        super().__init__(name)
        self.university = uni
        self.kur = 1
    
    def get_university(self):
        return self.university
    
    def get_year(self):
        return self.kur
    
    def study(self):
        if self.kur < 6:
            self.kur += 1


class Employee(Human):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
        self.spis = ['junior', 'middle', 'senior', 'lead']
        self.pos = 0
    
    def get_company(self):
        return self.company
    
    def work(self):
        if self.pos < 3:
            self.pos += 1
    
    def get_position(self):
        return self.spis[self.pos]