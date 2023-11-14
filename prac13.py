#2
def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
                arr[i],arr[min] = arr[min],arr[i]
    return arr

def binarySearch(list, min, max, el):
    if max >= min:
        mid = (max + min) // 2
        if list[mid] == el:
            return mid
        elif list[mid] > el:
            return binarySearch(list, min, mid - 1, el)
        else:
            return binarySearch(list, mid + 1, max, el)
    else:
        return -1

n = int(input("How many nums you want to enter: "))
nums = []

for i in range(n):
    num = int(input(f"{i + 1}: "))
    nums.append(num)

print("not sorted")
print(nums)
print("sorted")
sortedNum = selectionSort(nums)
print(sortedNum)

el = int(input("enter el to find: "))
index = binarySearch(sortedNum, 0, n - 1, el)

if index != -1:
    print(f"Found! Index: {index}")
else:
    print("Not found :(")

print("\n")

#3
def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while (i > -1) and key[0] < A[i][0]:
            A[i+1]=A[i]
            i=i-1 
            A[i+1] = key
    return A

def binarySearchD2(list, min, max, el):
    if max >= min:
        mid = (max + min) // 2
        if list[mid][0] == el:
            return mid
        elif list[mid][0] > el:
            return binarySearchD2(list, min, mid - 1, el)
        else:
            return binarySearchD2(list, mid + 1, max, el)
    else:
        return -1

products = []
inputs = int(input("Enter how many inputs you want: "))

for i in range(inputs):
    info = input(f"Enter {i + 1} info: ")
    while True:
        day = int(input("Enter day of month(1 <= day <= 31): ")) 
        if 1 <= day and day <= 31:
            break
    
    products.append([day, info])

print("not sorted")
for day, info in products:
    print(f"{day} : {info}")

insertionSort(products)

print("sorted")
for day, info in products:
    print(f"{day} : {info}")

dayFind = int(input("Enter day to find and print info: "))
index = binarySearchD2(products, 0, len(products) - 1, dayFind)
print(products[index])