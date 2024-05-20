import time
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


options = Options()
options.add_argument('--start-maximized')
options.add_argument('--incognito')
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = {'browser':'ALL'}
driver = webdriver.Chrome(chrome_options=options, executable_path='D:/Drivers/chromedriver.exe', desired_capabilities=dc)
fake = Faker('es_ES')



@pytest.mark.feature("SetUp")
class TestOpenHome:
    def test_openHome(self):
        """Abrimos el driver, la web en ambiente de TEST y maximizamos la ventana"""
        driver.get('https://antonio-rodriguez.tech')
        driver.maximize_window()
        assert 'Antonio Rodriguez' in driver.title
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

        closeCookies = driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
        closeCookies.click()
        time.sleep(0.5)


@pytest.mark.feature("Content")
class TestContent:
    def test_contentForm(self):
        """Hacemos click en inputUsuario -> placeHolder: Nombre y Apellido"""
        inputUsuario = driver.find_element(By.ID,'usuario')
        inputUsuario.click()
        time.sleep(0.3)

        inputUsuario.send_keys(fake.name())
        time.sleep(0.5)

        """Hacemos click en inputEmail -> placeHolder: Direccion de email"""
        inputEmail = driver.find_element(By.ID,'email')
        inputEmail.click()
        time.sleep(0.3)

        inputEmail.send_keys(fake.company_email())
        time.sleep(0.5)

        """Hacemos click en inputPhone -> placeHolder: Telefono"""
        inputPhone = driver.find_element(By.ID,'phone')
        inputPhone.click()
        time.sleep(0.3)

        inputPhone.send_keys(613223344)
        time.sleep(0.5)

        """Hacemos click en inputCompany -> placeHolder: Nombre de empresa"""
        inputCompany = driver.find_element(By.ID,'company')
        inputCompany.click()
        time.sleep(0.3)

        inputCompany.send_keys(fake.company())
        time.sleep(0.5)

        """Hacemos click en inputWebpage -> placeHolder: Pagina web"""
        inputWebpage = driver.find_element(By.ID,'webpage')
        inputWebpage.click()
        time.sleep(0.3)

        inputWebpage.send_keys('antonio-rodriguez.tech')
        time.sleep(0.5)

        """Hacemos click en inputCorreo -> placeHolder: Dominio de correo"""
        inputCorreo = driver.find_element(By.ID,'atEmail')
        inputCorreo.click()
        time.sleep(0.3)

        inputCorreo.send_keys(fake.domain_name())
        time.sleep(0.5)

        """Hacemos click en el Selector companySector"""
        selectorcompanySector = driver.find_element(By.ID,'companySector')
        selectorcompanySector.click()
        time.sleep(0.3)

        # Seleccionamos categoria
        category = driver.find_element(By.XPATH,'/html/body/div[1]/main/section/div[2]/div/form/select[1]/option[5]')
        category.click()
        time.sleep(0.5)

        """Hacemos click en el Selector numberEmployees"""
        numberEmployees = driver.find_element(By.ID,'numberEmployees')
        numberEmployees.click()
        time.sleep(0.3)

        # Seleccionamos categoria
        employees = driver.find_element(By.XPATH,'/html/body/div[1]/main/section/div[2]/div/form/select[2]/option[4]')
        employees.click()
        time.sleep(0.5)

        """Hacemos click en inputCheckbox termsAndPrivacyCheckbox"""
        inputCheckbox = driver.find_element(By.ID,'termsAndPrivacyCheckbox')
        inputCheckbox.click()
        time.sleep(0.3)

        inputCheckbox.click()
        time.sleep(0.3)

        inputCheckbox.click()
        time.sleep(0.5)

        """Hacemos click en Consigue tu informe gratuito"""
        clickOK = driver.find_element(By.XPATH,'/html/body/div[1]/main/section/div[2]/div/form/button/div')
        clickOK.click()
        time.sleep(3)


@pytest.mark.feature("TearDown")
class TestTearDown:
    # Close driver
    def test_tearDown(self):
        """Cerramos el driver"""
        driver.quit()