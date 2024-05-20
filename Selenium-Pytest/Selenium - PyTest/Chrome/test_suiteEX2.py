import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


options = Options()
options.add_argument('--start-maximized')
options.add_argument("--disable-popup-blocking")
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = {'browser':'ALL'}
driver = webdriver.Chrome(chrome_options=options, executable_path='C:/AntonioRodriguez/ChromeDriver/chromedriver.exe', desired_capabilities=dc)
time.sleep(0.5)


"""Test E2E de la seccion Exposicion en Internet"""

@pytest.mark.feature("SetUp")
class TestSetUp:
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
        """Ingresamos el password"""
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
        time.sleep(10)

        for e in driver.get_log('browser'):
            print(e)

@pytest.mark.feature("InternetExposure")
class TestExposure:
    def test_07_exposicionEnInternet(self):
        """Hacemos click en la seccion Exposicion para ver su contenido"""
        exposicion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[1]')
        exposicion.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

@pytest.mark.feature("MailboxSecurity")
class TestMailboxSecurity:
    def test_08_seguridadDeCorreo(self):
        """Hacemos click en la Subseccion de Seguridad de Correo en Exposicion en Internet"""
        seguridadDeCorreo = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[1]/span')
        seguridadDeCorreo.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

        sorTable1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div')
        sorTable1.click()
        time.sleep(0.5)
        sorTable1.click()
        time.sleep(0.3)

        sorTable2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[1]/div[2]/div')
        sorTable2.click()
        time.sleep(0.5)
        sorTable2.click()
        time.sleep(0.3)


    @pytest.mark.skip(reason="Tarda 30 mints en analizar")
    def test_11_volverAnalizar(self):
        """Hacemos scroll hasta el final de Seguridad de Correo"""
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        """Hacemos click en Volver a Analizar"""
        volverAnalizar = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div/div/div[4]/div/div[2]/div/div/div[1]/div[2]/button/div/div')
        volverAnalizar.click()
        time.sleep(3.5)

        for e in driver.get_log('browser'):
            print(e)
    @pytest.mark.skip(reason="Es del Analizar anterior")
    def test_12_continuar(self):
        """Despues de haber analizado SPF y DMARC nuevamente, hacemos click en Continuar"""
        continuar = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/button/div')
        continuar.click()
        time.sleep(1.5)

    def test_13_verTutorial(self):
        """Hacemos click en ver tutorial"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    def test_14_siguiente(self):
        """Hacemos click en Siguiente"""
        siguiente = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
        siguiente.click()
        time.sleep(0.5)

        siguiente.click()
        time.sleep(0.5)

    def test_15_estoyListo(self):
        """Hacemos click en Estoy listo"""
        estoyListo = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
        estoyListo.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    def test_16_verTutorial(self):
        """Hacemos nuevamente click en ver tutorial"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

    def test_17_saltarTutorial(self):
        """Hacemos click en Saltar tutorial"""
        saltarTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
        saltarTutorial.click()
        time.sleep(1)


"""Cambiamos a la seccion Filtraciones de Datos"""
@pytest.mark.feature("DataLeaks")
class TestLeaks:
    def test_18_filtracionesDeDatos(self):
        """Hacemos click en Filtraciones de Datos"""
        exposicion = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
        exposicion.click()
        time.sleep(1.5)

        filtracionesDatos = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[2]/span')
        filtracionesDatos.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def test_19_buscarEmpleados(self):
        """Buscamos un empleado de la lista de correos en Filtraciones de Datos -> Vision por empleados"""
        buscarEmpleados = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/div/div[2]/div/div[1]/div/input')
        buscarEmpleados.click()
        time.sleep(1)

        buscarEmpleados.send_keys('Antonio')
        time.sleep(1)
        buscarEmpleados.send_keys(Keys.BACKSPACE*2)
        time.sleep(1)

        buscarEmpleados.send_keys('Rodriguez')
        time.sleep(1)
        buscarEmpleados.send_keys(Keys.BACKSPACE*3)
        time.sleep(1)

        buscarEmpleados.send_keys('Farias')
        time.sleep(1)
        buscarEmpleados.send_keys(Keys.BACKSPACE*2)
        time.sleep(1.5)

    def test_20_verTutorial(self):
        """Hacemos click en ver tutorial"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[6]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    def test_21_siguiente(self):
        """Hacemos click en Siguiente"""
        siguiente = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
        siguiente.click()
        time.sleep(0.5)

        siguiente.click()
        time.sleep(0.5)

        siguiente.click()
        time.sleep(0.5)

    def test_22_estoyListo(self):
        """Hacemos click en Estoy listo"""
        estoyListo = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
        estoyListo.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    def test_23_verTutorial(self):
        """Hacemos nuevamente click en Volver a ver tutorial"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[6]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

    def test_24_saltarTutorial(self):
        """Hacemos click en Saltar tutorial"""
        saltarTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
        saltarTutorial.click()
        time.sleep(1)



