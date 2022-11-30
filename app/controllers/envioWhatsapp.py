from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from app.models.tables import Pessoa
import random
import time
import urllib

def enviar_senha_whatsapp(cpf):
    pessoa = Pessoa.query.filter_by(cpf=cpf).first()

    driver_service = Service(executable_path="/usr/lib/chromium-browser/chromedriver")

    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://web.whatsapp.com/")

    time.sleep(100)

    senha =random.randint(0,999)
    nome = pessoa.nome
    numero = '55'+str(pessoa.numero_cel)
    mensagem = "Sua senha é A" + str(senha)
    text = urllib.parse.quote(f"Olá {nome}! {mensagem}")

    link = f"https://web.whatsapp.com/send?phone={numero}&text={text}"
    driver.get(link)
    time.sleep(40)

    driver.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')[0].send_keys(Keys.ENTER)
    time.sleep(10)

