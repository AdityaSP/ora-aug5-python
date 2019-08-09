import time
import threading

def heavyduty(i):
    print("Started ", i)
    print(threading.current_thread().getName())
    time.sleep(5)
    print("Finished ", i)
    
#heavyduty(1)
#heavyduty(2)
#heavyduty(3)
#heavyduty(4)
#heavyduty(5)

#t1 = threading.Thread(target=heavyduty, args=[1])
#t2 = threading.Thread(target=heavyduty, args=[2])
#t3 = threading.Thread(target=heavyduty, args=[3])
#t4 = threading.Thread(target=heavyduty, args=[4])
#t5 = threading.Thread(target=heavyduty, args=[5])
#
#t1.start()
#t2.start()
#t3.start()
#t4.start()
#t5.start()
print(threading.current_thread().getName())
for i in range(5):
    threading.Thread(target=heavyduty, name = "MyT-"+ str(i), args=[i]).start()