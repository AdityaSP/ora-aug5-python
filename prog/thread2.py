import time
import threading

a = 0

def consumer():
    for i in range(5):
        time.sleep(5)
        e.wait()
        print(a)
        e.clear()
        
def producer():
    global a
    for i in range(5):
        time.sleep(10)
        a += 100
        e.set()
        
e = threading.Event()

  
prod = threading.Thread(target=producer)
con = threading.Thread(target=consumer)
st = time.time()
prod.start()
con.start()
prod.join()
con.join()
et = time.time()
print("Took", et-st)
