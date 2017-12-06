import pyipinfoio
from socket import *
import sys # In order to terminate the program


# takes geographic information from IPInfo, and opens the IP file.
# if the new location is not already in our file, we add it.
# otherwise, nothing happens
def log_location(loc):
	f = open("IP.txt", "a")
	locs = f.read().splitlines()
	if loc in locs:
		f.write(loc + '\n')
	f.close()

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Ready to serve...')

while True:
	
	print '\n\nWaiting..'
	connectionSocket, addr = serverSocket.accept()
	print 'Connection from ',addr

	t = str(addr)
	t = t[1:t.find(',')].strip('\'')
	#print('ip address:  ', t)
	
	# IMPORTANT: ipinfo relies on the 'curl' command, which does not exist on Windows machines
	# In order for this to work, the script must be run on a Unix / Linux box.
	ip = pyipinfoio.IPLookup()  # get info on IP
	location = ip.lookup(t, 'loc')  # look specifically for the location information

	if location_is_logged(location):
		with open("IP.txt", "a") as f:
			f.write('%s\n' % location)
	
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
		
serverSocket.close()

sys.exit()
