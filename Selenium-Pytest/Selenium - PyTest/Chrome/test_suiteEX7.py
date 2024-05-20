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

    # Close configuracion de cookies
    def test_closeCookies(self):
        """Cerramos la configuracion de cookies"""
        cookies = driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
        cookies.click()
        time.sleep(0.5)

# Click on LogIn
@pytest.mark.feature("LogIn")
class TestLogIn:
    def test_LogIn(self):
        """Hacemos click en el LogIn"""
        logIn = driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[2]/button[1]/div')
        driver.execute_script("arguments[0].scrollIntoView();", logIn)
        logIn.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    # Send mail
    def test_sendMail(self):
        """Ingresamos la direccion de Email"""
        mail = driver.find_element(By.ID,'businessEmail')
        mail.click()
        time.sleep(0.2)
        mail.send_keys('abgrodriguezfarias@gmail.com')
        time.sleep(0.2)

    # Send password
    def test_sendPass(self):
        """Ingresamos el password"""
        password = driver.find_element(By.ID,'password')
        password.click()
        time.sleep(0.2)
        password.send_keys('T3st.1234')
        time.sleep(0.2)

    # Start session
    def test_startSession(self):
        """Hacemos click en iniciar session"""
        start = driver.find_element(By.ID,'emailButton')
        start.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

@pytest.mark.feature("settings")
class TestSettings:
    # Scroll to acciones
    def test_scrollToAcciones(self):
        """Hacemos scroll hasta la opcion de acciones"""
        time.sleep(10)
        driver.execute_script("window.scrollTo(0,2000);")
        time.sleep(2)


    # Click on Settings
    def test_settings(self):
        """Hacemos click en configuraciones"""
        settings = driver.find_element(By.ID,'settings-button')
        settings.click()
        time.sleep(1)

        """Hacemos click en Mi Cuenta"""
        miAccount = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[1]/span')
        miAccount.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

@pytest.mark.feature("EditUser")
class TestEditUser:
    # Tu Informacion
    # Edit user
    def test_editUser(self):
        """En la seccion Tu informacion, hacemos click para editar usuario"""
        editUser = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/button/div/div')
        editUser.click()
        time.sleep(0.5)

    # Edit input FirstName
    def test_editName(self):
        """Editamos el nombre a traves del atributo ID"""
        firstName = driver.find_element(By.ID,'firstName')
        firstName.click()
        time.sleep(0.3)

        firstName.clear()
        time.sleep(0.5)

        firstName.send_keys(fake.first_name())
        time.sleep(0.3)

    # Edit input LastName
        """Editamos el apellido a traves del atributo ID"""
        lastName = driver.find_element(By.ID,'lastName')
        lastName.click()
        time.sleep(0.3)

        lastName.clear()
        time.sleep(0.5)

        lastName.send_keys(fake.last_name())
        time.sleep(0.3)

    # Edit input phoneNumber
        """Editamos el campo phoneNumber a traves del atributo ID"""
        phoneNumber = driver.find_element(By.ID,'phoneNumber')
        phoneNumber.click()
        time.sleep(0.3)

        phoneNumber.clear()
        time.sleep(0.5)

        phoneNumber.send_keys(fake.phone_number())
        time.sleep(0.3)

    # Cancel changes
    def test_saveChanges(self):
        """Cancelamos los cambios que hemos generados, haciendo click en el boton CANCELAR"""
        saveChanges = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/button[1]/div')
        saveChanges.click()
        time.sleep(0.3)

        for e in driver.get_log('browser'):
            print(e)


@pytest.mark.feature("Purchase")
class TestPurchase:
    # Edit purchase
    def test_purchase(self):
        """Hacemos click en el boton editar de la seccion Datos de Facturacion"""
        editInvoicing = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[2]/button/div/div')
        editInvoicing.click()
        time.sleep(0.3)

        billingAddress = driver.find_element(By.ID,'line1')
        billingAddress.click()
        time.sleep(0.5)

        #billingAddress.clear()
        billingAddress.send_keys(Keys.CONTROL,"a",Keys.DELETE)
        time.sleep(0.5)

        billingAddress.send_keys(fake.street_address())
        time.sleep(0.3)

    # Business Name
        """Hacemos click en boton corporate para editar datos de corporacion"""
        corporate = driver.find_element(By.ID,'corporateName')
        time.sleep(0.2)

        corporate.clear()
        time.sleep(0.5)

        corporate.send_keys(fake.company())
        time.sleep(0.3)

    # Postal Code
        """Hacemos click en input Postal Code para cambiar el codigo postal"""
        postalCode = driver.find_element(By.ID,'postalCode')
        postalCode.click()
        time.sleep(0.3)

        postalCode.clear()
        time.sleep(0.5)

        postalCode.send_keys(fake.postcode())
        time.sleep(0.5)

    # City
        """Hacemos click en el boton de ciudad para editarlo"""
        city = driver.find_element(By.ID,'city')
        city.click()
        time.sleep(0.3)

        city.clear()
        time.sleep(0.5)

        city.send_keys(fake.city())
        time.sleep(0.3)

    # Cancel changes
    def test_saveChanges(self):
        """Hacemos click en el boton cancelar para salir de la pantalla de Facturacion"""
        saveChanges = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[2]/button[1]/div')
        saveChanges.click()
        time.sleep(0.3)

        for e in driver.get_log('browser'):
            print(e)


