import os
import re
import sqlite3

pattern = r'(\d{3}\.\d*\s)(.*)(\.....*)'
writings = []

for item in os.listdir('lib'):
	parsed_string = re.match(pattern, item)
	parsed_list = list(parsed_string.group(2).split(' - '))
	if len(parsed_list) == 1:
		parsed_list.insert(0, 'Noname')
		writings.append(tuple(parsed_list))
	elif len(parsed_list) == 3:	
		parsed_list = [parsed_list[0], parsed_list[1] +' ' + parsed_list[2]] 
	else:
		writings.append(tuple(parsed_string.group(2).split(' - ')))


conn = sqlite3.connect('database.db')
conn.executemany('INSERT INTO  writings (author, writing) VALUES (?,?)', writings )
conn.commit()
conn.close()
