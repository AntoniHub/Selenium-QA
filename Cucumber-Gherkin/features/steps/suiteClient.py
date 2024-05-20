import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


options = Options()


"""
Regression test E2E /client
"""

@given('User after LogIn')
def test_01_openHome(context):
    """Abrimos el driver, la web en ambiente de TEST y maximizamos la ventana"""
    context.driver = webdriver.Chrome()
    context.driver.get('https://antonio-rodriguez.tech')
    context.driver.maximize_window()
    assert 'Antonio Rodriguez' in context.driver.title
    time.sleep(1)

# Close configuracion de cookies
#def test_02_closeCookies(context):
    """Cerramos la configuracion de cookies"""
    context.cookies = context.driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
    context.cookies.click()
    time.sleep(0.5)

# Click on LogIn
#def test_03_LogIn(context):
    """Hacemos click en el LogIn"""
    context.logIn = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[2]/button[1]/div')
    context.driver.execute_script("arguments[0].scrollIntoView();", context.logIn)
    context.logIn.click()
    time.sleep(1)

# Send mail
#def test_04_sendMail(context):
    """Ingresamos la direccion de Email"""
    context.mail = context.driver.find_element(By.ID,'businessEmail')
    context.mail.click()
    time.sleep(0.2)
    context.mail.send_keys('abgrodriguezfarias@gmail.com')
    time.sleep(0.2)

# Send password
#def test_05_sendPass(context):
    """Ingresamos el password"""
    context.password = context.driver.find_element(By.ID,'password')
    context.password.click()
    time.sleep(0.2)
    context.password.send_keys('T3st.4321')
    time.sleep(0.2)

# Start session
#def test_06_startSession(context):
    """Hacemos click en iniciar session"""
    context.start = context.driver.find_element(By.ID,'emailButton')
    context.start.click()
    time.sleep(1)


# Scroll to acciones
@when('Browse /client')
def test_07_scrollToAcciones(context):
    """Hacemos scroll hasta la opcion de acciones"""
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0,2000);")
    time.sleep(2)


# Click on Settings
#def test_08_settings(context):
    """Hacemos click en configuraciones"""
    context.settings = context.driver.find_element(By.ID,'settings-button')
    context.settings.click()
    time.sleep(1)

    """Hacemos click en Mi Cuenta"""
    context.miAccount = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[1]/span')
    context.miAccount.click()
    time.sleep(1)

# Tu Informacion
# Edit user
#def test_09_editUser(context):
    """En la seccion Tu informacion, hacemos click para editar usuario"""
    context.edit = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/button/div/div')
    context.edit.click()
    time.sleep(0.5)

# Edit input FirstName
#def test_10_firstName(context):
    """Editamos el nombre a traves del atributo ID"""
    context.first = context.driver.find_element(By.ID,'firstName')
    context.first.click()
    time.sleep(0.3)

    context.first.clear()
    time.sleep(0.5)

    context.first.send_keys('Antonio Rodriguez')
    time.sleep(0.3)

# Edit input LastName
    """Editamos el apellido a traves del atributo ID"""
    context.last = context.driver.find_element(By.ID,'lastName')
    context.last.click()
    time.sleep(0.3)

    context.last.clear()
    time.sleep(0.5)

    context.last.send_keys('Antonio Rodriguez')
    time.sleep(0.3)

# Edit input phoneNumber
    """Editamos el campo phoneNumber a traves del atributo ID"""
    context.phone = context.driver.find_element(By.ID,'phoneNumber')
    context.phone.click()
    time.sleep(0.3)

    context.phone.clear()
    time.sleep(0.5)

    context.phone.send_keys('+34 123456789')
    time.sleep(0.3)

# Cancel changes
#def test_11_cancelarCambios(context):
    """Cancelamos los cambios que hemos generados, haciendo click en el boton CANCELAR"""
    context.cancelar = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/button[2]/div')
    context.cancelar.click()
    time.sleep(0.3)

# Edit purchase
# Scroll to Datos de Facturacion
#def test_12_scrollToPurchase(context):
    """En la seccion Facturacion, scrolleamos hasta el input con placeholder='Billing address'"""
    time.sleep(2)
    context.scroll = context.driver.find_element(By.ID, 'line1')
    context.driver.execute_script("arguments[0].scrollIntoView();", context.scroll)
    time.sleep(2)

