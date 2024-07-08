#!/usr/bin/python3

post = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as postfile:
    for line in postfile:
        if "POST" in line:
            post +=1

print(f"nunmber of successful post is: {post}")
