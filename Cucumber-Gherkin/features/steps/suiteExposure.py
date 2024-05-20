import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--start-maximized')
options.add_argument("--disable-popup-blocking")


"""Test E2E de la seccion Exposicion en Internet"""
@given('Clicking on Exposure')
def test_01_openHome(context):
    """Abrimos el driver, la web en ambiente de TEST y maximizamos la ventana"""
    context.driver = webdriver.Chrome()
    context.driver.get('https://antonio-rodriguez.tech')
    context.driver.maximize_window()
    assert 'Antonio Rodriguez' in context.driver.title
    time.sleep(1)

    """Cerramos la configuracion de cookies"""
    context.cookies = context.driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
    context.cookies.click()
    time.sleep(0.5)

# Click on LogIn
    """Hacemos click en el LogIn"""
    context.logIn = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[2]/button[1]/div')
    context.driver.execute_script("arguments[0].scrollIntoView();", context.logIn)
    context.logIn.click()
    time.sleep(1)

# Send mail
    """Ingresamos la direccion de Email"""
    context.mail = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/input')
    context.mail.click()
    time.sleep(0.2)
    context.mail.send_keys('abgrodriguezfarias@gmail.com')
    time.sleep(0.2)

# Send password
    """Ingresamos el password"""
    context.password = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[3]/input')
    context.password.click()
    time.sleep(0.2)
    context.password.send_keys('T3st.4321')
    time.sleep(0.2)

# Start session
    """Hacemos click en iniciar session"""
    context.start = context.driver.find_element(By.ID,'emailButton')
    context.start.click()
    time.sleep(10)

@when('Begin with exposure')
def test_07_exposicionEnInternet(context):
    """Hacemos click en la seccion Exposicion para ver su contenido"""
    context.exposicion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[1]')
    context.exposicion.click()
    time.sleep(1.5)


@then('Switch to all items')
def test_08_seguridadDeCorreo(context):
    """Hacemos click en la Subseccion de Seguridad de Correo en Exposicion en Internet"""
    context.seguridadDeCorreo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[1]/span')
    context.seguridadDeCorreo.click()
    time.sleep(1.5)

    context.sorTable1 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div')
    context.sorTable1.click()
    time.sleep(0.5)
    context.sorTable1.click()
    time.sleep(0.3)

    context.sorTable2 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div/div[1]/div[2]/div')
    context.sorTable2.click()
    time.sleep(0.5)
    context.sorTable2.click()
    time.sleep(0.3)


    """Hacemos click en ver tutorial"""
    context.verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
    context.verTutorial.click()
    time.sleep(1)

    """Hacemos click en Siguiente"""
    context.siguiente = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
    context.siguiente.click()
    time.sleep(0.5)

    context.siguiente.click()
    time.sleep(0.5)

    """Hacemos click en Estoy listo"""
    context.estoyListo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
    context.estoyListo.click()
    time.sleep(1)

    """Hacemos nuevamente click en ver tutorial"""
    context.verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
    context.verTutorial.click()
    time.sleep(1)

    """Hacemos click en Saltar tutorial"""
    context.saltarTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
    context.saltarTutorial.click()
    time.sleep(1)


    """Cambiamos a la seccion Filtraciones de Datos"""
#@then('Switch to data filtrations')
#def test_18_filtracionesDeDatos(context):
    """Hacemos click en Filtraciones de Datos"""
    context.exposicion = context.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
    context.exposicion.click()
    time.sleep(1.5)

    context.filtracionesDatos = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[2]/span')
    context.filtracionesDatos.click()
    time.sleep(1.5)

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    """Buscamos un empleado de la lista de correos en Filtraciones de Datos -> Vision por empleados"""
    context.buscarEmpleados = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/div/div[2]/div/div[1]/div/input')
    context.buscarEmpleados.click()
    time.sleep(1)

    context.buscarEmpleados.send_keys('Antonio')
    time.sleep(1)
    context.buscarEmpleados.send_keys(Keys.BACKSPACE*2)
    time.sleep(1)

    context.buscarEmpleados.send_keys('Rodriguez')
    time.sleep(1)
    context.buscarEmpleados.send_keys(Keys.BACKSPACE*3)
    time.sleep(1)

    context.buscarEmpleados.send_keys('Farias')
    time.sleep(1)
    context.buscarEmpleados.send_keys(Keys.BACKSPACE*2)
    time.sleep(1.5)

    """Hacemos click en ver tutorial"""
    verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[6]/div/button[1]/div/div')
    verTutorial.click()
    time.sleep(1)

    """Hacemos click en Siguiente"""
    context.siguiente = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
    context.siguiente.click()
    time.sleep(0.5)

    context.siguiente.click()
    time.sleep(0.5)

    context.siguiente.click()
    time.sleep(0.5)

    """Hacemos click en Estoy listo"""
    context.estoyListo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
    context.estoyListo.click()
    time.sleep(1)

    """Hacemos nuevamente click en Volver a ver tutorial"""
    context.verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[6]/div/button[1]/div/div')
    context.verTutorial.click()
    time.sleep(1)

    """Hacemos click en Saltar tutorial"""
    context.saltarTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
    context.saltarTutorial.click()
    time.sleep(1)


    """Ahora nos vamos a la seccion de Seguridad de Pagina WEB"""
