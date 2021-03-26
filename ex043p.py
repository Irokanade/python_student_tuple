i = 1
studentList = []
chineseTotal = 0
englishTotal = 0
mathTotal = 0
chineseAvg = 0
englishAvg = 0
mathAvg = 0

while i < 4:
    temp = str(input('enter student {0} name : '.format(i)))
    studentList.append(temp)    

    temp = str(input("enter student {0} id: ".format(i)))

    validNum = 0
    for j in temp:
        #print(i)
        if j.isdigit():
            validNum += 1

    while validNum != 5:
        validNum = 0
        print("id must be 5 characters long and all digit characters, try again")
        temp = str(input("enter student {0} id: ".format(i)))
        for j in temp:
            if j.isdigit():
                validNum += 1

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

'''
for j in range(1, 3):
    print(studentList[j])

'''

#chinese total
#print('chinese')
j = 2
while j <= len(studentList):
    #print(studentList[j])
    chineseTotal += studentList[j]
    j += 5
    
#english total
#print('english')
j = 3
while j <= len(studentList):
    #print(studentList[j])
    englishTotal += studentList[j]
    j += 5

#maths total
j = 4
while j <= len(studentList):
    #print(studentList[j])
    mathTotal += studentList[j]
    j += 5
    

#print('studnetlist/5: {0}'.format(str(len(studentList)/5)))
chineseAvg = chineseTotal/(len(studentList)/5)
englishAvg = englishTotal/(len(studentList)/5)
mathAvg = mathTotal/(len(studentList)/5)

'''
print(chineseTotal)
print(englishTotal)
print(mathTotal)
'''

print(chineseAvg)
print(englishAvg)
print(mathAvg)






 