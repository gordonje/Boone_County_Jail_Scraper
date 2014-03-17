import urllib2
from BeautifulSoup import BeautifulSoup
import csv

# The target webpage
url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
# Loads all the HTML from the page into a variable, first opening it, and then reading it into the variable
html = urllib2.urlopen(url).read()
# Put all of the HTML into a 'blender'.
soup = BeautifulSoup(html)
# targeting mechanism, identifying what you want
results_table = soup.find('table', attrs = {'class': 'resultsTable'})
# create a variable for the row we are outputting
output_trs = []
# loop through all of the rows...
for tr in results_table.findAll('tr'):
	tds = tr.findAll('td')

	output_tds = []

	for td in tds:
		output_tds.append(td.text.replace('&nbsp;', ''))

	output_trs.append(output_tds)

outfile = open('inmates.csv', 'a')
write_the_file = csv.writer(outfile)

write_the_file.writerows(output_trs)