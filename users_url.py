import os

def users_url(url):
		users = {}
		with open('./project/log/weblog.csv') as o:
			l = o.readlines()
		for i in range(1, len(l)):
			s = l[i].split(',')
			if url == s[4][:-1]:
				if s[1] != '' and s[1] not in users.keys():
					users[s[1]] = 1
				elif s[1] != '':
					users[s[1]] += 1
		return users

users = users_url('http://127.0.0.1:8000/welcome')
print(users)