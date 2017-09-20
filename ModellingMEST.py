#MEST is a school that contains EITs and Fellows.
# Create classes to represent all three entities.
# - EITs have name, nationality, and the ability to recite fun facts about tech class 
# - Fellow has name, nationality, happiness_level and abilities to eat (increases happiness) and teach (decreases happiness)

class EIT:
    #EIT properties - name, nationality, fun_fact
    #EIT behaviours - recite fun facts
    def __init__(self, name, nationality, fun_fact):
        self.name = name
        self.nationality = nationality
        self.fun_fact = fun_fact

    def recite(self):
        print("My fun fact is {}")

class Fellow:
    #Fellow properties - name, nationality, happiness_level
    #Fellow behaviours - eat(increases happiness) and teach(decreases happiness)
    def __init__(self, name, nationality, happiness_level):
        self.name = name
        self.nationality = nationality
        self.happiness_level = happiness_level


class School:

    #MEST properties - EITS, fellows
    def __init__(self, mesters=[]):
        self.mesters = mesters

    #add method to add a mester