inventory={
    "laptop":10,
    "mouse":25,
    "keyboard":15
}
print(inventory)
inventory["monitor"]=8
print(inventory)
inventory["laptop"]=inventory["laptop"]-2
print(inventory)

for key,value in inventory.items():
    if value<10:
        print(key,value)