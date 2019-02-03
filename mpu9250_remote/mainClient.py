import tcp_client as tcp 
import time
import mpu9250 as mpu

''' Script to send  all'''

mpu = mpu.MPU9250()
Client = tcp.tcpClient('192.168.1.36',60000)

Client.connect()

while True:

    data = mpu.readAll()
    Client.sndPack(data)
    time.sleep(0.1) 