import time
import GPUtil

while True:
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        print(f"GPU ID: {gpu.id}, GPU Load: {gpu.load*100}%, Memory Free: {gpu.memoryFree}MB, Memory Used: {gpu.memoryUsed}MB, Temperature: {gpu.temperature} °C")
    time.sleep(3)  # 3초 대기 후 다시 실행