#@then('Switch to website security')
#def test_seguridadPaginaWEB(context):
    """Hacemos click en la Subseccion Seguridad de Pagina WEB"""
    context.exposicion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
    context.exposicion.click()
    time.sleep(1.5)

    context.seguridadDePaginaWEB = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[3]/span')
    context.seguridadDePaginaWEB.click()
    time.sleep(1.5)

    """HAcemos click en sorTable de Seguridad de Pagina WEB"""
    context.sorTable = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div')
    context.sorTable.click()
    time.sleep(0.5)

    context.sorTable.click()
    time.sleep(0.5)

    """Hacemos click en el icono de seleccionar los dominios WEBs que tenemos agregados"""
    context.selectIcon = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/div/div/select')
    context.selectIcon.click()
    time.sleep(1)

    """Hacemos click en el boton para agregar dominio WEB"""
    context.agregarDominio = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/button[1]/div/div')
    context.agregarDominio.click()
    time.sleep(1)

    """Ingresamos un Dominio WEB"""
    context.barraBusqueda = context.driver.find_element(By.ID,'website')
    context.barraBusqueda.send_keys('www.AntonioRodriguez.tech')
    time.sleep(1.5)
    context.barraBusqueda.send_keys(Keys.BACKSPACE*22)
    time.sleep(1)

    context.cancelar = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
    context.cancelar.click()
    time.sleep(1.5)

    """Hacemos click en quitar dominio en Seguridad de Pagina WEB
    # Si hay solo un dominio agregado, este Test fallara porque no estara habilitado el boton
    context.quitarDominio = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/button[2]/div/div')
    context.quitarDominio.click()
    time.sleep(1)

    context.cancelar = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
    context.cancelar.click()
    time.sleep(1)"""

    """Hacemos click en Ver mas del item de Ataques de intermediario"""
    context.verMas1 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div')
    context.verMas1.click()
    time.sleep(2.5)

    context.entendido1 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
    context.entendido1.click()
    time.sleep(1)

    """Hacemos click en Ver mas del item Ataques de ClickJacking en Seguridad de Pagina WEB"""
    context.verMas2 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div')
    context.verMas2.click()
    time.sleep(2.5)

    context.entendido2 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
    context.entendido2.click()
    time.sleep(1)

    """Hacemos click en Ver mas del item Cross-Site Scripting en Seguridad de Pagina WEB"""
    context.verMas3 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div[2]/div')
    context.verMas3.click()
    time.sleep(2.5)

    context.entendido3 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
    context.entendido3.click()
    time.sleep(1)

    """Hacemos click en Ver mas del item Ataques DDOS en Seguridad de Pagina WEB"""
    context.verMas4 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/div')
    context.verMas4.click()
    time.sleep(2.5)

    context.entendido4 = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button/div')
    context.entendido4.click()
    time.sleep(1)

    """Hacemos click en Volver a ver tutorial"""
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    context.verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
    context.verTutorial.click()
    time.sleep(1)

    """Hacemos click en Siguiente"""
    context.siguiente = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
    context.siguiente.click()
    time.sleep(0.5)

    context.siguiente.click()
    time.sleep(0.5)

    """Hacemos click en Estoy listo"""
    context.estoyListo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
    context.estoyListo.click()
    time.sleep(1)

    """Hacemos nuevamente click en Volver a ver tutorial"""
    context.verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
    context.verTutorial.click()
    time.sleep(1)

    """Hacemos click en Saltar tutorial"""
    context.saltarTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
    context.saltarTutorial.click()
    time.sleep(1)


