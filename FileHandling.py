with open("a.txt", "w") as file_a:
    file_a.write("6")
with open("b.txt", "w") as file_b:
    file_b.write("7")
with open("a.txt","r") as file_a:
    num1 = int(file_a.read())
with open("b.txt","r") as file_b:
    num2 = int(file_b.read())
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
print("file c is being created")
with open("c.txt","w") as file_c:
    file_c.write("Addition:"+str(addition)+"\n")
    file_c.write("Subtraction:"+str(subtraction)+"\n")
    file_c.write("Multiplication:"+str(multiplication)+"\n")


