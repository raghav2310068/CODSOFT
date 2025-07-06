from  random import choice
char_small=[chr(i) for i in range(97,123)]
char_big=[chr(i) for i in range(65,91)]
nums=[f"{i}" for i in range(0,10)]
symbols=["!","@","#","$","%","^","&","*","(",")","_","-","+","=","<",">",".","?","/"]
print("welcome to the password generator".title())
length=int(input("enter the length of the password: "))
choices=[char_small,char_big,nums,symbols]
password=""
for i in range(length):
    choice1=choice(choices)
    char=choice(choice1)
    password+=char

print(f"your password is: {password}")







