import time
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = Options()
options.add_argument('--incognito')
options.add_argument('--start-maximized')
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = {'browser':'ALL'}
driver = webdriver.Chrome(chrome_options=options, executable_path='D:/Drivers/chromedriver.exe', desired_capabilities=dc)
fake = Faker('es_ES')



@pytest.mark.feature("SetUp")
class TestOpenHome:
    def test_01_openHome(self):
        """Antonio Rodriguez Farias"""
        driver.get('https://testing.arodriguezf.tech/test')
        driver.maximize_window()
        assert 'Antonio Rodriguez Farias' in driver.title
        time.sleep(1)

    # Close configuracion de cookies
    def test_02_closeCookies(self):
        """Cerramos la configuracion de cookies"""
        cookies = driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
        cookies.click()
        time.sleep(0.5)


# Click on LogIn
@pytest.mark.feature("LogIn")
class TestLogIn:
    def test_03_LogIn(self):
        """Hacemos click en el LogIn"""
        logIn = driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div[2]/button[1]/div')
        driver.execute_script("arguments[0].scrollIntoView();", logIn)
        logIn.click()
        time.sleep(1)

    # Send mail
    def test_04_sendMail(self):
        """Ingresamos la direccion de Email"""
        mail = driver.find_element(By.ID,'businessEmail')
        mail.click()
        time.sleep(0.2)
        mail.send_keys('abgrodriguezfarias@gmail.com')
        time.sleep(0.2)

    # Send password
    def test_05_sendPass(self):
        """Ingresamos el password"""
        password = driver.find_element(By.ID,'password')
        password.click()
        time.sleep(0.2)
        password.send_keys('Test1234')
        time.sleep(0.2)

    # Start session
    def test_06_startSession(self):
        """Hacemos click en iniciar session"""
        start = driver.find_element(By.ID,'emailButton')
        start.click()
        time.sleep(3)

        for e in driver.get_log('browser'):
            print(e)



@pytest.mark.feature("Settings")
class TestSettings:
    # Scroll to acciones
    def test_07_editUser(self):
        # Click on Settings
        """En settings, abrimos ventana en Mi cuenta"""
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /my-account
        driver.get('https://testing.arodriguezf.tech/my-account')
        time.sleep(3.5)
        # Verificamos a traves del titulo que en verdad se visualice la pagina y no abra con error (404 por ejm)
        assert 'Ajustes - Antonio Rodriguez Farias' in driver.title

        """# Scrapping Text -> Tu información
        texto = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/b')
        texto = texto.text
        assert "Tu información" == texto"""

        # Your Information -> Edit data
        edit_data = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/button/div/div')
        edit_data.click()
        time.sleep(0.5)

        # First name
        first_name = driver.find_element(By.ID,'firstName')
        first_name.click()
        time.sleep(0.2)
        first_name.clear()
        time.sleep(0.2)

        first_name.send_keys(fake.first_name())
        time.sleep(0.3)

        # Last name
        last_name = driver.find_element(By.ID,'lastName')
        last_name.click()
        time.sleep(0.2)
        last_name.clear()
        time.sleep(0.2)

        last_name.send_keys(fake.last_name())
        time.sleep(0.3)

        # Phone
        phone = driver.find_element(By.ID,'phoneNumber')
        phone.click()
        time.sleep(0.2)
        phone.clear()
        time.sleep(0.2)

        phone.send_keys(+34613223344)
        time.sleep(0.3)

        # Save changes
        save_changes = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/button[1]/div')
        save_changes.click()
        time.sleep(1)


    # Edit purchase
    def test_08_editPurchase(self):
        """Hacemos click en el boton editar de la seccion Datos de Facturacion"""
        editInvoicing = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[2]/button/div/div')
        editInvoicing.click()
        time.sleep(0.3)

        billingAddress = driver.find_element(By.ID,'line1')
        billingAddress.click()
        time.sleep(0.2)

        # billingAddress.clear()
        billingAddress.send_keys(Keys.CONTROL,"a",Keys.DELETE)
        time.sleep(0.5)

        billingAddress.send_keys(fake.street_address())
        time.sleep(0.3)
        element_attribute_value = billingAddress.get_attribute('value')
        print('\nnewBillingAddress: {}'.format(element_attribute_value))
        time.sleep(0.3)

        # Business Name
        """Hacemos click en boton corporate para editar datos de corporacion"""
        corporate = driver.find_element(By.ID,'corporateName')
        time.sleep(0.2)

        corporate.clear()
        time.sleep(0.5)

        corporate.send_keys(fake.company())
        element_attribute_value = corporate.get_attribute('value')
        print('\nnewCorporate: {}'.format(element_attribute_value))
        time.sleep(0.3)

        # Postal Code
        """Hacemos click en input Postal Code para cambiar el codigo postal"""
        postalCode = driver.find_element(By.ID,'postalCode')
        postalCode.click()
        time.sleep(0.3)

        postalCode.clear()
        time.sleep(0.5)

        postalCode.send_keys(fake.postcode())
        element_attribute_value = postalCode.get_attribute('value')
        print('\nnewPostalCode: {}'.format(element_attribute_value))
        time.sleep(0.3)

        # City
        """Hacemos click en el boton de ciudad para editarlo"""
        city = driver.find_element(By.ID,'city')
        city.click()
        time.sleep(0.3)

        city.clear()
        time.sleep(0.5)

        city.send_keys(fake.city())
        element_attribute_value = city.get_attribute('value')
        print('\nnewCity: {}'.format(element_attribute_value))
        time.sleep(0.3)

        # Save changes
        saveChanges = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[2]/button[1]/div')
        saveChanges.click()
        time.sleep(0.3)

        for e in driver.get_log('browser'):
            print(e)



