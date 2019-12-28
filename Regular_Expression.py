'''
Identifier
\d=any number
\D=anything but a number
\s=space
\S=anything but a space
\w=any character
\W=anything but a character
.=any character except for a newline
\b=whitespace around words
\.=a period

Modifiers:
{1,3} we're expecting 1-3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ match the beginning of a string
| matches either or e.g. \d{1-3}|\w{5-6}
[] Match range or "variance" e.g. [A-Za-z] or [1-5a-qA-Z]
{x} expecting "x" amount

White Space Characters:
\n new line
\s space
\t tab
\e escape (rare)
\f form feed (rare)
\r return
'''

import re
examplestring='''Jessica is 15 year old, and Daniel is 27 year old.
Edward is 97, and his grandfather,Oscar ,is 102
'''
ages=re.findall(r'\d{1,3}',examplestring)
names=re.findall(r'[A-Z][a-z]*',examplestring)
print(ages)
print(names)
dict1={}
for i in range(len(ages)):
    k=ages[i]
    v=names[i]
    dict1.update({k:v})
print(dict1)

mailid=input("Enter the mailid:")
print(mailid)
if re.search(r'[0-9a-zA-Z].@[a-zA-z].(com)$',mailid):
    print("Correct")
else:   
    print("Incorrect")