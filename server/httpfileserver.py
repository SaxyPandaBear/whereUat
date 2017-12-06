import pyipinfoio
from socket import *
import sys # In order to terminate the program
import sqlite3


# takes geographic information from IPInfo, and opens the IP file.
# if the new location is not already in our file, we add it.
# otherwise, nothing happens
# def log_location(loc):
# 	f = open("IP.txt", "a")
# 	locs = f.read().splitlines()
# 	if loc in locs:
# 		f.write(loc + '\n')
# 	f.close()

serverSocket = socket(AF_INET, SOCK_STREAM)

# create a connection to a SQLite Database
db = sqlite3.connect('whereuat.sqlite3')  # database data stored in 'whereuat.sqlite3'
db.row_factory = sqlite3.Row  # https://docs.python.org/2/library/sqlite3.html#row-objects

# our table will be defined as follows
# IP: The IP that was logged									|	ip		= text
# Host: The host of the source IP								|	host	= text
# City: The name of the city of origin							|	city	= text
# Country : The 2 digit ISO code for the country of origin		|	country	= text
# Latitude: The latitude for the location of the IP				|	lat		= real
# Longitude: The longitude for the location of the IP			|	lng		= real
# Frequency: The number of times this particular IP has 		|	freq	= integer
# 				 logged in to our server.

# if the table doesn't already exist, 
db.execute('CREATE TABLE IF NOT EXISTS ipdata (ip TEXT, host TEXT, city TEXT, country TEXT, lat REAL, lng REAL, freq INTEGER)')

def insert_to_db(data):
	# first check if this IP has already been stored in our database
	ip = str(data['ip'])
	cursor = db.cursor()
	cursor.execute('SELECT freq FROM ipdata')
	row = cursor.fetchone()
	if row is not None:
		# a value was returned from the database with the given IP, so instead of inserting
		# we just update the frequency of this row in the database.
		freq = row['freq'] + 1
		db.execute('UPDATE ipdata SET freq=? WHERE ip=?', (freq, ip))
	else:
		# insert row into the db if the ip is new
		host = str(data['hostname'])
		city = str(data['city'])
		country = str(data['country'])
		geo = str(data['loc']).split(',')
		lat = float(geo[0])
		lng = float(geo[1])
		freq = 1  # a new row always starts with a frequency of 1
		values = (ip, host, city, country, lat, lng, freq)  # make a tuple of the data to insert
		db.execute('INSERT INTO ipdata VALUES (?,?,?,?,?,?,?)', values)
	# save whatever we just changed in the database
	db.commit()

# IMPORTANT: ipinfo relies on the 'curl' command, which does not exist on Windows machines
# In order for this to work, the script must be run on a Unix / Linux box.
ipLookup = pyipinfoio.IPLookup()  # get info on IP
# example output of a lookup - in this API wrapper, values are stored in a dictionary
# {
#   "ip": "8.8.8.8",
#   "hostname": "google-public-dns-a.google.com",
#   "loc": "37.385999999999996,-122.0838",
#   "org": "AS15169 Google Inc.",
#   "city": "Mountain View",
#   "region": "California",
#   "country": "US",
#   "phone": 650
# }

#Prepare a sever socket
serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Ready to serve...')

while True:
	
	print '\n\nWaiting..'
	connectionSocket, addr = serverSocket.accept()
	print 'Connection from ',addr

	address = str(addr)
	address = t[1:t.find(',')].strip('\'')
	
	# location = ip.lookup(t)  # look specifically for the location information
	ipinfo = ipLookup.lookup(address)
	insert_to_db(ipinfo)  # let the function take care of all of the heavy lifting

	# if location_is_logged(location):
	# 	with open("IP.txt", "a") as f:
	# 		f.write('%s\n' % location)
	
	try:
		message = connectionSocket.recv(1024)
		
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		f.close()
		#Send one HTTP header line into socket
		
		connectionSocket.send('HTTP/1.1 200 OK\n')
		connectionSocket.send('Connection: close\n')
		length = 'Content-Length: '+str(len(outputdata))+'\n'
		connectionSocket.send(length)
		connectionSocket.send('Content-Type: text/html\n')
		connectionSocket.send('\n')
		#connectionSocket.send('\n')
		connectionSocket.send(outputdata)
		#Send the content of the requested file to the client
		
		print('Data retrieved successfully')
		
		connectionSocket.close()
	except IOError:
                print('FILE NOT FOUND: '+filename)
		#Send response message for file not found
                connectionSocket.send('\HTTP/1.1 404 Not Found\n')
                connectionSocket.send('\n')
                errormessage = "404 Not Found: "+filename+'\n'
		connectionSocket.send(errormessage)
		
		connectionSocket.close()
	except (IndexError, SyntaxError):  # not sure what propogates these errors
		print('We B O K E')
	except KeyboardInterrupt:
		# the script waits on a keyboard interrupt, CTRL+C, so
		# on interrupt, close our connections
		serverSocket.close()
		ipLookup.close()
		db.close()
		connection.close()
sys.exit()
