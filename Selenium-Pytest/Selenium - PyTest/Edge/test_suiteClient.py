import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
#options.add_argument('--headless')
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
driver = webdriver.Edge(executable_path='C:/AntonioRodriguez/EdgeDriver/msedgedriver.exe', options = options)


"""
Regression test E2E /client
"""

@pytest.mark.feature("SetUp")
class TestOpenHome:
    def test_01_openHome(self):
        """Abrimos el driver, la web en ambiente de TEST y maximizamos la ventana"""
        driver.get('https://antonio-rodriguez.tech')
        driver.maximize_window()
        assert 'Antonio Rodriguez' in driver.title
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
        logIn = driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[2]/button[1]/div')
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
        password.send_keys('T3st.4321')
        time.sleep(0.2)

    # Start session
    def test_06_startSession(self):
        """Hacemos click en iniciar session"""
        start = driver.find_element(By.ID,'emailButton')
        start.click()
        time.sleep(1)

@pytest.mark.feature("settings")
class TestSettings:
    # Scroll to acciones
    def test_07_scrollToAcciones(self):
        """Hacemos scroll hasta la opcion de acciones"""
        time.sleep(10)
        driver.execute_script("window.scrollTo(0,2000);")
        time.sleep(2)


    # Click on Settings
    def test_08_settings(self):
        """Hacemos click en configuraciones"""
        settings = driver.find_element(By.ID,'settings-button')
        settings.click()
        time.sleep(1)

        """Hacemos click en Mi Cuenta"""
        miAccount = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[1]/span')
        miAccount.click()
        time.sleep(1)

@pytest.mark.feature("EditUser")
class TestEditUser:
    # Tu Informacion
    # Edit user
    def test_09_editUser(self):
        """En la seccion Tu informacion, hacemos click para editar usuario"""
        edit = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/button/div/div')
        edit.click()
        time.sleep(0.5)

    # Edit input FirstName
    def test_10_firstName(self):
        """Editamos el nombre a traves del atributo ID"""
        first = driver.find_element(By.ID,'firstName')
        first.click()
        time.sleep(0.3)

        first.clear()
        time.sleep(0.5)

        first.send_keys('TestFactum')
        time.sleep(0.3)

    # Edit input LastName
        """Editamos el apellido a traves del atributo ID"""
        last = driver.find_element(By.ID,'lastName')
        last.click()
        time.sleep(0.3)

        last.clear()
        time.sleep(0.5)

        last.send_keys('PruebaFactum')
        time.sleep(0.3)

    # Edit input phoneNumber
        """Editamos el campo phoneNumber a traves del atributo ID"""
        phone = driver.find_element(By.ID,'phoneNumber')
        phone.click()
        time.sleep(0.3)

        phone.clear()
        time.sleep(0.5)

        phone.send_keys('+34 123456789')
        time.sleep(0.3)

    # Cancel changes
    def test_11_cancelarCambios(self):
        """Cancelamos los cambios que hemos generados, haciendo click en el boton CANCELAR"""
        cancelar = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/button[2]/div')
        cancelar.click()
        time.sleep(0.3)

@pytest.mark.feature("Purchase")
class TestPurchase:
    # Edit purchase
    # Scroll to Datos de Facturacion
    def test_12_scrollToPurchase(self):
        """En la seccion Facturacion, scrolleamos hasta el input con placeholder='Billing address'"""
        time.sleep(2)
        scroll = driver.find_element(By.ID, 'line1')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        time.sleep(2)

    # Edit purchase
    def test_13_purchase(self):
        """Hacemos click en el boton editar de la seccion Datos de Facturacion"""
        editar = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[2]/button/div/div')
        editar.click()
        time.sleep(0.3)

        direccion = driver.find_element(By.ID,'line1')
        time.sleep(0.2)
        direccion.clear()
        time.sleep(0.5)

        direccion.send_keys('Calle José Cadalso')
        time.sleep(0.3)

    # Coporate Name
        """Hacemos click en boton corporate para editar datos de corporacion"""
        corporate = driver.find_element(By.ID,'corporateName')
        time.sleep(0.2)
        #corporate.click()
        #time.sleep(0.3)

        corporate.clear()
        time.sleep(0.5)

        corporate.send_keys('Test')
        time.sleep(0.3)

    # City
        """Hacemos click en el boton de ciudad para editarlo"""
        city = driver.find_element(By.ID,'city')
        city.click()
        time.sleep(0.3)

        city.clear()
        time.sleep(0.5)

        city.send_keys('Madrid')
        time.sleep(0.3)

    # Cancel changes
    def test_14_cancelChange(self):
        """Hacemos click en el boton cancelar para salir de la pantalla de Facturacion"""
        cancel = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[2]/button[2]/div')
        cancel.click()
        time.sleep(0.3)

