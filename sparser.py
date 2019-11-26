class Parser(object):
	import requests
	def __init__(self):
		pass

	def getList(self):
		try:
			return self.requests.get("http://spys.me/proxy.txt")
		except self.requests.exceptions.ConnectionError:
			return self.getList()
		return

	def load_proxies(self):
		self.main()
		with open("proxies.txt", "r") as file:
			return file.read().split("|")[0:-1:]

	def main(self):
		my_list = self.getList().text.split("\n")
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
				file.write(x[0]+"|")
