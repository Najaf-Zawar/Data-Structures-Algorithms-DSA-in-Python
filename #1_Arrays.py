from array import *
arr = array('i',[1,2,3,4,5])    # i is typecode

# print(arr.buffer_info())      #->(2114425143920, 3)
                                #          |       |
                                #       Address   size

# arr.reverse()                 # Reverse the array         
# print(arr)

######### Indexing ############
# print(arr[2])
# print(arr[4])

# ######## Iterating ############
# for i in range(len(arr)):
#     print(arr[i])
    
# for i in arr:
#     print(i)

######### Creating new Array with old Array ##############
# newArr = array(arr.typecode, (i for i in arr))
# print(newArr)
    
# SquareArr = array(arr.typecode, (i*i for i in arr)) #Square of Array
# print(SquareArr)

# for i in SquareArr:
#      print(i)


############### User Input Array #########################
myArr = array('i',[])

n = int(input("Enter the length of Array: "))

for i in range(n):
    val = int(input(f"Enter {i+1} value in array: "))
    myArr.append(val)

print(myArr)

############# Search by Value #################
sVal = int(input("Enter value you want to Search: "))

# Manually
count = 0
for i in range(len(myArr)):
    if sVal == myArr[i]:
        print(f"Value found at Index: {i}")
        break
    else:
        count += 1
        
# Built in Function
print(f"Value found at: {myArr.index(sVal)}")


        