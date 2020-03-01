#!/usr/bin/env python3

import redis
r_server = redis.Redis()

print("\n\nStarting with a clean database...")
r_server.flushdb()

for num in "one", "two", "three", "four", "five":
    r_server.rpush("nums", num)

length = r_server.llen("nums")

print("\nShowing the length of the list: ", length, "\n")

print("One way of showing the contents of the list:")
for x in range(0,length):
    print(str(r_server.lindex("nums",x)))

print("\nAnother way of showing the contents of the list:")
print(str(r_server.lrange("nums",0,-1)))

print("\n\nFlushing the database...\n")
r_server.flushdb()
