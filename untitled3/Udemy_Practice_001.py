__author__ = 'Executor'

class Animal:
    def talk(self):
        print("I have something to say")

    def walk(self): print('Hey waling here')

    def clothes(self): print("nakie")

class Duck(Animal):
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print('Quack!')

    def walk(self):
        print('She walks like a lady')

    def set_variables(self, k, v):
        self.variables[k] = v

    def get_variables(self, k):
        return self.variables.get(k, None)

class Dog(Animal):
    def clothes(self):
        print("balck and waitht")
    pass

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()
    dawg = Dog()
    dawg.clothes()
    dawg.talk()
    dawg.walk()

if __name__ == "__main__":
    main()