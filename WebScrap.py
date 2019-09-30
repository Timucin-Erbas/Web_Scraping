# --------------------------------------------------------------------
# Author: Timucin Erbas
# Date: Sep 14 2019 
# --------------------------------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
f = open("Car_Info.tsv", "w")

wantedlinks = set()
detailedcodes = []

for i in range (1,51,1):
	page = urlopen("https://www.arabam.com/ikinci-el?searchText=otomobil&page=" + str(i))
	code = BeautifulSoup(page, features = "html.parser")
	table = code.find("tbody")
	links = table.findAll("a")
	print(i)
	for j in links:
		wantedlink = j["href"]
		wantedlinks.add(wantedlink)

print("-------------------------------------------------")
print("count: " + str(len(wantedlinks)))

for i in wantedlinks:
	detcode = urlopen("https://www.arabam.com" + str(i))
	detailedcode = BeautifulSoup(detcode , features = "html.parser")
	detailedcodes.append(detailedcode)
	print(i)

print("--------------------------------------------------")
print("detailed codes length: " + str(len(detailedcodes)))

for i in range (0, len(detailedcodes), 1):
	print(i)
	carinformation = {}
	keyword = ""
	program = detailedcodes[i]
	pricegram = program.find("span", attrs = {"class" : "color-red4 font-semi-big bold w66 fl"})
	price = pricegram.getText()
	placegram = program.find("p", attrs = {"class" : "one-line-overflow font-default-minus pt4 color-black2018 bold"})
	place = placegram.getText()
	table = program.find("ul", attrs = {"class" : "w100 cf mt16"})
	table_elems = table.findAll("li")
	carinformation["place"] = place
	carinformation["price"] = price

	for elem in table_elems:
		splitelem = elem.getText().split(":")
		if splitelem[0] != "Motor Gücü":
			carinformation[splitelem[0]] = splitelem[1]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	for info in carinformation:
		f.write(str(carinformation[info]) + "	")
		print(info)
	f.write("\n")
f.close()




