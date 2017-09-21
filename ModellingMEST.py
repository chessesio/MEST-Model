#MEST is a school that contains EITs and Fellows.
# Create classes to represent all three entities.
# - EITs have name, nationality, fun_fact and the ability to recite fun facts about tech class 
# - Fellow has name, nationality, happiness_level and abilities to eat (increases happiness) and teach (decreases happiness)
# - School has EITs and Fellows

class EIT:

    def __init__(self, name, nationality, fun_fact):
        self.name = name
        self.nationality = nationality
        self.fun_fact = fun_fact

    def recite(self, eit_name):
        print(self.fun_fact)


class Fellow:

    def __init__(self, name, nationality, happiness_level=5):
        self.name = name
        self.nationality = nationality
        self.happiness_level = happiness_level

    def eat(self, fellow):
        self.happiness_level += 1

    def teach(self, fellow):
        self.happiness_level -= 1


class School:

    def __init__(self,eits=[],fellows=[]):
        self.eits = eits
        self.fellows = fellows

    def add_eit(self, new_eit):
        self.eits.append(new_eit)

    def add_fellow(self, new_fellow):
        self.fellows.append(new_fellow)

    def loop(self):

        while True:
            mest = School()
            choice = input("Select:\n1 to add EIT.\n2 to add fellow.\n3 to eat(fellows only)\n4 to teach (fellows only)\n")

            if choice == "1":
                new_eit_ = EIT(name=input("Enter EIT's name:\n"),nationality=input("Enter nationality;\n"),fun_fact=input("Enter fun fact about tech"))
                mest.add_eit(new_eit_)

            if choice == "2":
                new_fellow_ = Fellow(name=input("Enter fellow's name:\n"),nationality=input("Enter nationality;\n"))
                mest.add_fellow(new_fellow_)

            if choice == "3":
                fellow_name = input("Enter fellow's name")
                for fellow in self.fellows:
                    if fellow.name == name:
                        dinner = Fellow()
                        dinner.eat(fellow)
                        return print("{} is now full".format(fellow.name))
                    else:
                        print("That is not a fellow!")

            if choice == "4":
                fellow_name = input("Enter fellow's name")
                for fellow in self.fellows:
                    if fellow.name == name:
                        lesson = Fellow()
                        lesson.teach(fellow)
                        return print("{} has taught the EITs".format(fellow.name))
                    else:
                        print("That is not a fellow!")

runmest = School()
runmest.loop()