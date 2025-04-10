class Student:
    def __init__(self, fname, lname, id, energy_level = 100):
        self.name = fname
        self.last = lname
        self.id = id
        self.energy = energy_level

student1 = Student('Jon', 'Liu', '02409093', 70)
print(student1.name)