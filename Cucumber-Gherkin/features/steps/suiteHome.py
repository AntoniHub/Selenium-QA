import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
options.add_argument('--incognito')
options.add_argument('--start-maximized')



#Open HomePage
@given('User or viewer on the Cyber Guardian homepage')
def test_01_openWeb(context):
    """Se abre el browser en ambiente de TEST, maximiza la ventana y valida encabezado Cyber Guardian en Title"""
    context.driver = webdriver.Chrome()
    context.driver.get('https://antonio-rodriguez.tech')
    context.driver.maximize_window()
    assert 'Antonio Rodriguez' in context.driver.title
    time.sleep(1)

    #Close cookies
    """Identificamos la configuracion de cookies a traves de XPATH para cerrarlo"""
    cookies = context.driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
    cookies.click()
    time.sleep(1)

@when('The user wants to view any of the links at the top of the page')
#View Inicio
def test_03_viewInicio(context):
    """Hacemos click en Inicio"""
    inicio = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[1]/p[1]')
    action = ActionChains(context.driver)
    action.move_to_element(inicio).click().perform()
    time.sleep(0.5)

    #Click on icon path
    """Hacemos click en la flecha desplegable ubicada despues del texto:
    Descubre la plataforma que simplifica la ciberseguridad de las pymes con el nivel
    de protección de los más grandes."""
    icon = context.driver.find_element(By.CLASS_NAME,'fa-chevron-down')
    icon.click()
    time.sleep(0.5)

    #Scroll to button Ver la Demo
    """Hacemos scroll hasta el boton Ver la Demo, ubicado despues del subtitulo:
    Así te ayuda Cyber Guardian a protegerte"""
    verDemo = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/section[4]/div[1]/a/button')
    context.driver.execute_script("arguments[0].scrollIntoView();", verDemo)
    time.sleep(1)

    #See demo in another tab
    """Abrimos en otra ventana el video de la Demo"""
    context.driver.execute_script("window.open('');")
    time.sleep(0.3)
    #change window
    context.driver.switch_to.window(context.driver.window_handles[1])
    time.sleep(0.5)
    #Open video demo
    context.driver.get('https://es-testing.cyberguardian.tech/demo')
    time.sleep(1.5)
    #Play video
    play = context.driver.find_element(By.ID,'video')
    #play.click()
    play.send_keys(Keys.ENTER)
    time.sleep(12)

    #Return HomePage
    """Cerramos la ventana del video de la Demo, volvemos a la pantalla principal y hacemos scroll
    hasta el footer de la WebApp"""
    context.driver.close()
    context.driver.switch_to.window(context.driver.window_handles[0])
    time.sleep(1.5)
    correoElectronico = context.driver.find_element(By.XPATH, '/html/body/div[1]/main/footer/div/div/div[2]/a[2]')
    context.driver.execute_script("arguments[0].scrollIntoView();", correoElectronico)
    time.sleep(1)

