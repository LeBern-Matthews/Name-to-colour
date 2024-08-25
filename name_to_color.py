names=[]
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x=True
sums=[]
number=0
print("Instructions: Enter three of your names")
for x in range(1,4):
    name=input("Enter name: ")
    names.append(name)
    #quit=input("Is that all the names you wish to use? (yes/no)")

for name in names:
    for letter in name:
        for index, alpha_letter in enumerate(alphabet, start=1):
            if letter==alpha_letter:
                number+=index
                
    sums.append(number)
    print(sums)
    number=0
    
newsum=list(map(lambda x:x*4,sums))
for index, number in enumerate(newsum):
    if number > 255:
        newsum[index]=number-256
        print("in if statement")
print(newsum)
    
        