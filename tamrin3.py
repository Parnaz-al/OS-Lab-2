import random
print("choose!")
print("✋->1")
print("🤚->2")
user=input()
comp1=random.randint(1,2)
comp2=random.randint(1,2)
if(comp1==comp2):
    if (user!=comp1):
        print("you lose")
        print("compueter1:",comp1,"computer2:",comp2)
    
    else:
        print("no one lose")
        print("compueter1:",comp1,"computer2:",comp2)
    
else:
     if(user==comp1):
        print("compurer2 lose")
        print("compueter1:",comp1,"computer2:",comp2)
    
     else:    
        print("computer1 lose")
        print("compueter1:",comp1,"computer2:",comp2)
    
        





