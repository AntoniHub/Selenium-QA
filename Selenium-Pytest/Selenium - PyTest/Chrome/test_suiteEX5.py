import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


options = Options()
options.add_argument('--start-maximized')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = {'browser':'ALL'}
driver = webdriver.Chrome(chrome_options=options, executable_path='C:/AntonioRodriguez/ChromeDriver/chromedriver.exe', desired_capabilities=dc)
time.sleep(0.5)


#Open HomePage
@pytest.mark.feature("SetUp")
class TestHomePage:
    def test_01_openHome(self):
        """Abrimos el navegador, el ambiente de TEST y maximixamos la ventana"""
        driver.get('https://antonio-rodriguez.tech')
        driver.maximize_window()
        assert 'Antonio Rodriguez' in driver.title
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

        #driver.save_screenshot('image.png')

    #Close cookies
    def test_02_closeCookies(self):
        """Identificamos la configuracion de cookies a traves de XPATH para cerrarlo"""
        cookies = driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
        cookies.click()
        time.sleep(0.5)

@pytest.mark.feature("QuickView")
class TestViewHome:
    #View Inicio
    def test_03_viewInicio(self):
        """Hacemos click en Inicio"""
        inicio = driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[1]/p[1]')
        inicio.click()
        time.sleep(0.5)

    #View Funcionalidades
    def test_04_viewFuncionalidades(self):
        """Hacemos click en funcionalidades"""
        funcionalidades = driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[1]/p[2]')
        funcionalidades.click()
        time.sleep(0.5)

    #View consiguelo
    def test_05_viewConsiguelo(self):
        """Hacemos click en consiguelo"""
        consiguelo = driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[1]/p[3]')
        consiguelo.click()
        time.sleep(0.5)

@pytest.mark.feature("LogIn")
class TestLogIn:
    #LogIn
    def test_06_LogIn(self):
        """Hacemos click en el LogIn a traves de del atributo CLASS"""
        logIn = driver.find_element(By.CLASS_NAME, 'css-u6po9p')
        driver.execute_script("arguments[0].scrollIntoView();", logIn)
        logIn.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    #Send mail
    def test_07_sendMail(self):
        """Ingresamos la direccion de EMail"""
        mail = driver.find_element(By.ID,'businessEmail')
        mail.click()
        time.sleep(0.2)
        mail.send_keys('abgrodriguezfarias@gmail.com')
        time.sleep(0.2)

    #Send password
    def test_08_sendPass(self):
        """Ingresamos el password"""
        password = driver.find_element(By.ID,'password')
        password.click()
        time.sleep(0.2)
        password.send_keys('T3st.4321')
        time.sleep(0.2)

    #Start session
    def test_09_startSession(self):
        """Hacemos click en iniciar session"""
        start = driver.find_element(By.ID,'emailButton')
        start.click()
        time.sleep(8)

        for e in driver.get_log('browser'):
            print(e)

#Close driver
def test_10_tearDown():
    """Cerramos el driver"""
    driver.quit()