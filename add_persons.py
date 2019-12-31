#!/usr/bin/env python3
from luxand import luxand
import os

client = luxand("a3bb88b48d274bb5be690c0952002085")

for p in os.listdir("People"):
	name = p.split(".")[0]
	print("Adding %s" % name)
	client.add_person(name, photos = ["People/" + p])