@pytest.mark.feature("Employees")
class TestEmployees:
    # Seccion Settings
    # Empleados
    def test_15_empleados(self):
        """Hacemos click en configuraciones"""
        settings = driver.find_element(By.ID, 'settings-button')
        settings.click()
        time.sleep(1)

        """En configuraciones, hacemos click en el boton Lista de Empleados"""
        listaEmpleados = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[2]/span')
        listaEmpleados.click()
        time.sleep(0.3)

    # Agregar empleado
    def test_16_aniadirEmpleado(self):
        """Hacemos click en agregar empleado para visualizar modal y rellenar datos"""
        aniadirEmpleado = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/button[1]/div/div')
        aniadirEmpleado.click()
        time.sleep(0.3)

    # Edit firstName
        """Editar nombre de empleado"""
        nombreEmpleado = driver.find_element(By.ID,'firstName')
        nombreEmpleado.click()
        time.sleep(0.3)

        nombreEmpleado.clear()
        time.sleep(0.3)

        nombreEmpleado.send_keys('Employee')
        time.sleep(0.3)

    # Edit lastName
        """Editar apellido de empelado"""
        lastNameEmpleado = driver.find_element(By.ID,'lastName')
        lastNameEmpleado.click()
        time.sleep(0.3)

        lastNameEmpleado.clear()
        time.sleep(0.3)

        lastNameEmpleado.send_keys('lastName')
        time.sleep(0.3)

    # Edit Email
        """Editar EMail de empleado"""
        email = driver.find_element(By.ID,'email')
        email.click()
        time.sleep(0.3)

        email.clear()
        time.sleep(0.3)

        email.send_keys('abgrodriguezfarias@gmail.com')
        time.sleep(0.3)

    # Add Rol
        """Seleccionar rol de empleado"""
        rol = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[4]/div/select')
        rol.click()
        time.sleep(0.3)

        admin = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[4]/div/select/option[2]')
        admin.click()
        time.sleep(0.3)

        cancel = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
        cancel.click()
        time.sleep(0.5)

    def test_17_importarLista(self):
        """Hacemos click en Importar Lista CSV"""
        importarCSV = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/button[2]/div/div')
        importarCSV.click()
        time.sleep(0.8)

        # Cancelar y cerrar ventana
        cancelar = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
        cancelar.click()
        time.sleep(0.5)

    def test_18_filtrarEmpleados(self):
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

    def test_19_buscarEmpleado(self):
        """Hacemos click en Buscar Empleado"""
        buscarEmpleado = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/input')
        buscarEmpleado.click()
        time.sleep(0.5)

        buscarEmpleado.send_keys('Rodriguez')
        time.sleep(0.8)
        buscarEmpleado.clear()
        time.sleep(0.5)

@pytest.mark.feature("Communications")
class TestCommunications:
    # Seccion Settings
    # Click en Comunicaciones
    def test_20_comunicaciones(self):
        """Hacemos click en configuraciones"""
        settings = driver.find_element(By.ID, 'settings-button')
        settings.click()
        time.sleep(1)

        """En la seccion Comunicaciones, hacer click en el item Comunicaciones"""
        comunicaciones = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[3]/span')
        comunicaciones.click()
        time.sleep(0.3)

    # Click on slideButtons
    def test_21_slideButtons(self):
        """Hacemos click en cada uno de los Slide Buttons de la seccion Comunicaciones"""
        seguridadWeb = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button/div[1]')
        seguridadWeb.click()
        time.sleep(0.3)
        seguridadWeb.click()
        time.sleep(0.3)

        suplantacionWeb = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/button/div[1]')
        suplantacionWeb.click()
        time.sleep(0.3)
        suplantacionWeb.click()
        time.sleep(0.3)

        seguridadDispositivos = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[3]/button/div[1]')
        seguridadDispositivos.click()
        time.sleep(0.3)
        seguridadDispositivos.click()
        time.sleep(0.3)

        filtracionesDatos = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[4]/button/div[1]')
        filtracionesDatos.click()
        time.sleep(0.3)
        filtracionesDatos.click()
        time.sleep(0.3)

        seguridadCorreo = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[5]/button/div[1]')
        seguridadCorreo.click()
        time.sleep(0.3)
        seguridadCorreo.click()
        time.sleep(0.3)

        formacionPhishing = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[6]/button/div[1]')
        formacionPhishing.click()
        time.sleep(0.3)
        formacionPhishing.click()
        time.sleep(0.3)

        seguridadProveedores = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[7]/button/div[1]')
        seguridadProveedores.click()
        time.sleep(0.3)
        seguridadProveedores.click()
        time.sleep(0.3)

        panelAcciones = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[8]/button/div[1]')
        panelAcciones.click()
        time.sleep(0.3)
        panelAcciones.click()
        time.sleep(0.3)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