# Edit purchase
#def test_13_purchase(context):
    """Hacemos click en el boton editar de la seccion Datos de Facturacion"""
    context.editar = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[2]/button/div/div')
    context.editar.click()
    time.sleep(0.3)

    context.direccion = context.driver.find_element(By.ID,'line1')
    time.sleep(0.2)
    context.direccion.clear()
    time.sleep(0.5)

    context.direccion.send_keys('Calle José Cadalso')
    time.sleep(0.3)

# Coporate Name
    """Hacemos click en boton corporate para editar datos de corporacion"""
    context.corporate = context.driver.find_element(By.ID,'corporateName')
    time.sleep(0.2)

    context.corporate.clear()
    time.sleep(0.5)

    context.corporate.send_keys('Antonio')
    time.sleep(0.3)

# City
    """Hacemos click en el boton de ciudad para editarlo"""
    context.city = context.driver.find_element(By.ID,'city')
    context.city.click()
    time.sleep(0.3)

    context.city.clear()
    time.sleep(0.5)

    context.city.send_keys('Valencia')
    time.sleep(0.3)

# Cancel changes
#def test_14_cancelChange(context):
    """Hacemos click en el boton cancelar para salir de la pantalla de Facturacion"""
    context.cancel = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[2]/button[2]/div')
    context.cancel.click()
    time.sleep(0.3)

# Seccion Settings
# Empleados
#def test_15_empleados(context):
    """Hacemos click en configuraciones"""
    context.settings = context.driver.find_element(By.ID, 'settings-button')
    context.settings.click()
    time.sleep(1)

    """En configuraciones, hacemos click en el boton Lista de Empleados"""
    context.listaEmpleados = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[2]/span')
    context.listaEmpleados.click()
    time.sleep(0.3)

# Agregar empleado
#def test_16_aniadirEmpleado(context):
    """Hacemos click en agregar empleado para visualizar modal y rellenar datos"""
    context.aniadirEmpleado = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/button[1]/div/div')
    context.aniadirEmpleado.click()
    time.sleep(0.3)

# Edit firstName
    """Editar nombre de empleado"""
    context.nombreEmpleado = context.driver.find_element(By.ID,'firstName')
    context.nombreEmpleado.click()
    time.sleep(0.3)

    context.nombreEmpleado.clear()
    time.sleep(0.3)

    context.nombreEmpleado.send_keys('Employee')
    time.sleep(0.3)

# Edit lastName
    """Editar apellido de empelado"""
    context.lastNameEmpleado = context.driver.find_element(By.ID,'lastName')
    context.lastNameEmpleado.click()
    time.sleep(0.3)

    context.lastNameEmpleado.clear()
    time.sleep(0.3)

    context.lastNameEmpleado.send_keys('lastName')
    time.sleep(0.3)

# Edit Email
    """Editar EMail de empleado"""
    context.email = context.driver.find_element(By.ID,'email')
    context.email.click()
    time.sleep(0.3)

    context.email.clear()
    time.sleep(0.3)

    context.email.send_keys('abgrodriguezfarias@gmail.com')
    time.sleep(0.3)

# Add Rol
    """Seleccionar rol de empleado"""
    context.rol = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[4]/div/select')
    context.rol.click()
    time.sleep(0.3)

    context.admin = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[4]/div/select/option[2]')
    context.admin.click()
    time.sleep(0.3)

    context.cancel = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
    context.cancel.click()
    time.sleep(0.5)

#def test_17_importarLista(context):
    """Hacemos click en Importar Lista CSV"""
    context.importarCSV = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/button[2]/div/div')
    context.importarCSV.click()
    time.sleep(0.8)

    # Cancelar y cerrar ventana
    context.cancelar = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
    context.cancelar.click()
    time.sleep(0.5)

