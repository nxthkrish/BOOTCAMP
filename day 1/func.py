def name():
    name=input("Enter the name")
    age=int(input("Enter the age"))
    print("NAME IS ", name ," ","AGE IS ",age)
def che_ck():
    names=[]
    ages=[]
    for i in range(2):
        name = input(f"Enter the name of person {i + 1}: ")
        age = int(input(f"Enter the age of person {i + 1}: "))
        names.append(name)
        ages.append(age)
        index_of_max_age = ages.index(max(ages))
        print(f"The person with the highest age is {names[index_of_max_age]} with age {ages[index_of_max_age]} years.")
def ajay():
    name=input("Enter the name")
    age=int(input("Enter the age"))
    if name=='AJAY' or name=='ajay' :

        print("NAME IS ", name ," ","AGE IS ",age)

    else :

        print("NAME IS INVALID")
    
name()




    
    