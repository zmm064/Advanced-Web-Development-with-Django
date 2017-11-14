class Parent1:
    def speak(self):
        print("I am Parent1")
    def talk(self):
        print("Parent1 talking")

class Parent2:
    def speak(self):
        print("I am Parent2")


class Child(Parent2, Parent1):
    pass

child = Child()

child.speak()
child.talk()
