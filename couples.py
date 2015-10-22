def get_RightCase(nameNum):
    isRightCase = True

    variable = raw_input("\nRead in " +  nameNum +  " Name: ")
    if variable == "q":
        exit()
    
    while isRightCase:
        if re.match("^[a-zA-Z ]*$",variable):
            isRightCase = False
        else:
            variable = raw_input("Error: Enter Name Again: ")

    return variable




import re
from dictionary import *
    
dict = Dictionary()
f = open('dictionary.txt', 'r')
for line in f:
    line = line.strip('\n')
    dict.add_word(line)

print "Couple Name Generator: Enter q to quit"
while True:
    name1 = get_RightCase("First")
    name2 = get_RightCase("Second")

    print "\nCouple names Made from", name1, "and", name2


    name1 = (name1.lower()).split(' ')
    name2 = (name2.lower()).split(' ')



    for n1 in name1:
        for n2 in name2:
            for i in range(2,len(n1)):
                for j in range(2,len(n2)):
                    tmp = n1[:i] + n2[-j:]
                    if dict.word_exists(tmp):
                        print tmp
                    tmp = n2[:j] + n1[-i:]
                    if dict.word_exists(tmp):
                        print tmp
                















