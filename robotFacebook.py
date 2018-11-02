#imports para controlar o web w o tempo de execução
from selenium import webdriver
import time

#variaveis para email e senha (sera automatizado quando for criado a tela)
usr = 'your_email'
pwd = 'yout_password'


#Driver para conectar ao chrome
drive = webdriver.Chrome("C:\chromedriver.exe")

#abre o site
drive.get('http://facebook.com')

#envia via POST o email e senha
username_box = drive.find_element_by_id("email")
username_box.send_keys(usr)

time.sleep(1)

password_box = drive.find_element_by_id('pass')
password_box.send_keys(pwd)

#pressiona o botao para entrar
login_box = drive.find_element_by_id('loginbutton')
login_box.click()

#import para enviar a tecla "ESC" para sumir o popup de notificação
import pyautogui

time.sleep(2)
pyautogui.press("esc")

#Daqui para baixo a rolagem da página de forma automática, será controloado por botões na confecção das telas
control = 1
start = 250
while control > 0:
    #drive.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);window.scrollTo(0, document.body.scrollHeight/%f);"%(start,end))
    drive.execute_script("scrollBy(0,%s);"% start)
    start = start + 1
    time.sleep(1)

#Desenvolvido por LeandroSouza



