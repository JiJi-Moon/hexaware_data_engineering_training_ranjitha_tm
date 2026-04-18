emails=["user1@gmail.com","user2@yahoo.com","user3@gmail.com","user4@outlook.com"]

domains=[]

for email in emails:
    domains.append(email.split("@")[1])
print(domains)
unique_domains=list(set(domains))
print(unique_domains)
domain_count=dict()
for domain in unique_domains:
    domain_count[domain]=domains.count(domain)
print(domain_count)