"""Ahora nos vamos a la seccion de Seguridad de Pagina WEB"""
@pytest.mark.feature("WebSecurity")
class TestWebSecurity:
    def test_25_seguridadPaginaWEB(self):
        """Hacemos click en la Subseccion Seguridad de Pagina WEB"""
        exposicion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
        exposicion.click()
        time.sleep(1.5)

        seguridadDePaginaWEB = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[3]/span')
        seguridadDePaginaWEB.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

    def test_26_sorTable(self):
        """HAcemos click en sorTable de Seguridad de Pagina WEB"""
        sorTable = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div')
        sorTable.click()
        time.sleep(0.5)

        sorTable.click()
        time.sleep(0.5)

    def test_27_selectDominio(self):
        """Hacemos click en el icono de seleccionar los dominios WEBs que tenemos agregados"""
        selectIcon = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/div/div/select')
        selectIcon.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    def test_28_agregarDominio(self):
        """Hacemos click en el boton para agregar dominio WEB"""
        agregarDominio = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/button[1]/div/div')
        agregarDominio.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

        """Ingresamos un Dominio WEB"""
        barraBusqueda = driver.find_element(By.ID,'website')
        barraBusqueda.send_keys('www.antonioRodriguez.tech')
        time.sleep(1.5)
        barraBusqueda.send_keys(Keys.BACKSPACE*22)
        time.sleep(1)

        cancelar = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
        cancelar.click()
        time.sleep(1.5)

    @pytest.mark.xfail
    def test_29_quitarDominio(self):
        """Hacemos click en quitar dominio en Seguridad de Pagina WEB"""
        # Si hay solo un dominio agregado, este Test fallara porque no estara habilitado el boton
        quitarDominio = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/button[2]/div/div')
        quitarDominio.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

        cancelar = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
        cancelar.click()
        time.sleep(1)

    def test_30_verMas(self):
        """Hacemos click en Ver mas del item de Ataques de intermediario"""
        verMas1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div')
        verMas1.click()
        time.sleep(2.5)

        for e in driver.get_log('browser'):
            print(e)

        entendido1 = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
        entendido1.click()
        time.sleep(1)

        """Hacemos click en Ver mas del item Ataques de ClickJacking en Seguridad de Pagina WEB"""
        verMas2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div')
        verMas2.click()
        time.sleep(2.5)

        for e in driver.get_log('browser'):
            print(e)

        entendido2 = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
        entendido2.click()
        time.sleep(1)

        """Hacemos click en Ver mas del item Cross-Site Scripting en Seguridad de Pagina WEB"""
        verMas3 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div[2]/div')
        verMas3.click()
        time.sleep(2.5)

        for e in driver.get_log('browser'):
            print(e)

        entendido3 = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
        entendido3.click()
        time.sleep(1)

        """Hacemos click en Ver mas del item Ataques DDOS en Seguridad de Pagina WEB"""
        verMas4 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/div')
        verMas4.click()
        time.sleep(2.5)

        for e in driver.get_log('browser'):
            print(e)

        entendido4 = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
        entendido4.click()
        time.sleep(1)

    def test_31_verTutorial(self):
        """Hacemos click en Volver a ver tutorial"""
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    def test_32_siguiente(self):
        """Hacemos click en Siguiente"""
        siguiente = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
        siguiente.click()
        time.sleep(0.5)

        siguiente.click()
        time.sleep(0.5)

    def test_33_estoyListo(self):
        """Hacemos click en Estoy listo"""
        estoyListo = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
        estoyListo.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    def test_34_verTutorial(self):
        """Hacemos nuevamente click en Volver a ver tutorial"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

    def test_35_saltarTutorial(self):
        """Hacemos click en Saltar tutorial"""
        saltarTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
        saltarTutorial.click()
        time.sleep(1)


"""Ahora vamos a la Subseccion de Posibles Suplantaciones en Exposicion en Internet"""
@pytest.mark.feature("Impersonations")
class TestImpersonations:
    def test_36_posiblesSuplantaciones(self):
        """Hacemos click en la Subseccion de Posibles Suplantaciones en Exposicion en Internet"""
        exposicion = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
        exposicion.click()
        time.sleep(1.5)

        posibleSuplantaciones = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[4]/span')
        posibleSuplantaciones.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

    def test_37_sorTable(self):
        """Hacemos click en sorTable de Posibles Suplantaciones"""
        sorTable = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div')
        sorTable.click()
        time.sleep(1)

        sorTable.click()
        time.sleep(1)

    def test_38_seleccionarDominio(self):
        """Hacemos click en el icono para seleccionar dominio agregados"""
        selectDominio = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/div/div[1]/div/div/select')
        selectDominio.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

    def test_39_agregarDominio(self):
        """Hacemos click en el boton de añadir otra web"""
        otraWeb = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/div/div[1]/button/div/div')
        otraWeb.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

    def test_40_agregarURL(self):
        """Hacemos click en la barra de busqueda para agregar URL en Posibles Suplantaciones"""
        agregarURL = driver.find_element(By.ID,'website')
        agregarURL.click()
        time.sleep(1)

        agregarURL.send_keys('www.antonioRodriguez.tech')
        time.sleep(1.5)

        agregarURL.clear()
        time.sleep(1)

        cancelar = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
        cancelar.click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def test_41_verTutorial(self):
        """Hacemos click en ver tutorial"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    def test_42_siguiente(self):
        """Hacemos click en Siguiente"""
        siguiente = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
        siguiente.click()
        time.sleep(0.5)

        siguiente.click()
        time.sleep(0.5)

    def test_43_estoyListo(self):
        """Hacemos click en Estoy listo"""
        estoyListo = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
        estoyListo.click()
        time.sleep(1)

    def test_44_verTutorial(self):
        """Hacemos nuevamente click en Volver a ver tutorial"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

    def test_45_saltarTutorial(self):
        """Hacemos click en Saltar tutorial"""
        saltarTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
        saltarTutorial.click()
        time.sleep(1)


"""Ahora seleccionamos la Subseccion de Seguridad de Proveedores en Exposicion en Internet"""
@pytest.mark.feature("VendorSecurity")
class TestVendorSecurity:
    def test_46_seguridadProveedores(self):
        """Hacemos click en Seguridad de Proveedores"""
        exposicion = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
        exposicion.click()
        time.sleep(1.5)

        seguridadProveedores = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[5]/span')
        seguridadProveedores.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

    def test_47_agregarNuevoProveedor(self):
        """Hacemos click en Añade tu primer proveedor"""
        agregarProveedor = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/div/div[2]/div/div/button/div/div')
        agregarProveedor.click()
        time.sleep(1.5)

        for e in driver.get_log('browser'):
            print(e)

        nameSupplier = driver.find_element(By.ID,'name')
        nameSupplier.click()
        time.sleep(0.5)

        nameSupplier.send_keys('Antonio Rodriguez')
        time.sleep(1)

        # Hacemos click en el selector para desplegar cada una de las opciones
        selectSector = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/select')
        selectSector.click()
        time.sleep(1)

        # Seleccionamos la opcion 10 -> Transporte (excluida la aviacion)
        selectTransporte = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/select/option[10]')
        selectTransporte.click()
        time.sleep(1)

        dominioProveedor = driver.find_element(By.ID,'domain')
        dominioProveedor.click()
        time.sleep(0.5)
        dominioProveedor.send_keys('www.antonio.es')
        time.sleep(1)

        correoProveedor = driver.find_element(By.ID,'atEmail')
        correoProveedor.click()
        time.sleep(0.5)
        correoProveedor.clear()
        time.sleep(0.5)
        correoProveedor.send_keys('antonioRodriguez.ES')
        time.sleep(1)

        cancelar = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
        cancelar.click()
        time.sleep(1)

    def test_48_verTutorial(self):
        """Hacemos click en Volver a ver tutorial"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

        for e in driver.get_log('browser'):
            print(e)

    def test_49_siguiente(self):
        """Hacemos click en Siguiente"""
        siguiente = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
        siguiente.click()
        time.sleep(0.5)

        siguiente.click()
        time.sleep(0.5)

        siguiente.click()
        time.sleep(0.5)

    def test_50_estoyListo(self):
        """Hacemos click en Estoy listo"""
        estoyListo = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
        estoyListo.click()
        time.sleep(1)

    def test_51_verTutorial(self):
        """Hacemos nuevamente click en Volver a ver tutorial"""
        verTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
        verTutorial.click()
        time.sleep(1)

    def test_52_saltarTutorial(self):
        """Hacemos click en Saltar tutorial"""
        saltarTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
        saltarTutorial.click()
        time.sleep(1)

    def test_53_exposicionInternet(self):
        """Hacemos click nuevamente en Exposicion en Internet para cerrar"""
        exposicion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
        exposicion.click()
        time.sleep(0.5)


def test_tearDown():
    """Cerramos el driver"""
    driver.quit()