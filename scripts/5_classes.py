class animal():
    def __init__(self,animal_type,sound):
        self.type = animal_type
        self.sound = sound

    def speak(self):
        print(f"{self.type} makes {self.sound} sound")

class dog(animal): 
    def __init__(self,name,color):
        super().__init__('dog','bark')
        self.name = name
        self.color = color

    def describe(self):
        print(f"this is a {self.color} dog named {self.name}")
   
class cat(animal):
    def __init__(self,name,color):
        super().__init__('cat','meow')
        self.name = name
        self.color = color

    def describe(self):
        print(f"this is a {self.color} cat named {self.name}. It likes milk")

dog1 = dog("Luna", "brown")   
dog1.speak()
dog1.describe()
dog2= dog("Max", "black")
dog2.describe()
cat1 = cat("Milo", "white")
cat1.speak()
cat1.describe()