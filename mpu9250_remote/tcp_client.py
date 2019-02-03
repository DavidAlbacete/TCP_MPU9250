
import socket
import time
import pickle

'''Class for send numeric information over a tcp connection '''

class  tcpClient:

	##Constructor
	# @Param [in] self The object pointer.
	# @Param [in] server's ip
	# @Param [in] server's port
	def __init__(self,ip_server,port_server):
		
		self.ip_server = ip_server
		self.port_server = port_server
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		time.sleep(0.1)
		print("socket created")
	
	## Setting a connection to the server 
	# @Param [in] self The object pointer
	def connect(self):

		try:
			print('host = ' + socket.gethostname())
			self.s.connect((self.ip_server,self.port_server))
			print("connection done")
		except socket.error as msg:
			print(msg)
			
	## Encode and data
	# @Param [in] self The object pointer
	# @Param [in] data
	def sndPack(self,notEnCodData):

		try:
			print(str(notEnCodData))
			codeData = pickle.dumps(notEnCodData)
			self.s.send(codeData)
			print("data send")
		except socket.error as msg:
			print(msg)

	






