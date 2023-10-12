def multiplication(number):
    print(f"Multiplication table for {number}:\n")
    for i in range(1,11):
        result=number*i
        print(f"{number} x {i} = {result}")
        
num=int(input("enter the number to find multiplication table"))
multiplication(num)


    
    