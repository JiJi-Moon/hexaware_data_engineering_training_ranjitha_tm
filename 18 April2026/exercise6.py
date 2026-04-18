classA={"Rahul","Sneha","Amit","Neha"}
classB={"Sneha","Amit","Karan","Riya"}
print("Class A:",classA)
print("Class B:",classB)
print("Students in both class:",classA.intersection(classB))
print("Students only in class A",classA.difference(classB))
print("All Unique Students:",classA.union(classB))