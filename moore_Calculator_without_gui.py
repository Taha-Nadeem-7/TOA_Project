currentstate = "q0"
operation = []
i = 0
userin = []
while True:
    a = input("enter a number or a opertor or =")
    userin.append(a)
    if(a == "="):
        break
        
num = ["0","1","2","3","4","5","6","7","8","9"]
op = ["+","-","*","/"]

while(i < len(userin) and currentstate != "qt"):
    while (currentstate == "q0"):
        if userin[i] in num:
            operation.append(int(userin[i]))
            print(userin[i],end=" ")
            i+=1
            currentstate = "q1"
        elif userin[i] not in num:
            print("Invalid input at state q0")
            currentstate = "qt"

    while currentstate == "q1":
        if currentstate == "q1" and userin[i] in op:
            operation.append(userin[i])
            print(userin[i],end=" ")
            i+=1
            currentstate = "q2"
        elif userin[i] in num:
            operation[0] = int(str(operation[0]) + userin[1])
            print(userin[i],end = " ")
            i+=1
            currentstate = "q1"
        else: 
            print("Invalid input at state q0")
            currentstate = "qt"
    while currentstate == "q2":
        if userin[i] in num:
            operation.append(int(userin[i]))
            print(userin[i],end=" ")
            i+=1
            currentstate = "q3"
            
        elif (userin[i] not in num):
            print("Invalid input at state q2")
            currentstate = "qt"
            
    while currentstate == "q3":
        if userin[i] == "=":
            print("=",end=" ")
            i+=1
            currentstate = "qfinish"
        elif userin[i] in num:
            operation[2] = int(str(operation[2]) + userin[i])
            print(userin[i], end=" ")
            i+=1
            currentstate = "q3"
        else:
            print("Invalid input at state q3")
            currentstate = "qt"

    if currentstate == "qfinish":
        if len(operation) == 3:
            finalans = 0
            if operation[1] == "+":
                finalans = operation[0] + operation[2]
            elif operation[1] == "-":
                finalans = operation[0] - operation[2]
            elif operation[1] == "*":
                finalans = operation[0] * operation[2]
            elif operation[1] == "/":
                finalans = operation[0] / operation[2]
            print(finalans)
