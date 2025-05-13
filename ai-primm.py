

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

    def analyze():
        print('The AI is analyzing the data')

class Robot(Human):
    def __init__(self, name, age, occupation, task):
        self.task = task
        super().__init__(name, age, occupation)
    
    def perform_task(self):
        print(f'{self.name} is now completing the {self.task} task.')

my_ai = AI("Athena", 5, "Virtual Assistant", 9.8)
print(my_ai.name)
print(my_ai.age)
print(my_ai.occupation)
print(my_ai.intelligence_level)
my_ai.think()
my_ai.communicate()
my_ai.learn()
ai1 = AI('Jerome', 2, 'Virtual Youtuber', .8)
rob1 = Robot('Lesly', 2, 'Windshield placer for The Rouge', 'place windshield')
print(rob1.name)
print(rob1.age)
print(rob1.occupation)
rob1.perform_task()