#def test_18_filtrarEmpleados(context):
    """Hacemos click en Filtrar empleados - TAGs"""
    context.filtrarEmpleados = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/button/div/div')
    context.filtrarEmpleados.click()
    time.sleep(0.8)

    """Hacemos click en el selector de TAGs"""
    context.selectorTAG = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/select')
    context.selectorTAG.click()
    time.sleep(0.8)
    context.selectorTAG.click()
    time.sleep(0.5)

# Des-seleccionamos el boton de Filtrar empleados
    context.filtrarEmpleados.click()
    time.sleep(0.5)

#def test_19_buscarEmpleado(context):
    """Hacemos click en Buscar Empleado"""
    context.buscarEmpleado = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/input')
    context.buscarEmpleado.click()
    time.sleep(0.5)

    context.buscarEmpleado.send_keys('Rodriguez')
    time.sleep(0.8)
    context.buscarEmpleado.clear()
    time.sleep(0.5)


# Seccion Settings
# Click en Comunicaciones
#def test_20_comunicaciones(self):
    """Hacemos click en configuraciones"""
    context.settings = context.driver.find_element(By.ID, 'settings-button')
    context.settings.click()
    time.sleep(1)

    """En la seccion Comunicaciones, hacer click en el item Comunicaciones"""
    context.comunicaciones = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[3]/span')
    context.comunicaciones.click()
    time.sleep(0.3)

# Click on slideButtons
#def test_21_slideButtons(context):
    """Hacemos click en cada uno de los Slide Buttons de la seccion Comunicaciones"""
    context.seguridadWeb = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button/div[1]')
    context.seguridadWeb.click()
    time.sleep(0.3)
    context.seguridadWeb.click()
    time.sleep(0.3)

    context.suplantacionWeb = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/button/div[1]')
    context.suplantacionWeb.click()
    time.sleep(0.3)
    context.suplantacionWeb.click()
    time.sleep(0.3)

    context.seguridadDispositivos = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[3]/button/div[1]')
    context.seguridadDispositivos.click()
    time.sleep(0.3)
    context.seguridadDispositivos.click()
    time.sleep(0.3)

    context.filtracionesDatos = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[4]/button/div[1]')
    context.filtracionesDatos.click()
    time.sleep(0.3)
    context.filtracionesDatos.click()
    time.sleep(0.3)

    context.seguridadCorreo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[5]/button/div[1]')
    context.seguridadCorreo.click()
    time.sleep(0.3)
    context.seguridadCorreo.click()
    time.sleep(0.3)

    context.formacionPhishing = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[6]/button/div[1]')
    context.formacionPhishing.click()
    time.sleep(0.3)
    context.formacionPhishing.click()
    time.sleep(0.3)

    context.seguridadProveedores = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[7]/button/div[1]')
    context.seguridadProveedores.click()
    time.sleep(0.3)
    context.seguridadProveedores.click()
    time.sleep(0.3)

    context.panelAcciones = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[8]/button/div[1]')
    context.panelAcciones.click()
    time.sleep(0.3)
    context.panelAcciones.click()
    time.sleep(0.3)

    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# Emails con las últimas novedades
# Novedades
#def test_22_novedades(context):
    """En la seccion Comunicaciones, SubSeccion Emails con ultimas novedades, hacemos click
    en Novedades"""
    context.novedades = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div[2]/div[1]/button/div[2]')
    context.novedades.click()
    time.sleep(0.3)
    context.novedades.click()
    time.sleep(0.3)

# Boletín mensual
    """Hacemos click en Boletin Mensual"""
    context.boletinMensual = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div[2]/div[2]/button/div[2]')
    context.boletinMensual.click()
    time.sleep(0.3)
    context.boletinMensual.click()
    time.sleep(0.3)

# Noticias generales y actualizaciones
    """Hacemos click en Noticias Generales y Actualizaciones"""
    context.noticiasGenerales = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div[2]/div[3]/button/div[2]')
    context.noticiasGenerales.click()
    time.sleep(0.3)
    context.noticiasGenerales.click()
    time.sleep(0.3)


