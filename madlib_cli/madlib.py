
print("Welcome to MadLib Game")
print()


def read_template():
    with open('assets/dark_and_stormy_night_template.txt') as file:
        content = file.read()
        return content


content = read_template()
print(content[0:73])


def merge():
    Adjective = input(">enter Adjective ")
    Adjective1 = input(">enter Adjective ")
    A_First_Name = input(">enter A First Name ")
    Past_Tense_Verb = input(">enter Past Tense Verb ")
    A_First_Name1 = input(">enter A_First_Name ")
    Adjective2 = input(">enter Adjective2 ")
    Adjective3 = input(">Adjective3 ")
    Plural_Noun = input(">Plural_Noun ")
    Large_Animal = input(">Large_Animal ")
    Small_Animal = input(">Small_Animal ")
    A_Girl_Name = input(">A_Girl_Name ")
    Adjective4 = input(">Adjective4 ")
    Plural_Noun1 = input(">Plural_Noun1 ")
    Adjective5 = input(">Adjective5 ")
    Plural_Noun2 = input(">Plural_Noun2")
    Number_from_1_to_50 = input(">Number_1-50")
    First_Name2 = input(">First_Name2")
    Number1 = input(">Number1")
    Plural_Noun3 = input(">Plural_Noun3")
    Number2 = input(">Number2")
    Plural_Noun4 = input(">Plural_Noun4")
    print(content.format(Adjective=Adjective,
          Adjective1=Adjective1, A_First_Name=A_First_Name, Past_Tense_Verb=Past_Tense_Verb, A_First_Name1=A_First_Name1, Adjective2=Adjective2, Adjective3=Adjective3, Plural_Noun=Plural_Noun, Large_Animal=Large_Animal, Small_Animal=Small_Animal, A_Girl_Name=A_Girl_Name, Adjective4=Adjective4, Plural_Noun1=Plural_Noun1, Adjective5=Adjective5, Plural_Noun2=Plural_Noun2, Number_from_1_to_50=Number_from_1_to_50, First_Name2=First_Name2, Number1=Number1, Plural_Noun3=Plural_Noun3, Number2=Number2, Plural_Noun4=Plural_Noun4,).rstrip('\n'))


merge()
