# Cairometer (C) 2013 by Omar N. Metwally
# This script mines Twitter data using API v. 1.1 to 
# count the number of tweets featuring political keywords
# as functions of latitutde and longitude and plots them over time
# Permission is granted for anyone to copy, use, modify or distribute
# this program and accompanying programs and documents for any purpose,
# provided this copyright notice is retained and prominently displayed,
# along with a note saying that the original programs are available at this
# webpage. The programs are documents are distributed without warranty,
# express or implied. As the programs were written for research purposes, 
# they have not been tested to the degree that would be advisable in any
# important application. All use of these programs is entirely at the
# user's own risk.
# The 'Request' function was written by Matt Griffiths. See the accompanying
# file 'fxn.py' for details.
# This script utilizes the matplotlib library. For copyright details
# visit matplotlib.org

import urllib, datetime
from fxn import Request
import json
from pylab import *

# define consumer key and consumer secret prior to use:
consumer_key = ''
consumer_secret = ''

# query term 
print "Enter tweet query term: "
query_term = raw_input()
print "Enter latitude (eg. 30): "
latitude = raw_input()
print "Enter longitude (eg. 31.2): "
longitude = raw_input()
print "Enter radius in miles (eg. 14): "
radius = raw_input()
radius = str(radius)

# get last 7 dates and use them for twitter API v. 1.1 queries
# Note that the number of results returned is capped at 100
today = datetime.date.today()
delta = datetime.timedelta(1)

dates = []
values = []
dates.append(today+delta)

print "The date today is ",today.__str__()
print "The last 7 dates will be used to query the Twitter API.\n"

i = 0
while i < 8:
	temp = today-(delta*i)
	dates.append(temp)

	i+=1
		
num_dates = len(dates)

i=num_dates-2

# xvals and yvals are lists that hold the dates and number of tweets
# for plotting
xvals = []
yvals = []

while i > 0:

	since_date = dates[i].__str__()
	until_date = dates[i-1].__str__()

	request, response = Request(
	    'https://api.twitter.com/1.1/search/tweets.json?q='+query_term+'&count=1000&geocode='+latitude+','+longitude+','+radius+'mi&since='+since_date+'&until='+until_date,consumer_key,consumer_secret)

	data = json.loads(response)
	tweets = data['statuses']
	yvals.append(len(tweets))

	xvals.append(dates[i].day)

	print since_date+' '+str(len(tweets))

	i-=1

print "Plotting number of tweets vs date (requires matplotlib)..."
print "Close bar graph's window to exit."
bar(xvals,yvals)
show()


