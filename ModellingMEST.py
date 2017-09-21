#MEST is a school that contains EITs and Fellows.
# Create classes to represent all three entities.
# - EITs have name, nationality, fun_fact and the ability to recite fun facts about tech class 
# - Fellow has name, nationality, happiness_level and abilities to eat (increases happiness) and teach (decreases happiness)
# - School has EITs and Fellows

class Person:
    #Class person holds the shared properties of EITs and fellows
    def __init__(self, name, nationality):#construct name and nationality
        self.name = name
        self.nationality = nationality


class EIT(Person):#Class for EITs' unique properties

    def __init__(self, name, nationality, fun_fact):
        super().__init__(name, nationality)
        self.fun_fact = fun_fact

    def recite(self, eit_name):#method for EITs' behavior 'recite fun fact about tech class'
        print(self.fun_fact)


class Fellow(Person):#class for fellows unique properties

    def __init__(self, name, nationality, happiness_level=5):#happiness level has a default value of 5 which increases or decreases depending on fellows behavior
        super().__init__(name, nationality)
        self.happiness_level = happiness_level

    def eat(self, fellow):#increase happiness when fellow eats
        self.happiness_level += 1

    def teach(self, fellow):#decrease happiness when fellow teaches
        self.happiness_level -= 1


class School:
    #class school hold the objects fellows and EITs
    def __init__(self,eits=[],fellows=[]):#School has two lists eits for object EITs and fellows for object Fellows
        self.eits = eits
        self.fellows = fellows

    def add_eit(self, new_eit):#Add an EIT to the eits list
        self.eits.append(new_eit)

    def add_fellow(self, new_fellow):#Add a fellow to the fellows list
        self.fellows.append(new_fellow)

    def loop(self):

        while True:#start a loop where methods will be called
            mest = School()#instantiate the School class
            #prompt the user for an action he wants to do 
            choice = input("Select:\n1 to add EIT.\n2 to add fellow.\n3 to eat(fellows only)\n4 to teach (fellows only)\n")

            if choice == "1":
                #intantiate class EIT to take an EIT's arguements
                new_eit_ = EIT(name=input("Enter EIT's name:\n"),nationality=input("Enter nationality;\n"),fun_fact=input("Enter fun fact about tech"))
                mest.add_eit(new_eit_)

            if choice == "2":
                #intantiate class Fellow to take an fellow's arguements
                new_fellow_ = Fellow(name=input("Enter fellow's name:\n"),nationality=input("Enter nationality;\n"))
                mest.add_fellow(new_fellow_)

            if choice == "3":
                fellow_name = input("Enter fellow's name")#Prompt user for which fellow should eat
                for fellow in self.fellows:#iterate through list fellows to find the fellow
                    if fellow.name == name:
                        dinner = Fellow()#intantiate class fellows
                        dinner.eat(fellow)#call the eat method in the Fellows class
                        return print("{} is now full".format(fellow.name))
                    else:
                        print("That is not a fellow!")#if fellow is not in the list, print this

            if choice == "4":
                fellow_name = input("Enter fellow's name")#prompt user for which fellow should eat
                for fellow in self.fellows:#look for this fellow in the fellows list
                    if fellow.name == name:
                        lesson = Fellow()#instantiate the class fellows
                        lesson.teach(fellow)#call method to make the fellow teach
                        return print("{} has taught the EITs".format(fellow.name))
                    else:
                        print("That is not a fellow!")#if fellow is not in the list, print this


runmest = School()#intantiate the school
runmest.loop()#start the loop to perform object behaviors