@pytest.mark.feature("Employees")
class TestEmployees:
    # Seccion Settings
    # Empleados
    def test_09_empleados(self):
        """Settings -> Employee list """
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /employees
        driver.get('https://testing.arodriguezf.tech/employees')
        time.sleep(3.5)
        assert 'Ajustes - Antonio Rodriguez Farias' in driver.title



@pytest.mark.feature("Communications")
class TestCommunications:
    # Seccion Settings
    # Click en Comunicaciones
    def test_10_comunicaciones(self):
        """Settings -> Communications """
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /email-preferences
        driver.get('https://testing.arodriguezf.tech/email-preferences')
        time.sleep(5)
        assert 'Ajustes - Antonio Rodriguez Farias' in driver.title



@pytest.mark.feature("MySubscriptions")
class TestMySubscriptions:
    # Seccion Settings
    # Mi suscripcion
    def test_13_miSuscripcion(self):
        """Settings -> Billing """
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /billing
        driver.get('https://testing.arodriguezf.tech/billing')
        time.sleep(3.5)
        assert 'Ajustes - Antonio Rodriguez Farias' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("ControlPanel")
class TestControlPanel:
    # Avanzamos en el panel de control
    # Seccion panel de control
    def test_14_panelDeControl(self):
        """Settings -> Control panel """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /control-panel
        driver.get('https://testing.arodriguezf.tech/control-panel')
        time.sleep(3.5)
        assert 'Panel de control - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("Acciones")
class TestAcciones:
    # Seccion listado de acciones
    def test_15_listadoDeAcciones(self):
        """Home -> /client/actions"""
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /employees
        driver.get('https://testing.arodriguezf.tech/user/actions')
        time.sleep(3.5)
        assert 'Listado de acciones - Antonio Rodriguez Farias' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("DeviceSecurity")
class TestSeguridad:
    def test_16_seguridadDispositivos(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /control-panel
        driver.get('https://testing.arodriguezf.tech/devices')
        time.sleep(3.5)
        assert 'Seguridad - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)


        """ Ir a /protections"""
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /control-panel
        driver.get('https://testing.arodriguezf.tech/protections')
        time.sleep(3.5)
        assert 'Seguridad - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)



@pytest.mark.feature("Managedthreats")
class TestAmenazasGestionadas:
    def test_17_amenazasGestionadas(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /control-panel
        driver.get('https://testing.arodriguezf.tech/threats')
        time.sleep(3.5)
        assert 'Amenazas - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("MailboxSecurity")
class TestSeguridadBuzones:
    def test_18_seguridadBuzones(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /control-panel
        driver.get('https://testing.arodriguezf.tech/security')
        time.sleep(3.5)
        assert 'Seguridad - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("EmailSecurity")
class TestSeguridadCorreo:
    def test_19_seguridadCorreo(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /control-panel
        driver.get('https://testing.arodriguezf.tech/email-security')
        time.sleep(3.5)
        assert 'Seguridad - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("DataBreaches")
class TestFiltracionesDatos:
    def test_20_seguridadCorreo(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /control-panel
        driver.get('https://testing.arodriguezf.tech/alert')
        time.sleep(3.5)
        assert 'Filtraciones - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("WebsiteSecurity")
class TestSeguridadWEB:
    def test_21_seguridadWEB(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /control-panel
        driver.get('https://testing.arodriguezf.tech/website')
        time.sleep(3.5)
        assert 'Seguridad web - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("PossibleSpoofs")
class TestPosiblesSuplantaciones:
    def test_22_PosiblesSuplantaciones(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /control-panel
        driver.get('https://testing.arodriguezf.tech/domain')
        time.sleep(3.5)
        assert 'Posibles suplantaciones - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("SupplierSecurity")
class TestSeguridadProveedores:
    def test_23_SeguridadProveedores(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /client/control-panel
        driver.get('https://testing.arodriguezf.tech/security')
        time.sleep(3.5)
        assert 'Seguridad - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



@pytest.mark.feature("Phishing")
class TestCampaniasPhishing:
    def test_23_campaniasPhishing(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /client/control-panel
        driver.get('https://testing.arodriguezf.tech/simulator')
        time.sleep(3.5)
        assert 'Formación - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)


    def test_24_crearCampania(self):
        """Home """
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        # change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        # Open /client/control-panel
        driver.get('https://testing.arodriguezf.tech/new-simulator')
        time.sleep(3.5)
        assert 'Crear campaña - Antonio Rodriguez' in driver.title

        for e in driver.get_log('browser'):
            print(e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)




@pytest.mark.feature("TearDown")
class TestTearDown:
    # Close driver
    def test_tearDown(self):
        """Cerramos el driver"""
        driver.quit()