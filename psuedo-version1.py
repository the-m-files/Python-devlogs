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

def view_subjects():
    for subject in Subjects:
        print(subject)

add_assignment("Math", "Homework3 2")
view_subjects()
remove_assignment("Math", "Homework3 2")
view_subjects()

#interface:

running = True

while running == True:
    print(f"1.) add assignment")
    print(f"2.) remove assignment")
    print(f"3.) view total subjects")
    print(f"4.) close program")
    uinput = input("Select an option >>> ")

    if uinput == "1":
        uinput = input("select the subject and name of assignment seperated by '|' char to add: ")
        uinput = uinput.split("|")
        add_assignment(uinput[0], uinput[1])

    if uinput == "2":
        uinput = input("select the subject and name of assignment seperated by '|' char to remove: ")
        uinput = uinput.split("|")
        remove_assignment(uinput[0], uinput[1])

    if uinput == "3":
        view_subjects()

    if uinput == "4":
        print("closing program")
        running = False

