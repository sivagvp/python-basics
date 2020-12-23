# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#@author : Siva Ganesh
def search(arr,x):
    for i in range(len(arr)):
     if(arr[i]==x):
       return i
    return -1  
list =[]
n=int(input("Enter no of elements:"))
print("please enter "+str(n)+" elements:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print("Entered Elements are:") 
print(list) 
searchElement=int(input("Enter element to search:"))
index=search(list,searchElement)
if(index==-1):
    print("ELEMENT NOT FOUND AT INDEX")
else:
    print("Element found at index:"+str(index))

 
