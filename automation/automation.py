import re
with open("automation/assest/potential-contacts.txt","r") as f:
    file_content=f.read()

# print(file_content)

match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file_content)
# print(match[0])
# match.sort()
# s=(1,2,3,4,4,5)/
# print(s)
match=set(match)
match1=sorted(match)

print(match1)


with open("automation/assest/Email.txt", "w") as f:
    for element in match1:
        f.write(element + "\n")

phone = re.findall(r'\d{3}-\d{3}-\d{4}|\d{3}-\d{4}', file_content)
phone=set(phone)
phone1=sorted(phone)

with open("automation/assest/phone.txt", "w") as f:
    for element in phone1:
        if len(element)==12:
            f.write( element + "\n")
        if len(element)==8:
          f.write( "206-"+ element + "\n")


# print(phone)
