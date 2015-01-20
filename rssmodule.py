#!/usr/bin/env python3

import urllib.request
import emailmodule
import re
import time

#User Options

#Add mailng details here:
receiver = "example@example.com"
sender = "Myself"

#Add RSS feeds here:
rssfeeds = [
"http://feeds.bbci.co.uk/news/rss.xml",
"http://rss.slashdot.org/Slashdot/slashdot",
"http://www.aljazeera.com/Services/Rss/?PostingId=2007731105943979989"
]

#Main Function

emailbody = "<html><head><style>img {width: 300px} body {color: black; font-size: 14px;}</style></head><body>"

for feeds in rssfeeds:

	feedunparsed = urllib.request.urlopen(feeds)

	feed = str(feedunparsed.read())

	itemlist = []

	for i in re.finditer('<item>', feed):
		itemlist.append(i.end())

	for i in re.finditer('</item>', feed):
		itemlist.append(i.start())

	itemlist.sort()

	for index, i in enumerate(itemlist):
		if (not(index % 2 == 0)):
			continue

		start = i
		end = itemlist[index+1]

		item = feed[start:end]
		
		titlebegin = item.find("<title>") + 7
		titleend = item.find("</title>")
		titleun = item[titlebegin:titleend]
		title = titleun.replace("\\", "")

		linkbegin = item.find("<link>") + 6
		linkend = item.find("</link>")
		link = item[linkbegin:linkend]

		desbegin = item.find("<description>") + 13
		desend = item.find("</description>")
		desun = item[desbegin:desend]
		desu = desun.replace("\\", "")

		if desu.find("&lt;") != -1:
			des = desu[0:desu.find("&lt;")]

		else:
			des = desu


		emailbody += "<a style = 'font-size: 20px; text-decoration:none;' href = '" + link + "'>" + title + "</a><br>"
		emailbody += "<p style = 'color:black;'>" + des + "</p><br>"
		
emailbody += "</body></html>"

subject = "News for " + time.strftime("%c")

emailmodule.main(receiver, sender, subject, emailbody, "html")

