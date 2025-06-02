# simple inheritance example
# base class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # derived class
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks.")



# animal=Animal("general animal")
# animal.speak()  # Output: "general animal makes a sound."
# dog = Dog("Buddy")
# dog.speak()  # Output: "Buddy barks."

#============================================================
#super() example
class Animal:
    def __init__(self):
        self.name = "buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()  # Call the constructor of the base class
        self.breed = breed

    def speak(self):
        # Call the speak method of the base class
        super().speak()
        print(f"{self.name} barks. Breed: {self.breed}")

# animal = Animal("general animal")
# animal.speak()  # Output: "general animal makes a sound."
dog = Dog("Golden Retriever")
dog.speak()  # Output: "Buddy barks. Breed: Golden Retriever"