Subjects = {
    "Math":[],
    "Science":[],
    "English":[],
    "Soc. Science":[],
    "Int. Science":[],
    "Spanish":[],
    "Health":[]
}

def add_assignment(subject, assignment):
    Subjects[subject].append(assignment)


def remove_assignment(subject, assignment):
    Subjects[subject].remove(assignment)
    print("removed ", assignment)

def add_subject(subject):
    if subject not in Subjects.keys():
        Subjects[subject] = []
    else:
        print("Subject already exists")

def remove_subject(subject):
    if subject in Subjects.keys():
        del Subjects[subject]
    else:
        print("Subject not found")

def view_subjects():
    print(f"{"-"*13}Psuedo Version 1{"-"*13}")
    for subject in Subjects:
        print(f"{subject}: \n {Subjects.get(subject)}")

    print("-"*25)


def compiler(option):
    if option == "1":
        uinput = input("select the subject and name of assignment seperated by '|' char to add: ")
        uinput = uinput.split("|")
        add_assignment(uinput[0], uinput[1])

    if option == "2":
        uinput = input("select the subject and name of assignment seperated by '|' char to remove: ")
        uinput = uinput.split("|")
        remove_assignment(uinput[0], uinput[1])

    if option == "3":
        view_subjects()

    if option == "4":
        uinput == input("Tell the course name you want to add to subjects: ")
        add_subject(uinput)

    if option == "5":
        uinput = input("Tell the course name you want to remove from subjects: ")
        remove_subject(uinput)


# add_assignment("Math", "Homework3 2")
# view_subjects()
# remove_assignment("Math", "Homework3 2")
# view_subjects()

#interface:
running = True


while running == True:
    print(f"1.) add assignment")
    print(f"2.) remove assignment")
    print(f"3.) view total subjects")
    print(f"4.) Add subject")
    print(f"5.) Add subject")
    print(f"4.) close program")
    uinput = input("Select an option >>> ")
    if uinput == "close":
        running = False
    compiler(uinput)