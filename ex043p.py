i = 1
studentList = []

while i < 4:
    temp = str(input('enter student {0} name : '.format(i)))
    studentList.append(temp)    

    temp = str(input("enter student {0} id: ".format(i)))
    while len(temp) != 5:
        print("id must be 5 characters long, try again")
        temp = str(input("enter student {0} id: ".format(i)))

    studentList.append(temp)
    temp = float(input("enter student {0} chinese score: ".format(i)))
    while temp > 100 or temp < 0:
        print("score error")
        temp = float(input("enter student {0} chinese score: ".format(i)))

    studentList.append(temp)
    temp = float(input("enter student {0} english score: ".format(i)))
    while temp > 100 or temp < 0:
        print("score error")
        temp = float(input("enter student {0} english score: ".format(i)))

    studentList.append(temp)
    temp = float(input("enter student {0} mathematics score: ".format(i)))
    while temp > 100 or temp < 0:
        print("score error")
        temp = float(input("enter student {0} mathematics score: ".format(i)))

    studentList.append(temp)
    i += 1
    

tuple(studentList)

for i in studentList:
    print(i)