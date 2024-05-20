import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--start-maximized')

"""Test E2E de la seccion Seguridad Interna en la pagina 
https://es-testing.cyberguardian.tech/client/device-security"""

@given('User in the Cyber Guardian application who wants to check the status of his protections')
def test_01_openHome(context):
    """Abrimos el driver, la web en ambiente de TEST y maximizamos la ventana"""
    context.driver = webdriver.Chrome()
    context.driver.get('https://es-testing.cyberguardian.tech/home')
    context.driver.maximize_window()
    assert 'Cyber Guardian' in context.driver.title
    time.sleep(1)

    # Close configuracion de cookies
    """Cerramos la configuracion de cookies"""
    cookies = context.driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
    cookies.click()
    time.sleep(0.5)

    # Click on LogIn
    """Hacemos click en el LogIn"""
    logIn = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[2]/button[1]/div')
    context.driver.execute_script("arguments[0].scrollIntoView();", logIn)
    logIn.click()
    time.sleep(1)

    # Send mail
    """Ingresamos la direccion de Email"""
    mail = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/input')
    mail.click()
    time.sleep(0.2)
    mail.send_keys('testcyberguardian@gmail.com')
    time.sleep(0.2)

    # Send password
    """Ingresamos password"""
    password = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[3]/input')
    password.click()
    time.sleep(0.2)
    password.send_keys('T3st.4321')
    time.sleep(0.2)

    # Start session
    """Hacemos click en iniciar session"""
    start = context.driver.find_element(By.ID,'emailButton')
    start.click()
    time.sleep(8)


@when('Click on Protections')
def test_07_Proteccion(context):
    """Hacemos click en la seccion Proteccion -> Controla tu seguridad interna"""
    proteccion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/span/div')
    proteccion.click()
    time.sleep(2)

@then('It will display each of the sections and you will be able to navigate between them')
def test_viewProtection(context):
    """Hacemos click en el sub item de menu Seguridad de Dispositivos"""
    seguridadDispositivos = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[1]/span')
    seguridadDispositivos.click()
    time.sleep(2)

    """Hacemos click para ver el tutorial de Seguridad de Dispositivos"""
    verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
    verTutorial.click()
    time.sleep(1.5)

    """Hacemos click en siguiente para avanzar en la lectura del tutorial"""
    siguienteTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
    siguienteTutorial.click()
    time.sleep(0.5)

    siguienteTutorial.click()
    time.sleep(0.5)

    siguienteTutorial.click()
    time.sleep(0.5)

    """Hacemos click en Estoy Listo despues de terminar el tutorial de Seguridad de Dispositivos"""
    estoyListo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
    estoyListo.click()
    time.sleep(2)

    """Hacemos click para ver el tutorial de Seguridad de Dispositivos"""
    verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
    verTutorial.click()
    time.sleep(1.5)

    """Hacemos click en Saltar tutorial"""
    saltarTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
    saltarTutorial.click()
    time.sleep(1)

    """Hacemos click en el item de menu Amenazas Gestionadas"""
    proteccion = context.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/span/div')
    proteccion.click()
    time.sleep(1.5)

    amenazasGestionadas = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[2]/span')
    amenazasGestionadas.click()
    time.sleep(2)

    """Hacemos click en la seccion Seguridad de Buzones de Seguridad de Dispositivos"""
    proteccion = context.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/span/div')
    proteccion.click()
    time.sleep(1.5)

    seguridadBuzones = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[3]/span')
    seguridadBuzones.click()
    time.sleep(2)


    """Hacemos click en el sorTable para expandir"""
    sorTable = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div')
    sorTable.click()
    time.sleep(1)

    sorTable.click()
    time.sleep(1)

    """Hacemos click en el tutorial de la seccion de Seguridad de Buzones"""
    videoTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
    videoTutorial.click()
    time.sleep(1.5)

    """Hacemos click en siguiente para terminar el video tutorial de Seguridad de Buzones"""
    siguiente = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
    siguiente.click()
    time.sleep(0.8)

    siguiente.click()
    time.sleep(0.8)

    siguiente.click()
    time.sleep(0.8)

    """HAcemos click en estoy listo del video tutorial de Seguridad de Buzones"""
    estoyListo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
    estoyListo.click()
    time.sleep(2)

    """Hacemos click en el tutorial de la seccion de Seguridad de Buzones
    Ahora para probar el boton de Saltar tutorial"""
    videoTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
    videoTutorial.click()
    time.sleep(1.5)

    """Hacemos click en saltar tutorial de Seguridad de Buzones"""
    saltarTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
    saltarTutorial.click()
    time.sleep(1.5)


    """Hacemos click en Contacta con soporte"""
    contactaSoporte = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[3]/div/div')
    contactaSoporte.click()
    time.sleep(1.5)

    contactaSoporte.click()
    time.sleep(1.5)

    """Cerramos el driver"""
    context.driver.quit()