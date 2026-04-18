numbers=[10,20,30,40,50]
print(numbers)
fruits=["apple","banana","mango","orange"]
print(fruits[0])
print(fruits[2])
#Access from end
print(fruits[-1])
print(fruits[-2])

#modify elements
numbers=[10,20,30]
numbers[1]=200
print(numbers)

#Add an element
numbers.append(40)
print(numbers)

#Insert
numbers=[10,20,40]
numbers.insert(2,30)
print(numbers)

#Remove
numbers=[10,20,30,40]
numbers.remove(30)
print(numbers)

#remove last Element
numbers.pop()
print(numbers)
print(len(numbers))

#print all elements one by one
numbers=[10,20,30,40]
for num in numbers:
    print(num)

#Check if an element is present in the list
fruits=["apple","banana","mango"]
if "banana" in fruits:
    print("Banana exists")

#Slice
numbers=[10,20,30,40,50]
print(numbers[1:4])

#Reverse the list
numbers=[10,20,30,40,50]
numbers.reverse()
print(numbers)

#Sort the list
numbers.sort()
print(numbers)

# Min and Max values of the list
print(max(numbers))
print(min(numbers))

#Sum of the list
print(sum(numbers))