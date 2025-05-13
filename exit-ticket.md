### P(redict)

Predict what the following code snippet will do:
```py
class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def think(self):
        print("The human is thinking deeply.")

    def communicate(self):
        print("The human is communicating clearly.")

class AI(Human):
    def __init__(self, name, age, occupation, intelligence_level):
        self.intelligence_level = intelligence_level
        super().__init__(name, age, occupation)

    def think(self):
        print("The A`perform_task()` online.")

    def communicate(self):
        print("The AI is communicating digitally with its human.")

    def learn(self):
        print("The AI is learning and improving its capabilities.")

my_ai = AI("Athena", 5, "Virtual Assistant", 9.8)
print(my_ai.name)
print(my_ai.age)
print(my_ai.occupation)
print(my_ai.intelligence_level)
my_ai.think()
my_ai.communicate()
my_ai.learn()
```
---

### I(nvestigate)

Answer these questions about the code snippet:

1. What is the relationship between the Human and AI classes?
   Human is the parent, and ai is the child.
   
2. How does the `__init__()` method in the AI class use the `super()` function?
   It uses super to steal name age and occupation from the human class.

3. How does the output of the `think()` and `communicate()` methods differ between the Human and AI instances?
    Think for human outputs: The human is thinking deeply. Whereas for ai states: The A`perform_task()` online.
   Same for human communicate: The human is communicating clearly. and ai communicate: The AI is communicating digitally with its human.

4. Which attributes will the AI class get/grab from the Human class?
   Name age and occupation

5. Which attribute belongs specifically to the AI class?
   intelligence_level

6. How many attributes **total** will an instance of the AI class have?
   4
---
