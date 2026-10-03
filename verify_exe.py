import subprocess
import time
import os

exe_path = os.path.join("dist", "RockPaperScissors.exe")
p = subprocess.Popen([exe_path])
time.sleep(5)
ret = p.poll()
if ret is None:
    print("EXE is RUNNING (PID", p.pid, ") - OK")
    p.terminate()
    try:
        p.wait(timeout=5)
    except subprocess.TimeoutExpired:
        p.kill()
    print("Terminated test process.")
else:
    print("EXE EXITED with code", ret)
