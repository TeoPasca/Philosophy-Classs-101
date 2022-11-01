
from bs4 import BeautifulSoup
import requests
import re
import sys

divisions = ["Theoretical", "Practical", "Logic", "Quit"]
theoretical = ["Metaphysics", "Epistemology", "Return"]
practical = ["Ethics", "Aesthetics", "Social", "Political", "Return"]
logic = ["Logic"]
#---------------PRINT
def line():
	print("-" * 20)
def selectAbove():
	print("Please select from above")
def selectBelow():
	print("Please select from below")
def oneReturn():
	line() 
	print("1 Return")
	line()
def listItemsIn(menus):
	line()
	index = 1
	for Items in menus:
		print(f"{index}.", Items)
		index +=1
	line()
def backToThe(previousMenu):
	oneReturn()
	while True:
		choose6 = input()
		if choose6 == "1":
			return previousMenu()
		else:
			print("Please press 1 to return")
def noInternetMessage():
	print("No internet\nPlease connect your device to an internet source.")	

#---------------MENU
def mainMenu():
	selectBelow()
	listItemsIn(divisions)
	while True:
		choose2 = input()
		if choose2 == "1":
			theoMenu()
		elif choose2 == "2":
			practMenu()
		elif choose2 == "3":
			webLogic()
		elif choose2 == "4":
			exit()
		else:
			selectAbove()

def theoMenu():
	selectBelow()
	listItemsIn(theoretical)
	while True:
		choose3 = input()
		if choose3 == "1":
			return webmeta()
		elif choose3 == "2":
			return webepi()
		elif choose3 == "3":
			return mainMenu()
		else:
			selectAbove()
def practMenu():
	selectBelow()
	listItemsIn(practical)
	while True:
		choose4 = input()
		if choose4 == "1":
			webEthi()
		elif choose4 == "2":
			webAest()
		elif choose4 == "3":
			webSoci()
		elif choose4 == "4":
			webPoli()
		elif choose4 == "5":
			return mainMenu()
		else:
			selectAbove()

	
#----------------------------WEBSCRap
def getUrlPath(path):
	path = f"https://en.wikipedia.org/wiki/{path}"
	return path
def call(url):
	page = requests.get(url)
	doc = BeautifulSoup(page.text, "html.parser")
	return doc

def listWebfind(url):
	index = 1
	ol = url.find("ol")
	for li in ol.find_all('li'):
		print(f"{index}.", li.text)
		index +=1

def findH1(url):
	h1 = url.h1
	print(h1.text, "\n")

def findDiv(url,index1, index2):
	div = url.find("div", class_="vector-body")
	for paragraph in div.find_all("p")[index1:index2]:
		print(re.sub("[\[\\d\]]", '', paragraph.text))


def webmeta():
	try:
		metaurl = call(getUrlPath("Metaphysics"))
		findH1(metaurl)
		findDiv(metaurl, index1=2, index2=4)
		
		listWebfind(metaurl)
	except:
		noInternetMessage()
		backToThe(theoMenu)
	else:
		backToThe(theoMenu)
	
			
def webepi():
	try:
		epiurl = call(getUrlPath("Epistemology"))
		findH1(epiurl)
		findDiv(epiurl, index1=9, index2=11)
		listWebfind(epiurl)	
	except:
		noInternetMessage()
		backToThe(theoMenu)
	else:
		backToThe(theoMenu)

def webEthi():
	try:
		ethiurl = call(getUrlPath("Ethics"))
		findH1(ethiurl)
		findDiv(ethiurl, index1=2, index2=5)
		listWebfind(ethiurl)
	except:
		noInternetMessage()
		backToThe(practMenu)
	else:
		backToThe(practMenu)

def webAest():
	try:
		aesturl = call(getUrlPath("Aesthetics"))
		findH1(aesturl)
		findDiv(aesturl, index1=2, index2=5)
	except:
		noInternetMessage()
		backToThe(practMenu)
	else:
		backToThe(practMenu)
def webSoci():
	try:
		sociurl = call(getUrlPath("Social_philosophy"))
		findH1(sociurl)
		findDiv(sociurl, index1=1, index2=2)
	except:
		noInternetMessage()
		backToThe(practMenu)
	else:
		backToThe(practMenu)
def webPoli():
	try:
		poliurl= call(getUrlPath("Political_philosophy"))
		findH1(poliurl)
		findDiv(poliurl, index1=1, index2=6)
	except:
		noInternetMessage()
		backToThe(practMenu)
	else:
		backToThe(practMenu)

def webLogic():
	try:
		logicurl= call(getUrlPath("Logic"))
		findH1(logicurl)
		findDiv(logicurl, index1=2, index2=3)
	except:
		noInternetMessage()
		backToThe(mainMenu)
	else:
		backToThe(mainMenu)


def start():
	print("+-------------------------------------+")
	print("|  Welcome to Philosophy Class 101    |")
	print("+-------------------------------------+")
	print("\n   To continue please select y/n")
	while True:
		choose1 = input()
		if choose1.lower() == "y":
			mainMenu()
		elif choose1.lower() == 'n':
			print("Maybe next class")
			break
		else:
			print("Please press y/n")
def main():
	start()

if __name__ == "__main__":
	start()

