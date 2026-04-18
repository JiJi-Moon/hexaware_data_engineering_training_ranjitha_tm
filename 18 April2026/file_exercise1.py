logins=[]
with open("logins.txt","r") as f:
    for i in f:
        logins.append(i.strip())
login_count=dict()
unique_login=list(set(logins))

for uni in unique_login:
    login_count[uni]=logins.count(uni)
max_login=max(login_count,key=login_count.get)
print("Total number of login records",len(logins))
print("Login in counts",login_count)
print("Most logged person",max_login)
print("Unique users",unique_login)
