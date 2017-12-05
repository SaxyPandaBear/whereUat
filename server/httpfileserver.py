import pyipinfoio
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Ready to serve...')

while True:
	
	print('\n\nWaiting..')
	connectionSocket, addr = serverSocket.accept()
	print 'Connection from ',addr

	ff = open("IP.txt","a")
	t = str(addr)
	t = t[1:t.find(',')].strip('\'')
	#print('ip address:  ', t)
	
	ip = pyipinfoio.IPLookup()  # get info on IP
	varr = ip.lookup(t, 'loc')  # look specifically for the location information
        ff.write(varr+'\n')
	
	#print(varr)
        ff.close()
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
