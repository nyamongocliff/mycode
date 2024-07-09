#! /usr/bin/env python3

i= 0
foo = open("/home/student/mycode/cfgread/dracula.txt", "r")

foo_lines = foo.readlines()

for line in foo_lines:
    #i+=1
    #rint(i)

    if "vampire" in line.lower():
        i+=1
        print(i)
        print(line)








foo.close()
