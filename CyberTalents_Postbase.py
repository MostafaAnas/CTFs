#!/bin/python
import base64
from string import ascii_lowercase
from string import ascii_uppercase

validChars = ascii_lowercase + ascii_uppercase + "123456789"

#print(validChars)

for c in validChars:
	for d in validChars:
		data = "R" + c + d + "BR3tCNDUzXzYxWDdZXzRSfQ=="
		decoded = base64.b64decode(data)
		if "FLAG" in decoded:
			print(decoded)