@pytest.mark.feature("News")
class TestNews:
    # Emails con las últimas novedades
    # Novedades
    def test_22_novedades(self):
        """En la seccion Comunicaciones, SubSeccion Emails con ultimas novedades, hacemos click
        en Novedades"""
        novedades = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div[2]/div[1]/button/div[2]')
        novedades.click()
        time.sleep(0.3)
        novedades.click()
        time.sleep(0.3)

    # Boletín mensual
        """Hacemos click en Boletin Mensual"""
        boletinMensual = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div[2]/div[2]/button/div[2]')
        boletinMensual.click()
        time.sleep(0.3)
        boletinMensual.click()
        time.sleep(0.3)

    # Noticias generales y actualizaciones
        """Hacemos click en Noticias Generales y Actualizaciones"""
        noticiasGenerales = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div[2]/div[3]/button/div[2]')
        noticiasGenerales.click()
        time.sleep(0.3)
        noticiasGenerales.click()
        time.sleep(0.3)

@pytest.mark.feature("MySubscriptions")
class TestMySubscriptions:
    # Seccion Settings
    # Mi suscripcion
    def test_23_miSuscripcion(self):
        """Hacemos click en configuraciones"""
        settings = driver.find_element(By.ID, 'settings-button')
        settings.click()
        time.sleep(1)

        """en la seccion Mi Suscripcion, hacemos click en Mi Suscripcion"""
        suscripcion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[4]/span')
        suscripcion.click()
        time.sleep(2)
        #suscripcion.click()
        #time.sleep(0.3)

@pytest.mark.feature("MyNotifications")
class TestMyNotifications:
    # Seccion Tus notificaciones
    # Mis notificaciones
    def test_24_misNotificaciones(self):
        """En la Campana, hacemos click en Mis Notificaciones"""
        notificaciones = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[1]/button/div')
        notificaciones.click()
        time.sleep(2)

@pytest.mark.feature("ControlPanel")
class TestControlPanel:
    # Avanzamos en el panel de control
    # Seccion panel de control
    def test_25_panelDeControl(self):
        """En el panel de control, Hacemos click en Panel de Control"""
        panel = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[2]/span')
        panel.click()
        time.sleep(1)

    # Seccion listado de acciones
    def test_26_listadoDeAcciones(self):
        """En la seccion del Listado de Acciones, hacemos click en Listado de Acciones"""
        listadoDeAcciones = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[3]/span')
        listadoDeAcciones.click()
        time.sleep(1)

@pytest.mark.feature("DeviceSecurity")
class TestDeviceSecurity:
    # Proteccion
    # Seguridad de Dispositivos
    def test_27_seguridadDispositivos(self):
        """En la seccion de Proteccion, hacemos click en el boton Seguridad de Dispositivos"""
        proteccion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[1]')
        proteccion.click()
        time.sleep(1)

        seguridadDispositivos = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[1]/span')
        action = ActionChains(driver)
        action.move_to_element(seguridadDispositivos).perform()
        time.sleep(0.5)

        amenazasGestionadas = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[2]/span')
        action.move_to_element(amenazasGestionadas).perform()
        time.sleep(0.5)

        seguridadBuzones = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[3]/span')
        action.move_to_element(seguridadBuzones).perform()
        time.sleep(0.5)

        proteccion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[1]')
        proteccion.click()
        time.sleep(1)

