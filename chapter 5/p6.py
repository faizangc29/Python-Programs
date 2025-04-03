# Problem 6 & 7 & 8
# write dict of 4 friends and input name and language
# if name of two friends is same what will happen  "first name is skiped"
# if language is same of two friends what will happen "it shows output  all friends no one will skip"


d = {}

name = input("enter name ")
lang = input("enter language ")
d.update({name: lang})
name = input("enter name ")
lang = input("enter language ")
d.update({name: lang})
name = input("enter name ")
lang = input("enter language ")
d.update({name: lang})
name = input("enter name ")
lang = input("enter language ")
d.update({name: lang})

print(d)