import time
import socket
import threadProct1N as th
import pickle

''' tcp server to receive information'''

class tcpServer:
	
	##Constructor
	# @Param [in] self The object pointer
	# @Param [in] server's ip
	# Param [in] server's port
	def __init__(self,host,port):

		self.host = host
		self.port = port

		self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set()

	## Set connection
	# @Param [in] self The object pointer
	def set(self):

		self.s.bind((self.host,self.port))
		self.s.listen(1)
		self.conn,self.addr = self.s.accept()
		print('binding complete')
		
		
		
		
	
	## Receive one packet
	# @Param [in] self The object pointer
	# @Param [out] information decoded
	def rcvPack(self):

		data = self.conn.recv(4096)
		arr = pickle.loads(data)
		return arr





