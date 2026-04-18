numbers=(10,20,30,40,50)
print(numbers)

fruits=("apple","banana","mango")
print(fruits[0])
print(fruits[2])

fruits=("apple","banana","mango")
print(fruits[-1])
print(fruits[-2])

numbers=(10,20,30,40,50)
print(len(numbers))

numbers=(10,20,30,40,50)
print(len(numbers))

numbers=(10,20,30,40,50)
for i in numbers:
    print(i)

numbers=(10,20,30,40,50)
#Cannot happen because Tupes are immutable
#numbers[1]=200

#Packing
students=("Rahul",22,"Python")
print(students)

#Unpacking
name,age,course=students

print(name)
print(age)
print(course)

#Mixed Datatype
data=("Arjun",25,True,5000.50)
print(data)