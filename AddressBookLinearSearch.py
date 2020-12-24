'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#Firt we will implement the function for linear search algorithm

def search(addressBook,mobileNumber):
    for index in range(len(addressBook)):
        if(addressBook[index]==mobileNumber):
            return index
    return -1
    
#Now we will write the actualprogram touse above logic
ADDRESSBOOK=[]
absize=int(input("Enter NO OF MOBILE NUMBERS YOU WANT TO ADD IN ADDRESS BOOK:"))
if(absize>1)
print("NOW ITS TIME TO ADD "+str(absize)+ " MOBILE NUMBER(S) TO YOUR ADDRSS BOOK")
for i in range(0,absize):
    INPUTMOBILENUMBER=input()
    ADDRESSBOOK.append(INPUTMOBILENUMBER)
    

print("HAVE A LOOK! YOU ARE ADDRESS BOOK BELOW")
print(ADDRESSBOOK)

#NOW YOU NEED TO ENTER MOBILENUMBER TO SEARCH 
MOBILENUMBER=input("HEY!ENTER MOBILE NUMBER YOU WANT TO SEARCH HERE::")

#NOW WE WILL USE THE LINEAR SEARCH ALGORITHM TO SEARCH MOBILE NUMBER IN ADDRESS BOOK

if(-1==search(ADDRESSBOOK,MOBILENUMBER)):
    print("OOPS !"+MOBILENUMBER +" IS NOT PRESENT IN YOUR ADDRESS BOOK")
else:
    print("WOW ! "+MOBILENUMBER +" IS PRESENT IN YOUR ADDRESS BOOK")
##END OF program
#NOTE WE DIDNT USE ANY STANDARD NAMING CONENTIONS HERE FOR PRACTICE WE WILL LEARN THOSE LATER
        
    