@pytest.mark.feature("InternetExposure")
class TestExposure:
    # Seccion Exposicion en Internet
    def test_28_exposicionEnInternet(self):
        """En la seccion de Exposicion en Internet, recorremos la seccion de Exposicion en Internet"""
        exposicion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[1]')
        exposicion.click()
        time.sleep(1)

        seguridadEnCorreo = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[1]/span')
        action = ActionChains(driver)
        action.move_to_element(seguridadEnCorreo).perform()
        time.sleep(0.5)

        filtracionesDeDatos = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[2]/span')
        action.move_to_element(filtracionesDeDatos).perform()
        time.sleep(0.5)

        seguridadDePaginaWeb = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[3]/span')
        action.move_to_element(seguridadDePaginaWeb).perform()
        time.sleep(0.5)

        posiblesSuplantaciones = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[4]/span')
        action.move_to_element(posiblesSuplantaciones).perform()
        time.sleep(0.5)

        seguridadDeProveedores = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[5]/span')
        action.move_to_element(seguridadDeProveedores).perform()
        time.sleep(0.5)

        exposicion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[1]')
        exposicion.click()
        time.sleep(1)

@pytest.mark.feature("PhishingCampaign")
class TestPhishingCampaign:
    def test_29_formarcioPhishing(self):
        """Hacemos click en Formación de Phishing"""
        formacionPhishing = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[6]/span')
        formacionPhishing.click()
        time.sleep(1.5)

    def test_30_sorTable(self):
        """Hacemos click en sorTable de Formacion de phishing"""
        sorTable = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div/div/div[1]/div[2]/div')
        sorTable.click()
        time.sleep(0.5)

        sorTable.click()
        time.sleep(0.5)

    def test_31_crearCampania(self):
        """Hacemos click en Crear campaña"""
        crearCamania = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div[2]/button[1]/div/div')
        crearCamania.click()
        time.sleep(1)

        """Hacemos click en cada una de las campañas"""
        paqueteNoRecibido = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div')
        paqueteNoRecibido.click()
        time.sleep(0.6)

        documentoEscaneado = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div')
        documentoEscaneado.click()
        time.sleep(0.6)

        facturaElectricidad = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div')
        facturaElectricidad.click()
        time.sleep(0.6)

        documentoCompartido = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[4]/div')
        documentoCompartido.click()
        time.sleep(0.6)

        coronavirus = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[5]/div')
        coronavirus.click()
        time.sleep(0.6)

        comentariosTuTrabajo = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[6]/div')
        comentariosTuTrabajo.click()
        time.sleep(0.6)

    def test_32_seleccionarEmpleados(self):
        """Seleccionar empleados de la lista o enviar campaña a todos los empleados"""
        seleccionarLista = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div')
        seleccionarLista.click()
        time.sleep(0.5)

        """Hacemos click en Seleccionar de la lista"""
        # Buscamos en la barra de busqueda
        buscarEmpleado = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div/input')
        buscarEmpleado.click()
        time.sleep(0.3)

        buscarEmpleado.send_keys('rodriguez')
        time.sleep(0.8)
        buscarEmpleado.clear()
        time.sleep(0.6)

        # Filtrar empleados - TAGs
        filtrarEmpleados = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[1]/button/div/div')
        filtrarEmpleados.click()
        time.sleep(0.5)

        # Agregar filtro
        agregarFiltro = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/button/div/div')
        agregarFiltro.click()
        time.sleep(0.5)

        # Quitar filtro
        quitarFiltro = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/button/div/div')
        quitarFiltro.click()
        time.sleep(0.5)

        # Desplegar selector de TAGs
        selectorTAG = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/select')
        selectorTAG.click()
        time.sleep(1)
        selectorTAG.click()
        time.sleep(0.5)

    # Cuando quieres mandar la campaña
    def test_33_datePicker(self):
        """Hacemos click en el Date Picker para desplegar calendario"""
        datePicker = driver.find_element(By.CLASS_NAME,'datapiker-btn')
        datePicker.click()
        time.sleep(0.5)

        # Hacemos click en Phishing header para volver a la pagina inicial de Phishing
        phishing = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[6]/span')
        phishing.click()
        time.sleep(0.5)

    # Resultados de Campanias
    def test_34_resultadosCampanias(self):
        """Hacemos click en el buscador de Resultados de Campañas"""
        buscarCampania = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div/input')
        buscarCampania.click()
        time.sleep(0.5)

        buscarCampania.send_keys('elec')
        time.sleep(0.8)
        buscarCampania.clear()
        time.sleep(0.5)


    # Visión general por empleado
    def test_35_buscarEmpleado(self):
        """Hacemos click en Buscar empleado"""
        buscarEmpleado = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div[2]/div/div[1]/div/input')
        buscarEmpleado.click()
        time.sleep(0.5)

        buscarEmpleado.send_keys('Rodriguez')
        time.sleep(1)
        buscarEmpleado.clear()
        time.sleep(0.5)

        """Hacemos click en Filtrar empleado"""
        filtrarEmpleado = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div[2]/div/div[1]/button/div/div')
        filtrarEmpleado.click()
        time.sleep(0.8)

        # Abrimos el selector
        selectorTAG = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/select')
        selectorTAG.click()
        time.sleep(0.8)
        selectorTAG.click()
        time.sleep(0.5)

        filtrarEmpleado.click()
        time.sleep(0.5)

    #Volver a ver tutorial
    def test_36_verTutorial(self):
        """Hacemos click en Volver a ver tutorial"""
        volverAVerTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[5]/div/button[1]/div/div')
        volverAVerTutorial.click()
        time.sleep(1)

    def test_37_siguiente(self):
        """Hacemos click en siguiente"""
        siguiente = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
        siguiente.click()
        time.sleep(0.5)

        siguiente.click()
        time.sleep(0.5)

    def test_38_estoyListo(self):
        """Hacemos click en Estoy listo"""
        estoyListo = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
        estoyListo.click()
        time.sleep(1.5)

    def test_39_volverAVerTutorial(self):
        """Hacemos click en Volver a ver tutorial"""
        volverAVerTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[5]/div/button[1]/div/div')
        volverAVerTutorial.click()
        time.sleep(1.5)

    def test_40_saltarTutorial(self):
        """Hacemos click en Saltar tutorial"""
        saltarTutorial = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
        saltarTutorial.click()
        time.sleep(1.5)