#@then('Switch to possible impersonations')
#def test_posiblesSuplantaciones(context):
    """Hacemos click en la Subseccion de Posibles Suplantaciones en Exposicion en Internet"""
    context.exposicion = context.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
    context.exposicion.click()
    time.sleep(1.5)

    context.posibleSuplantaciones = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[4]/span')
    context.posibleSuplantaciones.click()
    time.sleep(1.5)

    """Hacemos click en sorTable de Posibles Suplantaciones"""
    context.sorTable = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div')
    context.sorTable.click()
    time.sleep(1)

    context.sorTable.click()
    time.sleep(1)

    """Hacemos click en el icono para seleccionar dominio agregados"""
    context.selectDominio = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/div/div[1]/div/div/select')
    context.selectDominio.click()
    time.sleep(1.5)

    """Hacemos click en el boton de añadir otra web"""
    context.otraWeb = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[3]/div/div[1]/div/div[1]/button/div/div')
    context.otraWeb.click()
    time.sleep(1.5)

    """Hacemos click en la barra de busqueda para agregar URL en Posibles Suplantaciones"""
    context.agregarURL = context.driver.find_element(By.ID,'website')
    context.agregarURL.click()
    time.sleep(1)

    context.agregarURL.send_keys('www.CyberGuardian.tech')
    time.sleep(1.5)

    context.agregarURL.clear()
    time.sleep(1)

    context.cancelar = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
    context.cancelar.click()
    time.sleep(1)

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    """Hacemos click en ver tutorial"""
    context.verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
    context.verTutorial.click()
    time.sleep(1)

    """Hacemos click en Siguiente"""
    context.siguiente = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
    context.siguiente.click()
    time.sleep(0.5)

    context.siguiente.click()
    time.sleep(0.5)

    """Hacemos click en Estoy listo"""
    context.estoyListo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
    context.estoyListo.click()
    time.sleep(1)

    """Hacemos nuevamente click en Volver a ver tutorial"""
    context.verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/button[1]/div/div')
    context.verTutorial.click()
    time.sleep(1)

    """Hacemos click en Saltar tutorial"""
    context.saltarTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
    context.saltarTutorial.click()
    time.sleep(1)


#@then('Switch to supplier security')
#def test_seguridadProveedores(context):
    """Hacemos click en Seguridad de Proveedores"""
    context.exposicion = context.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
    context.exposicion.click()
    time.sleep(1.5)

    context.seguridadProveedores = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/div[2]/div/div/button[5]/span')
    context.seguridadProveedores.click()
    time.sleep(1.5)

    """Hacemos click en Añade tu primer proveedor"""
    context.agregarProveedor = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[4]/div/div/div[2]/div/div/button/div/div')
    context.agregarProveedor.click()
    time.sleep(1.5)

    context.nameSupplier = context.driver.find_element(By.ID,'name')
    context.nameSupplier.click()
    time.sleep(0.5)

    context.nameSupplier.send_keys('Factum - CyberGuardian')
    time.sleep(1)

    # Hacemos click en el selector para desplegar cada una de las opciones
    context.selectSector = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/select')
    context.selectSector.click()
    time.sleep(1)

    # Seleccionamos la opcion 10 -> Transporte (excluida la aviacion)
    context.selectTransporte = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/select/option[10]')
    context.selectTransporte.click()
    time.sleep(1)

    context.dominioProveedor = context.driver.find_element(By.ID,'domain')
    context.dominioProveedor.click()
    time.sleep(0.5)
    context.dominioProveedor.send_keys('www.Proveedor.es')
    time.sleep(1)

    context.correoProveedor = context.driver.find_element(By.ID,'atEmail')
    context.correoProveedor.click()
    time.sleep(0.5)
    context.correoProveedor.clear()
    time.sleep(0.5)
    context.correoProveedor.send_keys('Proveedor.Dominio.ES')
    time.sleep(1)

    context.cancelar = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/button[2]/div')
    context.cancelar.click()
    time.sleep(1)

    """Hacemos click en Volver a ver tutorial"""
    context.verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
    context.verTutorial.click()
    time.sleep(1)

    """Hacemos click en Siguiente"""
    context.siguiente = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[1]/div')
    context.siguiente.click()
    time.sleep(0.5)

    context.siguiente.click()
    time.sleep(0.5)

    context.siguiente.click()
    time.sleep(0.5)

    """Hacemos click en Estoy listo"""
    context.estoyListo = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button/div')
    context.estoyListo.click()
    time.sleep(1)

    """Hacemos nuevamente click en Volver a ver tutorial"""
    context.verTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[5]/div/button[1]/div/div')
    context.verTutorial.click()
    time.sleep(1)

    """Hacemos click en Saltar tutorial"""
    context.saltarTutorial = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/div')
    context.saltarTutorial.click()
    time.sleep(1)

    """Hacemos click nuevamente en Exposicion en Internet para cerrar"""
    context.exposicion = context.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/button[5]/span/div')
    context.exposicion.click()
    time.sleep(0.5)


#def test_tearDown():
    """Cerramos el driver"""
    context.driver.quit()