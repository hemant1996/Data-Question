def array_to_number(a):
    if(a[0][0] =="0" and a[0][1] =="_" and a[0][2] =="0" and a[1][0] =="|" and a[1][1] =="0" and a[1][2] =="|" and a[2][0] =="|" and a[2][1] =="_" and a[2][2] =="|"):
        return 0
    elif(a[0][0] =="0" and a[0][1] =="0" and a[0][2] =="0" and a[1][0] =="0" and a[1][1] =="0" and a[1][2] =="|" and a[2][0] =="0" and a[2][1] =="0" and a[2][2] =="|"):
        return 1
    elif(a[0][0] =="0" and a[0][1] =="_" and a[0][2] =="0" and a[1][0] =="0" and a[1][1] =="_" and a[1][2] =="|" and a[2][0] =="|" and a[2][1] =="_" and a[2][2] =="0"):
        return 2
    elif(a[0][0] =="0" and a[0][1] =="_" and a[0][2] =="0" and a[1][0] =="0" and a[1][1] =="_" and a[1][2] =="|" and a[2][0] =="0" and a[2][1] =="_" and a[2][2] =="|"):
        return 3
    elif(a[0][0] =="0" and a[0][1] =="0" and a[0][2] =="0" and a[1][0] =="|" and a[1][1] =="_" and a[1][2] =="|" and a[2][0] =="0" and a[2][1] =="0" and a[2][2] =="|"):
        return 4
    elif(a[0][0] =="0" and a[0][1] =="_" and a[0][2] =="0" and a[1][0] =="|" and a[1][1] =="_" and a[1][2] =="0" and a[2][0] =="0" and a[2][1] =="_" and a[2][2] =="|"):
        return 5
    elif(a[0][0] =="0" and a[0][1] =="_" and a[0][2] =="0" and a[1][0] =="|" and a[1][1] =="_" and a[1][2] =="0" and a[2][0] =="|" and a[2][1] =="_" and a[2][2] =="|"):
        return 6
    elif(a[0][0] =="0" and a[0][1] =="_" and a[0][2] =="0" and a[1][0] =="0" and a[1][1] =="0" and a[1][2] =="|" and a[2][0] =="0" and a[2][1] =="0" and a[2][2] =="|"):
        return 7
    elif(a[0][0] =="0" and a[0][1] =="_" and a[0][2] =="0" and a[1][0] =="|" and a[1][1] =="_" and a[1][2] =="|" and a[2][0] =="|" and a[2][1] =="_" and a[2][2] =="|"):
        return 8
    elif(a[0][0] =="0" and a[0][1] =="_" and a[0][2] =="0" and a[1][0] =="|" and a[1][1] =="_" and a[1][2] =="|" and a[2][0] =="0" and a[2][1] =="_" and a[2][2] =="|"):
        return 9
def findNumber(start, end):
    f = open("input_user_story_1.txt", "r")
    lines = f.readlines()
    liness = lines[start:end]
    arry = [["0" for x in range(4)] for y in range(4)]
    number_arr = [[["0" for k in range(4)] for j in range(4)] for i in range(10)]
    count = 0
    row = 0
    column = 0
    no = 0
    number_count = 0
    for x in liness:
        for i in x:
            if(no%3 == 0):
                column = 0
                number_count = int(no/3)
            if(i == "|" or i == "_"):
                number_arr[number_count][row][column] = i
            column = column + 1
            no = no + 1
        row = row + 1
        column = 0
        no = 0
    value = ""
    for x in range(0,9):
        value = value + str(array_to_number(number_arr[x]))
    return value
start = 0
end = 3
for i in range(0,100):
    print(findNumber(start,end))
    start = start + 4
    end = end + 4