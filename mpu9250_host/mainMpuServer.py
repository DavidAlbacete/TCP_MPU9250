import storage
import time
''' script to work with information receive '''

storage = storage.storage()
storage.start()

print(' ')
print(' STORAGE SET ')
print(' ')

## acquire read lock from storage
def acquire():

	storage.lock.acquire_read()

## release read
def release():
	
	storage.lock.release_read()

##  read accelerometer data
def getAcc():

	return storage.a

## read gyroscope data
def getGyr():

	return storage.g
	
##read magnetometer data
def getMag():

	return storage.m
## read temperature
def getTem():

	return storage.t

while True:

	acquire()
	a = getAcc()
	g = getGyr()
	m = getMag()
	t = getTem()
	release()

	print ('accel' + ' ' + str(a))
	print ('gyr' + ' ' + str(g))
	print ('magnet' + ' '+ str(m))
	print ('temp' + ' ' + str(t))

	time.sleep(0.1)