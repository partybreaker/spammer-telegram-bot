import requests
from pprint import pprint

def getList():
	try:
		return requests.get("http://spys.me/proxy.txt")
	except requests.exceptions.ConnectionError:
		return getList()
	return

def main():
	my_list = getList().text.split("\n")
	my_list2 = []
	my_list3 = []
	i = 0
	while i<9:
		del my_list[0]
		i += 1
	del my_list[-1]
	del my_list[-1]
	for x in my_list:
		try:
			if x.split()[2] == "+" and x.split()[1][-1] == "S":
				my_list2.append(x.split())
		except IndexError:
			pass
	with open("proxies.txt", "w") as file:
		file.write("")
	with open("proxies.txt", "a") as file:	
		for x in my_list2:
			file.write(x[0]+"]")
main()