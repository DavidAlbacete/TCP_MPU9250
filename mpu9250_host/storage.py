import tcpServer as tcp
import threading
import threadProct1N as th
import time

''' Class to receive the information received from the tcp connection and storage '''
class storage(threading.Thread): 

	## Constructor
	# @Param [in] self The object pointer
	 def __init__(self):

	 	threading.Thread.__init__(self)
	 	self.lock = th.ReadWriteLock()

	 	self.tcpConn = tcp.tcpServer('192.168.1.36', 60000)

	 	self.a = (0 ,0 ,0 )
	 	self.g = (0 ,0 ,0 )
	 	self.m = (0 ,0 ,0 )
	 	self.t = 0

	 ## Updating the stored values
	 # @Param [in] self The object pointer
	 # @Param [in] accelerometer data
	 # @Param [in] gyroscope data
	 # @Param [in] magnetometer data
	 # @Param [in] temperature
	 def update(self, a, g, m, t):
	 	
	 	self.a = a
	 	self.g = g
	 	self.m = m
	 	self.t = t

	 ## Separating the received data (you have to know how is sent the inormation)
	 # it is not autonomus from the sender
	 # @Param [in] self The object pointer
	 # @Param [in] data to separate 
	 def separate(self, data):
 
	 	a = data[0]
	 	g = data[1]
	 	m = data[2]
	 	t = data[3]

	 	return a, g, m, t
	 	
	 ## run method
	 # @Param [in] self The object pointer
	 def run(self):

	 	while True:

	 		data = self.tcpConn.rcvPack()
	 		a,g,m,t = self.separate(data)

	 		self.lock.acquire_write()
	 		self.update(a,g,m,t)
	 		self.lock.release_write()

	 		time.sleep(0.1)


