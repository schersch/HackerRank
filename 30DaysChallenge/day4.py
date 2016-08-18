#30 Days of Code Challenge
#Day 4: Class vs. Instance

class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            self.age = 0
            print('Age is not valid, setting age to 0.')
        else:
            self.age = initialAge
            
    def yearPasses(self):
        self.age = self.age + 1

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
