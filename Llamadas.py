# by Tecno-95

import subprocess
import time

numero = input("[+]Numero de télefono: ")
subprocess.call("termux-telephony-call {}".format(numero),shell=True
time.sleep(3)
print("\u001b[32;1m[+]Llamando...")