# Seccion Settings
# Mi suscripcion
#def test_23_miSuscripcion(context):
    """Hacemos click en configuraciones"""
    context.settings = context.driver.find_element(By.ID, 'settings-button')
    context.settings.click()
    time.sleep(1)

    """en la seccion Mi Suscripcion, hacemos click en Mi Suscripcion"""
    context.suscripcion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[2]/button/div[2]/div/div/button[4]/span')
    context.suscripcion.click()
    time.sleep(2)
    #suscripcion.click()
    #time.sleep(0.3)


# Seccion Tus notificaciones
# Mis notificaciones
#def test_24_misNotificaciones(context):
    """En la Campana, hacemos click en Mis Notificaciones"""
    context.notificaciones = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div[1]/button/div')
    context.notificaciones.click()
    time.sleep(2)


# Avanzamos en el panel de control
# Seccion panel de control
@then('Navigate through the entire application')
def test_25_panelDeControl(context):
    """En el panel de control, Hacemos click en Panel de Control"""
    context.panel = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[2]/span')
    context.panel.click()
    time.sleep(1)

# Seccion listado de acciones
#def test_26_listadoDeAcciones(context):
    """En la seccion del Listado de Acciones, hacemos click en Listado de Acciones"""
    context.listadoDeAcciones = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[3]/span')
    context.listadoDeAcciones.click()
    time.sleep(1)

# Proteccion
# Seguridad de Dispositivos
    """En la seccion de Proteccion, hacemos click en el boton Seguridad de Dispositivos"""
    #def test_27_seguridadDispositivos(context):
    context.proteccion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[1]')
    context.proteccion.click()
    time.sleep(1)

    context.seguridadDispositivos = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[1]/span')
    context.action = ActionChains(context.driver)
    context.action.move_to_element(context.seguridadDispositivos).perform()
    time.sleep(0.5)

    context.amenazasGestionadas = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[2]/span')
    context.action.move_to_element(context.amenazasGestionadas).perform()
    time.sleep(0.5)

    context.seguridadBuzones = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[2]/div/div/button[3]/span')
    context.action.move_to_element(context.seguridadBuzones).perform()
    time.sleep(0.5)

    context.proteccion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[4]/div[1]')
    context.proteccion.click()
    time.sleep(1)


# Seccion Exposicion en Internet
#def test_28_exposicionEnInternet(context):
    """En la seccion de Exposicion en Internet, recorremos la seccion de Exposicion en Internet"""
    context.exposicion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[1]')
    context.exposicion.click()
    time.sleep(1)

    context.seguridadEnCorreo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[1]/span')
    context.action = ActionChains(context.driver)
    context.action.move_to_element(context.seguridadEnCorreo).perform()
    time.sleep(0.5)

    context.filtracionesDeDatos = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[2]/span')
    context.action.move_to_element(context.filtracionesDeDatos).perform()
    time.sleep(0.5)

    context.seguridadDePaginaWeb = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[3]/span')
    context.action.move_to_element(context.seguridadDePaginaWeb).perform()
    time.sleep(0.5)

    context.posiblesSuplantaciones = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[4]/span')
    context.action.move_to_element(context.posiblesSuplantaciones).perform()
    time.sleep(0.5)

    context.seguridadDeProveedores = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[5]/span')
    context.action.move_to_element(context.seguridadDeProveedores).perform()
    time.sleep(0.5)

    context.exposicion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[1]')
    context.exposicion.click()
    time.sleep(1)


#def test_29_formarcioPhishing(context):
    """Hacemos click en Formación de Phishing"""
    context.formacionPhishing = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[6]/span')
    context.formacionPhishing.click()
    time.sleep(1.5)

#def test_30_sorTable(context):
    """Hacemos click en sorTable de Formacion de phishing"""
    context.sorTable = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div/div/div[1]/div[2]/div')
    context.sorTable.click()
    time.sleep(0.5)

    context.sorTable.click()
    time.sleep(0.5)

