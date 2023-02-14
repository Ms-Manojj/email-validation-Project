# Email validation project
# user entre some email id and we will checked id is correct or not

print("Program start here :")
print()

print("first user entre the email id")

user=input("Kindy entre your email :")
# user="1998manojsingh@gmail.com"
print(user)
try:
    id=user[0:user.index("@")]
    company_name=user[user.index("@")+1:user.index(".")]
    domain=user[user.index(".")+1:]
except:
    pass
for i in id:
    if id in("#","-","!","$","%","^","&","*"," "):
        print("Incorrect id ")
    else:
        pass

if company_name in ("gmail","email","yahoo","redifmail"):
    # print("id correct")
    pass
else:
    print("id incorrect")

if domain in("com","co.in","in"):
    print("id correct")
else:
    print("id incorrect")

















