
print("Welcome to MadLib Game")
print()

with open('assets/dark_and_stormy_night_template.txt') as file:
    contents = file.read()
print(contents[0:73])


def read_template():
    Adjective1 = input("write anything")
    Adjective2 = input(">")
    Noun = input(">")

    print(contents[0:73].format(Adjective=Adjective1,
          Adjective3=Adjective2, A_First_Name=Noun))


read_template()