@then('He will be able to see each of the links, video, PDF documents and other actions at the top of the page')
#Open Aviso Legal y Condiciones de Uso
def test_08_openLegal(context):
    """Abrimos en otra ventana Aviso Legal y Condiciones de Uso"""
    time.sleep(1)
    context.driver.execute_script("window.open('');")
    context.driver.switch_to.window(context.driver.window_handles[1])
    context.driver.get('https://static.cyberguardian.tech/es/aviso-legal-y-condiciones-de-uso.pdf')
    #assert 'aviso-legal-y-condiciones-de-uso.pdf' in driver.title
    time.sleep(1)

    #Open Condiciones generales de contratacion
    """Abrimos en otra ventana Condiciones generales de contratacion"""
    time.sleep(1)
    context.driver.execute_script("window.open('');")
    context.driver.switch_to.window(context.driver.window_handles[2])
    context.driver.get('https://static.cyberguardian.tech/es/condiciones-generales-de-contratacion.pdf')
    #assert 'condiciones-generales-de-contratacion.pdf' in driver.title
    time.sleep(1)

    #Open Politica de Privacidad
    """Abrimos en otra ventana Politica de Privacidad """
    time.sleep(1)
    context.driver.execute_script("window.open('');")
    context.driver.switch_to.window(context.driver.window_handles[3])
    context.driver.get('https://static.cyberguardian.tech/es/politica-de-privacidad.pdf')
    #assert 'politica-de-privacidad.pdf' in driver.title
    time.sleep(1)

    #Open Politica de Cookies
    """Abrimos en otra ventana Politica de Cookies"""
    time.sleep(1)
    context.driver.execute_script("window.open('');")
    context.driver.switch_to.window(context.driver.window_handles[4])
    context.driver.get('https://static.cyberguardian.tech/es/politica-de-cookies.pdf')
    #assert 'politica-de-cookies.pdf' in driver.title
    time.sleep(1)

    #View all tabs
    """Recorremos todas las ventanas que se han abierto en paralelo"""
    context.driver.switch_to.window(context.driver.window_handles[0])
    time.sleep(1.2)
    context.driver.switch_to.window(context.driver.window_handles[1])
    time.sleep(1.2)
    context.driver.switch_to.window(context.driver.window_handles[2])
    time.sleep(1.2)
    context.driver.switch_to.window(context.driver.window_handles[3])
    time.sleep(1.2)
    context.driver.switch_to.window(context.driver.window_handles[4])
    time.sleep(1.2)

    #Close all tabs
    """Cerramos todas las ventanas abiertas hasta llegar a la pantalla principal"""
    context.driver.close()
    context.driver.switch_to.window(context.driver.window_handles[3])
    time.sleep(1)
    context.driver.close()
    context.driver.switch_to.window(context.driver.window_handles[2])
    time.sleep(1)
    context.driver.close()
    context.driver.switch_to.window(context.driver.window_handles[1])
    time.sleep(1)
    context.driver.close()
    context.driver.switch_to.window(context.driver.window_handles[0])
    time.sleep(1)

    #Open Cookies
    """Abrimos la configuracion de cookies ubicada en la parte inferior derecha"""
    cookies = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/footer/div/div/div[3]/a[4]')
    cookies.click()
    time.sleep(1)

    #Cookies tecnicas propias
    """Hacemos click en cookies tecnicas propias"""
    cookiesTecnicas = context.driver.find_element(By.ID,'ot-header-id-C0001')
    cookiesTecnicas.click()
    time.sleep(1)

    #Cookies analiticas
    """Hacemos click en cookies analiticas"""
    cookiesAnaliticas = context.driver.find_element(By.ID,'ot-header-id-C0002')
    cookiesAnaliticas.click()
    time.sleep(1)
    """Clickeamos en el switch"""
    switch = context.driver.find_element(By.CLASS_NAME,'ot-switch-nob')
    switch.click()
    time.sleep(0.3)
    """Volvemos al estado inicial del switch"""
    switch.click()
    time.sleep(1)

    #Confirm preferences
    """Hacemos click en confirmar mis preferencias"""
    confirmar = context.driver.find_element(By.CLASS_NAME,'save-preference-btn-handler')
    confirmar.click()
    time.sleep(1)

    """Hacemos click en el selector de idiomas para cambiarlo"""
    selectLanguage = context.driver.find_element(By.CLASS_NAME,'language-selector')
    selectLanguage.click()
    time.sleep(1)

    english = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/footer/div/div/div[1]/div/div/select/option[2]')
    english.click()

    selectLanguage.click()
    time.sleep(1.5)

    selectLanguage.click()
    time.sleep(0.8)

    spanish = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/footer/div/div/div[1]/div/div/select/option[1]')
    spanish.click()

    selectLanguage.click()
    time.sleep(0.5)


    #Close driver
    """Cerramos el driver"""
    time.sleep(2)
    context.driver.quit()