#!/usr/bin/env python3
from luxand import luxand
import os

client = luxand("a3bb88b48d274bb5be690c0952002085")

for p in os.listdir("Photos"):
	print("Recognizing people in %s" % p)
	people = client.recognize("Photos/" + p)

	for pp in people:
		print("  %s with %3.2f%s probability" % (pp["name"], 100 * float(pp["probability"]), '%'))
