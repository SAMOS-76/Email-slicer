email = input("What is your email?: ")
username = email.split("@", 1)[0]
domain_name = email.split("@", 1)[1]
print("Username: " + username)
print("Domain Name: " + domain_name)