#def test_31_crearCampania(context):
    """Hacemos click en Crear campaña"""
    context.crearCamania = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div[2]/button[1]/div/div')
    context.crearCamania.click()
    time.sleep(1)

    """Hacemos click en cada una de las campañas"""
    context.paqueteNoRecibido = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div')
    context.paqueteNoRecibido.click()
    time.sleep(0.6)

    context.documentoEscaneado = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div')
    context.documentoEscaneado.click()
    time.sleep(0.6)

    context.facturaElectricidad = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div')
    context.facturaElectricidad.click()
    time.sleep(0.6)

    context.documentoCompartido = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[4]/div')
    context.documentoCompartido.click()
    time.sleep(0.6)

    context.coronavirus = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[5]/div')
    context.coronavirus.click()
    time.sleep(0.6)

    context.comentariosTuTrabajo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div[6]/div')
    context.comentariosTuTrabajo.click()
    time.sleep(0.6)

#def test_32_seleccionarEmpleados(context):
    """Seleccionar empleados de la lista o enviar campaña a todos los empleados"""
    context.seleccionarLista = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div')
    context.seleccionarLista.click()
    time.sleep(0.5)

    """Hacemos click en Seleccionar de la lista"""
    # Buscamos en la barra de busqueda
    context.buscarEmpleado = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div/input')
    context.buscarEmpleado.click()
    time.sleep(0.3)

    context.buscarEmpleado.send_keys('Rodriguez')
    time.sleep(0.8)
    context.buscarEmpleado.clear()
    time.sleep(0.6)

    # Filtrar empleados - TAGs
    context.filtrarEmpleados = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[1]/button/div/div')
    context.filtrarEmpleados.click()
    time.sleep(0.5)

    # Agregar filtro
    context.agregarFiltro = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/button/div/div')
    context.agregarFiltro.click()
    time.sleep(0.5)

    # Quitar filtro
    context.quitarFiltro = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/button/div/div')
    context.quitarFiltro.click()
    time.sleep(0.5)

    # Desplegar selector de TAGs
    context.selectorTAG = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/select')
    context.selectorTAG.click()
    time.sleep(1)
    context.selectorTAG.click()
    time.sleep(0.5)

# Cuando quieres mandar la campaña
#def test_33_datePicker(context):
    """Hacemos click en el Date Picker para desplegar calendario"""
    context.datePicker = context.driver.find_element(By.CLASS_NAME,'datapiker-btn')
    context.datePicker.click()
    time.sleep(0.5)

    # Hacemos click en Phishing header para volver a la pagina inicial de Phishing
    context.phishing = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[6]/span')
    context.phishing.click()
    time.sleep(0.5)

# Resultados de Campanias
#def test_34_resultadosCampanias(context):
    """Hacemos click en el buscador de Resultados de Campañas"""
    context.buscarCampania = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div/input')
    context.buscarCampania.click()
    time.sleep(0.5)

    context.buscarCampania.send_keys('Antonio')
    time.sleep(0.8)
    context.buscarCampania.clear()
    time.sleep(0.5)


# Visión general por empleado
#def test_35_buscarEmpleado(context):
    """Hacemos click en Buscar empleado"""
    context.buscarEmpleado = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div[2]/div/div[1]/div/input')
    context.buscarEmpleado.click()
    time.sleep(0.5)

    context.buscarEmpleado.send_keys('Rodriguez')
    time.sleep(1)
    context.buscarEmpleado.clear()
    time.sleep(0.5)

    """Hacemos click en Filtrar empleado"""
    context.filtrarEmpleado = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div[2]/div/div[1]/button/div/div')
    context.filtrarEmpleado.click()
    time.sleep(0.8)

    # Desplegamos el selector
    context.selectorTAG = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/select')
    context.selectorTAG.click()
    time.sleep(0.8)
    context.selectorTAG.click()
    time.sleep(0.5)

    context.filtrarEmpleado.click()
    time.sleep(0.5)

#Volver a ver tutorial
#def test_36_verTutorial(context):
    """Hacemos click en Volver a ver tutorial"""
    context.volverAVerTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[5]/div/button[1]/div/div')
    context.volverAVerTutorial.click()
    time.sleep(1)

#def test_37_siguiente(context):
    """Hacemos click en siguiente"""
    context.siguiente = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
    context.siguiente.click()
    time.sleep(0.5)

    context.siguiente.click()
    time.sleep(0.5)

#def test_38_estoyListo(context):
    """Hacemos click en Estoy listo"""
    context.estoyListo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
    context.estoyListo.click()
    time.sleep(1.5)

