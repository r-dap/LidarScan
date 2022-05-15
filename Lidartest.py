import PyLidar3
import time
port = "com6" #windows
Obj = PyLidar3.YdLidarX4(port)
if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time()
    while(time.time()-t)<10: 
        v1 = next(gen)
        print(v1) #這邊回傳lidar 角度與距離(m)
   
    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")