@pytest.mark.feature("Footer")
class TestFooter:
    # Contactar con soporte
    def test_41_contactarSoporte(self):
        """Hacemos click en Contactar con soporte"""
        contactarSoporte = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[2]/a[1]')
        contactarSoporte.click()
        time.sleep(1.3)
        contactarSoporte.click()
        time.sleep(1.3)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # Soporte
    def test_42_chatOnline(self):
        """Hacemos click en Chat Online"""
        chatOnline = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[2]/a[1]')
        chatOnline.click()
        time.sleep(1)
        chatOnline.click()
        time.sleep(1)

    # Aviso Legal y Condiciones de Uso
    def test_43_condicionesUso(self):
        """Hacemos click en Aviso Legal y Condiciones de Uso"""
        condicionesUso = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[3]/a[1]')
        condicionesUso.click()
        time.sleep(1)

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,2000);")
        time.sleep(1)
        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)

    # Condiciones Generales de Contratación
    def test_44_generalesContratacion(self):
        """Hacemos click en Condiciones Generales de Contratación"""
        contratacion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[3]/a[2]')
        contratacion.click()
        time.sleep(1)

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,2000);")
        time.sleep(1)
        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)


    # Política de privacidad
    def test_45_politicaPrivacidad(self):
        """Hacemmos click en Política de privacidad"""
        politicaPrivacidad = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[3]/a[3]')
        politicaPrivacidad.click()
        time.sleep(1)

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,2000);")
        time.sleep(1)
        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)

    def test_46_openCookies(self):
        """Abrimos la configuracion de cookies ubicada en la parte inferior derecha"""
        cookies = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[3]/a[4]')
        cookies.click()
        time.sleep(1)

    #Cookies tecnicas propias
    def test_47_cookiesTecnicas(self):
        """Hacemos click en cookies tecnicas propias"""
        cookiesTecnicas = driver.find_element(By.ID,'ot-header-id-C0001')
        cookiesTecnicas.click()
        time.sleep(1)

    #Cookies analiticas
    def test_48_cookiesAnaliticas(self):
        """Hacemos click en cookies analiticas"""
        cookiesAnaliticas = driver.find_element(By.ID,'ot-header-id-C0002')
        cookiesAnaliticas.click()
        time.sleep(1)
        """Clickeamos en el switch"""
        switch = driver.find_element(By.CLASS_NAME,'ot-switch-nob')
        switch.click()
        time.sleep(0.3)
        """Volvemos al estado inicial del switch"""
        switch.click()
        time.sleep(1)

    #Confirm preferences
    def test_49_confirmarPreferencias(self):
        """Hacemos click en confirmar mis preferencias"""
        confirmar = driver.find_element(By.CLASS_NAME,'save-preference-btn-handler')
        confirmar.click()
        time.sleep(1)

@pytest.mark.feature("TearDown")
class TestTearDown:
    # Close driver
    def test_tearDown(self):
        """Cerramos el driver"""
        driver.quit()