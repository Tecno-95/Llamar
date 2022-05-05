# by Tecno-95

import colorama
from colorama import Fore
import subprocess
import time



# Función de llamada

def call():
    numero = input(Fore.BLUE + "[+]Número de Télefono: ")
    
    subprocess.call("termux-telephony-call {} ".format(numero),shell=True)

    time.sleep(3)

    print(Fore.GREEN + "[+]Llamando...")

call()

