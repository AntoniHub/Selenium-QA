import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--incognito')
options.add_argument('--start-maximized')


#Open HomePage
@given('User with a valid ID and Pass')
def test_01_openHome(context):
    """Abrimos el navegador, el ambiente de TEST y maximixamos la ventana"""
    context.driver = webdriver.Chrome()
    context.driver.get('https://es-testing.cyberguardian.tech/home')
    context.driver.maximize_window()
    assert 'Cyber Guardian' in context.driver.title
    time.sleep(1)
    #driver.save_screenshot('image.png')

    #Close cookies
    """Identificamos la configuracion de cookies a traves de XPATH para cerrarlo"""
    cookies = context.driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
    cookies.click()
    time.sleep(0.5)

    #View Inicio
    """Hacemos click en Inicio"""
    inicio = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[1]/p[1]')
    inicio.click()
    time.sleep(0.5)

    #View Funcionalidades
    """Hacemos click en funcionalidades"""
    funcionalidades = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[1]/p[2]')
    funcionalidades.click()
    time.sleep(0.5)

    #View consiguelo
    """Hacemos click en consiguelo"""
    consiguelo = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[1]/p[3]')
    consiguelo.click()
    time.sleep(0.5)

@when('Click on LogIn')
def test_06_LogIn(context):
    """Hacemos click en el LogIn a traves de del atributo CLASS"""
    logIn = context.driver.find_element(By.CLASS_NAME, 'css-u6po9p')
    context.driver.execute_script("arguments[0].scrollIntoView();", logIn)
    logIn.click()
    time.sleep(1)

    #Send mail
    """Ingresamos la direccion de EMail"""
    mail = context.driver.find_element(By.ID,'businessEmail')
    mail.click()
    time.sleep(0.2)
    mail.send_keys('testcyberguardian@gmail.com')
    time.sleep(0.2)

    #Send password
    """Ingresamos el password"""
    password = context.driver.find_element(By.ID,'password')
    password.click()
    time.sleep(0.2)
    password.send_keys('T3st.4321')
    time.sleep(0.2)

@then('Successfully log in to Cyber Guardian at /client')
def test_successfullyLogIn(context):
    #Start session
    """Hacemos click en iniciar session"""
    start = context.driver.find_element(By.ID,'emailButton')
    start.click()
    time.sleep(8)


    #Close driver
    """Cerramos el driver"""
    context.driver.quit()