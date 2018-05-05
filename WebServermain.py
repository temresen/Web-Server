from socket import *

#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 1234

serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
	#Establish the connection
	print("Ready to serve...")

	connectionSocket, addr = serverSocket.accept()

	try:
		message = connectionSocket.recv(1024)
		#print(message)
		filename = message.split()[1]
		print(filename)              
		f = open(filename[1:])                        

		outputdata = f.read()

		#Send one HTTP header line into socket
		connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")	

		print("Server is running on :" +gethostname()+" with port number "+str(serverPort))

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):           
			connectionSocket.send(bytes(outputdata[i].encode()))
		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found
		connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
		connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
		# Close the client connection socket
		connectionSocket.close()

serverSocket.close() 