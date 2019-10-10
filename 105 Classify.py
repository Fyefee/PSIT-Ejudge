"""ig : chw_jeffy"""
def main():
    """Classify"""
    allstudent = []
    count = 1
    count2 = 0
    while 1:
        student = input()
        if student == "END":
            break
        allstudent.append(student)
    allstudent.sort()
    for i in range(len(allstudent)-1):
        if allstudent[i][0:2] == allstudent[i+1][0:2] and allstudent[i][2:4] \
            == allstudent[i+1][2:4]:
            count += 1
        elif allstudent[i][0:2] == allstudent[i+1][0:2] and count2 == 0:
            print("%s %s %s"%(allstudent[i][0:2], int(allstudent[i][2:4]), count))
            count = 1
            count2 += 1
        elif allstudent[i][0:2] == allstudent[i+1][0:2] and count2 > 0:
            print("-- %s %s"%(int(allstudent[i][2:4]), count))
            count2 += 1
            count = 1
        elif allstudent[i][0:2] != allstudent[i+1][0:2] and count2 > 0:
            print("-- %s %s"%(int(allstudent[i][2:4]), count))
            count2 = 0
            count = 1
        else:
            print("%s %s %s"%(allstudent[i][0:2], int(allstudent[i][2:4]), count))
            count2 = 0
            count = 1
    if allstudent[len(allstudent)-1][0:2] == allstudent[len(allstudent)-2][0:2]:
        print("-- %s %s"%(int(allstudent[len(allstudent)-1][2:4]), count))
    else:
        print("%s %s %s"%(allstudent[len(allstudent)-1][0:2], \
            int(allstudent[len(allstudent)-1][2:4]), count))

main()
