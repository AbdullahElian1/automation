import re
with open("automation/assest/potential-contacts.txt","r") as f:
    file_content=f.read()

# print(file_content)

match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file_content)
# print(match[0])
match=set(match)


with open("automation/assest/Email.txt", "w") as f:
    for element in match:
        f.write(element + "\n")

phone = re.findall(r'\d{3}-\d{3}-\d{4}', file_content)
phone1 = re.findall(r'\d{3}-\d{4}', file_content)

with open("automation/assest/phone.txt", "w") as f:
    for element in phone:
        f.write( element + "\n")


print(phone)
