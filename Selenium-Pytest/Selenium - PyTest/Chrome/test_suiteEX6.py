import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


options = Options()
options.add_argument('--start-maximized')
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = {'browser':'ALL'}
driver = webdriver.Chrome(chrome_options=options, executable_path='C:/AntonioRodriguez/ChromeDriver/chromedriver.exe', desired_capabilities=dc)
time.sleep(0.5)


"""Test E2E de la seccion Seguridad Interna en la pagina"""

@pytest.mark.feature("SetUp")
class TestHomePage:
    def test_01_openHome(self):
        """Abrimos el driver, la web en ambiente de TEST y maximizamos la ventana"""
        driver.get('https://antonio-rodriguez.tech')
        driver.maximize_window()
        assert 'Antonio Rodriguez' in driver.title
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    # Close configuracion de cookies
    def test_02_closeCookies(self):
        """Cerramos la configuracion de cookies"""
        cookies = driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
        cookies.click()
        time.sleep(0.5)

@pytest.mark.feature("LogIn")
class TestLogIn:
    # Click on LogIn
    def test_03_LogIn(self):
        """Hacemos click en el LogIn"""
        logIn = driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[2]/button[1]/div')
        driver.execute_script("arguments[0].scrollIntoView();", logIn)
        logIn.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    # Send mail
    def test_04_sendMail(self):
        """Ingresamos la direccion de Email"""
        mail = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/input')
        mail.click()
        time.sleep(0.2)
        mail.send_keys('abgrodriguezfarias@gmail.com')
        time.sleep(0.2)

    # Send password
    def test_05_sendPass(self):
        """Ingresamos password"""
        password = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[3]/input')
        password.click()
        time.sleep(0.2)
        password.send_keys('T3st.4321')
        time.sleep(0.2)

    # Start session
    def test_06_startSession(self):
        """Hacemos click en iniciar session"""
        start = driver.find_element(By.ID,'emailButton')
        start.click()
        time.sleep(8)

        for e in driver.get_log('browser'):
            print(e)

@pytest.mark.feature("Proteccion")
class TestProteccion:
    def test_07_Proteccion(self):
        """Hacemos click en la seccion Proteccion -> Controla tu seguridad interna"""
        proteccion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/span/div')
        proteccion.click()
        time.sleep(2)

        for e in driver.get_log('browser'):
            print(e)


    def test_08_seguridadDispositivos(self):
        """Hacemos click en el sub item de menu Seguridad de Dispositivos"""
        seguridadDispositivos = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[1]/span')
        seguridadDispositivos.click()
        time.sleep(2)

        for e in driver.get_log('browser'):
            print(e)

    def test_09_verTutorial(self):
        """Hacemos click para ver el tutorial de Seguridad de Dispositivos"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

    def test_10_siguienteTutorial(self):
        """Hacemos click en siguiente para avanzar en la lectura del tutorial"""
        siguienteTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
        siguienteTutorial.click()
        time.sleep(0.5)

        siguienteTutorial.click()
        time.sleep(0.5)

        siguienteTutorial.click()
        time.sleep(0.5)

    def test_11_estoyListo(self):
        """Hacemos click en Estoy Listo despues de terminar el tutorial de Seguridad de Dispositivos"""
        estoyListo = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
        estoyListo.click()
        time.sleep(2)

    def test_12_verTutorial(self):
        """Hacemos click para ver el tutorial de Seguridad de Dispositivos"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1.5)

    def test_13_saltarTutorial(self):
        """Hacemos click en Saltar tutorial"""
        saltarTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
        saltarTutorial.click()
        time.sleep(1)

@pytest.mark.feature("AmenazasGestionadas")
class TestAmenazasGestionadas:
    def test_18_amenazasGestionadas(self):
        """Hacemos click en el item de menu Amenazas Gestionadas"""
        proteccion = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/span/div')
        proteccion.click()
        time.sleep(1.5)

        amenazasGestionadas = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[2]/span')
        amenazasGestionadas.click()
        time.sleep(2)

        for e in driver.get_log('browser'):
            print(e)

@pytest.mark.feature("SeguridadBuzones")
class TestMailboxSecurity:
    def test_19_seguridadBuzones(self):
        """Hacemos click en la seccion Seguridad de Buzones de Seguridad de Dispositivos"""
        proteccion = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/span/div')
        proteccion.click()
        time.sleep(1.5)

        seguridadBuzones = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[3]/span')
        seguridadBuzones.click()
        time.sleep(2)

        for e in driver.get_log('browser'):
            print(e)

    def test_20_sorTable(self):
        """Hacemos click en el sorTable para expandir"""
        sorTable = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div')
        sorTable.click()
        time.sleep(1)

        sorTable.click()
        time.sleep(1)

    def test_21_verTutorial(self):
        """Hacemos click en el tutorial de la seccion de Seguridad de Buzones"""
        videoTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
        videoTutorial.click()
        time.sleep(1.5)

    def test_22_siguiente(self):
        """Hacemos click en siguiente para terminar el video tutorial de Seguridad de Buzones"""
        siguiente = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
        siguiente.click()
        time.sleep(0.8)

        siguiente.click()
        time.sleep(0.8)

        siguiente.click()
        time.sleep(0.8)

    def test_23_estoyListo(self):
        """HAcemos click en estoy listo del video tutorial de Seguridad de Buzones"""
        estoyListo = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
        estoyListo.click()
        time.sleep(2)

    def test_24_verTutorial(self):
        """Hacemos click en el tutorial de la seccion de Seguridad de Buzones
        Ahora para probar el boton de Saltar tutorial"""
        videoTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
        videoTutorial.click()
        time.sleep(1.5)

    def test_25_saltarTutorial(self):
        """Hacemos click en saltar tutorial de Seguridad de Buzones"""
        saltarTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
        saltarTutorial.click()
        time.sleep(1.5)

@pytest.mark.feature("Footer")
class TestFooter:
    def test_26_contactaSoporte(self):
        """Hacemos click en Contacta con soporte"""
        contactaSoporte = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[3]/div/div')
        contactaSoporte.click()
        time.sleep(1.5)

        contactaSoporte.click()
        time.sleep(1.5)



"""Finalizamos la ejecucion del codigo"""
def test_tearDown():
    """Cerramos el driver"""
    driver.quit()