@pytest.mark.feature("Employees")
class TestEmployees:
    # Seccion Settings
    # Empleados
    def test_empleados(self):
        """Hacemos click en configuraciones"""
        settings = driver.find_element(By.ID, 'settings-button')
        settings.click()
        time.sleep(1)

        """En configuraciones, hacemos click en el boton Lista de Empleados"""
        listaEmpleados = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[2]/span')
        listaEmpleados.click()
        time.sleep(0.3)

        for e in driver.get_log('browser'):
            print(e)

    # Agregar empleado
    @pytest.mark.xfail
    def test_aniadirEmpleado(self):
        """Hacemos click en agregar empleado para visualizar modal y rellenar datos"""
        aniadirEmpleado = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/button[1]/div/div')
        aniadirEmpleado.click()
        time.sleep(0.3)

        for e in driver.get_log('browser'):
            print(e)

    # Edit firstName
        """Editar nombre de empleado"""
        nombreEmpleado = driver.find_element(By.ID,'firstName')
        nombreEmpleado.click()
        time.sleep(0.3)

        nombreEmpleado.clear()
        time.sleep(0.3)

        nombreEmpleado.send_keys(fake.first_name())
        time.sleep(0.3)

    # Edit lastName
        """Editar apellido de empelado"""
        lastNameEmpleado = driver.find_element(By.ID,'lastName')
        lastNameEmpleado.click()
        time.sleep(0.3)

        lastNameEmpleado.clear()
        time.sleep(0.3)

        lastNameEmpleado.send_keys(fake.last_name())
        time.sleep(0.3)

    # Edit Email
        """Editar EMail de empleado"""
        email = driver.find_element(By.ID,'email')
        email.click()
        time.sleep(0.3)

        email.clear()
        time.sleep(0.3)

    # Fallara porque el email debe ser del dominio perteneciente a la empresa (aca elegira uno random)
        email.send_keys(fake.company_email())
        time.sleep(0.3)

    # Add Rol
        """Seleccionar rol de empleado"""
        rol = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[4]/div/select')
        rol.click()
        time.sleep(0.3)

        admin = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[4]/div/select/option[2]')
        admin.click()
        time.sleep(0.3)

        saveWhitoutTAG = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/div[2]/button/div')
        saveWhitoutTAG.click()
        time.sleep(0.5)

        for e in driver.get_log('browser'):
            print(e)

        cancelar = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
        cancelar.click()
        time.sleep(0.8)


    def test_importarLista(self):
        """Hacemos click en Importar Lista CSV"""
        importarCSV = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/button[2]/div/div')
        importarCSV.click()
        time.sleep(0.8)

        for e in driver.get_log('browser'):
            print(e)

        # Cancelar y cerrar ventana
        cancelar = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
        cancelar.click()
        time.sleep(0.5)

    def test_filtrarEmpleados(self):
        """Hacemos click en Filtrar empleados - TAGs"""
        filtrarEmpleados = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/button/div/div')
        filtrarEmpleados.click()
        time.sleep(0.8)

        """Hacemos click en el selector de TAGs"""
        selectorTAG = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/select')
        selectorTAG.click()
        time.sleep(0.8)
        selectorTAG.click()
        time.sleep(0.5)

        # Des-seleccionamos el boton de Filtrar empleados
        filtrarEmpleados.click()
        time.sleep(0.5)

    def test_buscarEmpleado(self):
        """Hacemos click en Buscar Empleado"""
        buscarEmpleado = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/input')
        buscarEmpleado.click()
        time.sleep(0.5)

        buscarEmpleado.send_keys(fake.name())
        time.sleep(0.8)
        buscarEmpleado.clear()
        time.sleep(0.5)



@pytest.mark.feature("TearDown")
class TestTearDown:
    # Close driver
    def test_tearDown(self):
        """Cerramos el driver"""
        driver.quit()