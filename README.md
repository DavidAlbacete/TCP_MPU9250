DAVID ALBACETE SEGURA 
This project is for interfacing a mpu9250 from your computer 
using a tcp connection between your computer and a raspberry pi(
wich uses a i2c protocol to read from the mpu)

You have to run in the raspberry  the mainClient.py script and 
in your computer the mainMpuServer.py

I'm using the Fabo9axis library to read from the mpu 
link : https://github.com/FaBoPlatform/FaBo9AXIS-MPU9250-Python
and also  the srcipt described here to control the threads' 
interactions
link: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch06s04.html