#def test_39_volverAVerTutorial(context):
    """Hacemos click en Volver a ver tutorial"""
    context.volverAVerTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[5]/div/button[1]/div/div')
    context.volverAVerTutorial.click()
    time.sleep(1.5)

#def test_40_saltarTutorial(context):
    """Hacemos click en Saltar tutorial"""
    context.saltarTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
    context.saltarTutorial.click()
    time.sleep(1.5)


# Contactar con soporte
#def test_41_contactarSoporte(context):
    """Hacemos click en Contactar con soporte"""
    context.contactarSoporte = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[2]/a[1]')
    context.contactarSoporte.click()
    time.sleep(1.3)
    context.contactarSoporte.click()
    time.sleep(1.3)

    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# Soporte
#def test_42_chatOnline(context):
    """Hacemos click en Chat Online"""
    context.chatOnline = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[2]/a[1]')
    context.chatOnline.click()
    time.sleep(1)
    context.chatOnline.click()
    time.sleep(1)

# Aviso Legal y Condiciones de Uso
#def test_43_condicionesUso(context):
    """Hacemos click en Aviso Legal y Condiciones de Uso"""
    context.condicionesUso = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[3]/a[1]')
    context.condicionesUso.click()
    time.sleep(1)

    context.driver.switch_to.window(context.driver.window_handles[1])
    time.sleep(1)

    context.driver.execute_script("window.scrollTo(0,2000);")
    time.sleep(1)
    context.driver.close()

    context.driver.switch_to.window(context.driver.window_handles[0])
    time.sleep(0.5)

# Condiciones Generales de Contratación
#def test_44_generalesContratacion(context):
    """Hacemos click en Condiciones Generales de Contratación"""
    context.contratacion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[3]/a[2]')
    context.contratacion.click()
    time.sleep(1)

    context.driver.switch_to.window(context.driver.window_handles[1])
    time.sleep(1)

    context.driver.execute_script("window.scrollTo(0,2000);")
    time.sleep(1)
    context.driver.close()

    context.driver.switch_to.window(context.driver.window_handles[0])
    time.sleep(0.5)


# Política de privacidad
#def test_45_politicaPrivacidad(context):
    """Hacemmos click en Política de privacidad"""
    context.politicaPrivacidad = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[3]/a[3]')
    context.politicaPrivacidad.click()
    time.sleep(1)

    context.driver.switch_to.window(context.driver.window_handles[1])
    time.sleep(1)

    context.driver.execute_script("window.scrollTo(0,2000);")
    time.sleep(1)
    context.driver.close()

    context.driver.switch_to.window(context.driver.window_handles[0])
    time.sleep(0.5)

#def test_46_openCookies(context):
    """Abrimos la configuracion de cookies ubicada en la parte inferior derecha"""
    context.cookies = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/footer/div/div[2]/div[3]/a[4]')
    context.cookies.click()
    time.sleep(1)

#Cookies tecnicas propias
#def test_47_cookiesTecnicas(context):
    """Hacemos click en cookies tecnicas propias"""
    context.cookiesTecnicas = context.driver.find_element(By.ID,'ot-header-id-C0001')
    context.cookiesTecnicas.click()
    time.sleep(1)

#Cookies analiticas
#def test_48_cookiesAnaliticas(context):
    """Hacemos click en cookies analiticas"""
    context.cookiesAnaliticas = context.driver.find_element(By.ID,'ot-header-id-C0002')
    context.cookiesAnaliticas.click()
    time.sleep(1)
    """Clickeamos en el switch"""
    context.switch = context.driver.find_element(By.CLASS_NAME,'ot-switch-nob')
    context.switch.click()
    time.sleep(0.3)
    """Volvemos al estado inicial del switch"""
    context.switch.click()
    time.sleep(1)

#Confirm preferences
#def test_49_confirmarPreferencias(context):
    """Hacemos click en confirmar mis preferencias"""
    context.confirmar = context.driver.find_element(By.CLASS_NAME,'save-preference-btn-handler')
    context.confirmar.click()
    time.sleep(1)



# Close driver
#def test_tearDown(context):
    """Cerramos el driver"""
    context.driver.quit()