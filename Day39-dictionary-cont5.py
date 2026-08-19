#-----------------------------#
#            DICT             #
#-----------------------------#

#the dict function is like the list(), str(), int() functions but for the dictionary class
#here is an example of it in use:

#to perform this you have to have something like a matrix structure

classes = [
    ["class1", "Ms.Heming"],
    ["class2", "Mr.Cornobonos"],
    ["class3", "Ms.Griddle"]
]

print(dict(classes))

#-----------------------------#
#           NESTING           #
#-----------------------------#

#you can nest dictionaries inside dictionaries. here is an example:

world = {
    "Asia":{"Russia":"Moscow", 
            "China":"Bei Jing", 
            "Nepal":"Kathmandu"},
    "Europe":{"Luxembourg":"Luxembourg City", 
              "England":"London", 
              "Netherland":"Amsterdam"},
    "Africa":{"Kenya":"Nairobi", 
              "Egypt":"Cairo", 
              "Morroco":"Rabat"}
}

#notice how they are nested within eachother?
#WARNING: you can't set the key as a mutable object that means NO LISTS AND DICTS


#here is an example that uses random junk but uses lists and dictionaries

junk_files = {
    "Media1":["Photos.png", "Interstellar.gif", "Chrome.exe", "Monsters_31ds345.exe"],
    "The_third_median":{
        "anatos forbora dos camos":1,
        "Nomos bro aftoromoka thoro":2,
        "Incoboto in tra a bolo":3,
        "Sony bony tho lony":4,
        "Sing me to summon the median after two":-1
    },
    "Songs":[
        "Happy birthday",
        {"Old mac don ald":"Had no farm"},
        "song",
    ],

}

#that is a fake directory of junk files with lists and dictionaries intertwined
#to make this actually useful we can get values like this:

print(junk_files["Media1"])

print(junk_files["Songs"][1])

print("-"*25)
#here is someone navigating this mess:

print(junk_files["The_third_median"])

print(junk_files["The_third_median"]["Sing me to summon the median after two"])

mystery = {

  "a": 2

}



mystery.setdefault("A", 5)

mystery.setdefault("a", 10)

mystery.setdefault("B", 30)

mystery.setdefault("B", 40)

print(mystery)