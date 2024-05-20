import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


options = Options()
options.binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
options.set_preference("browser.download.folderList",2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","/Data")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")
driver = webdriver.Firefox(executable_path='C:/AntonioRodriguez/GeckoDriver/geckodriver.exe', options=options)


#Open HomePage
@pytest.mark.feature("SetUp")
class TestHomePage:
    def test_01_openWeb(self):
        """Se abre el browser en ambiente de TEST, maximiza la ventana y valida encabezado Cyber Guardian en Title"""
        driver.get('https://es-testing.cyberguardian.tech/home')
        driver.maximize_window()
        assert 'Antonio Rodriguez' in driver.title
        time.sleep(1)

    #Close cookies
    def test_02_closeCookies(self):
        """Identificamos la configuracion de cookies a traves de XPATH para cerrarlo"""
        cookies = driver.find_element(By.CLASS_NAME,'onetrust-close-btn-handler')
        cookies.click()
        time.sleep(1)

@pytest.mark.feature("QuickView")
class TestViewHome:
    #View Inicio
    def test_03_viewInicio(self):
        """Hacemos click en Inicio"""
        inicio = driver.find_element(By.XPATH,'/html/body/div[1]/main/nav/div[2]/div[1]/p[1]')
        action = ActionChains(driver)
        action.move_to_element(inicio).click().perform()
        time.sleep(0.5)

    #Click on icon path
    def test_04_iconPath(self):
        """Hacemos click en la flecha desplegable ubicada despues del texto:
        Descubre la plataforma que simplifica la ciberseguridad de las pymes con el nivel
        de protección de los más grandes."""
        icon = driver.find_element(By.CLASS_NAME,'fa-chevron-down')
        icon.click()
        time.sleep(0.5)

    #Scroll to button Ver la Demo
    #@pytest.mark.xfail
    def test_05_scrollToVerDemo(self):
        """Hacemos scroll hasta el boton Ver la Demo, ubicado despues del subtitulo:
        Así te ayuda Cyber Guardian a protegerte"""
        verDemo = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[4]/div[1]/a/button')
        driver.execute_script("arguments[0].scrollIntoView();", verDemo)
        time.sleep(1)

@pytest.mark.feature("ViewDemo")
class TestViewDemo:
    #See demo in another tab
    def test_06_seeDemo(self):
        """Abrimos en otra ventana el video de la Demo"""
        driver.execute_script("window.open('');")
        time.sleep(0.3)
        #change window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        #Open video demo
        driver.get('https://antonio-rodriguez.tech')
        time.sleep(1.5)
        #Play video
        play = driver.find_element(By.ID,'video')
        #play.click()
        play.send_keys(Keys.ENTER)
        time.sleep(12)

    #Return HomePage
    def test_07_returnHome(self):
        """Cerramos la ventana del video de la Demo, volvemos a la pantalla principal y hacemos scroll
        hasta el footer de la WebApp"""
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1.5)
        correoElectronico = driver.find_element(By.XPATH, '/html/body/div[1]/main/footer/div/div/div[2]/a[2]')
        driver.execute_script("arguments[0].scrollIntoView();", correoElectronico)
        time.sleep(1)

@pytest.mark.feature("Footer")
class TestFooter:
    #Open Aviso Legal y Condiciones de Uso
    def test_08_openLegal(self):
        """Abrimos en otra ventana Aviso Legal y Condiciones de Uso"""
        time.sleep(1)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://antonio-rodriguez.tech')
        #assert 'aviso-legal-y-condiciones-de-uso.pdf' in driver.title
        time.sleep(1)

    #Open Condiciones generales de contratacion
    def test_09_contratacion(self):
        """Abrimos en otra ventana Condiciones generales de contratacion"""
        time.sleep(1)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[2])
        driver.get('https://antonio-rodriguez.tech')
        #assert 'condiciones-generales-de-contratacion.pdf' in driver.title
        time.sleep(1)

    #Open Politica de Privacidad
    def test_10_politicaPrivacidad(self):
        """Abrimos en otra ventana Politica de Privacidad """
        time.sleep(1)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[3])
        driver.get('https://antonio-rodriguez.tech')
        #assert 'politica-de-privacidad.pdf' in driver.title
        time.sleep(1)

    #Open Politica de Cookies
    def test_11_politicaCookies(self):
        """Abrimos en otra ventana Politica de Cookies"""
        time.sleep(1)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[4])
        driver.get('https://antonio-rodriguez.tech')
        #assert 'politica-de-cookies.pdf' in driver.title
        time.sleep(1)

    #View all tabs
    def test_12_viewAllTabs(self):
        """Recorremos todas las ventanas que se han abierto en paralelo"""
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1.2)

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1.2)

        driver.switch_to.window(driver.window_handles[2])
        time.sleep(1.2)

        driver.switch_to.window(driver.window_handles[3])
        time.sleep(1.2)

        driver.switch_to.window(driver.window_handles[4])
        time.sleep(1.2)

    #Close all tabs
    def test_13_closeTabs(self):
        """Cerramos todas las ventanas abiertas hasta llegar a la pantalla principal"""
        driver.close()
        driver.switch_to.window(driver.window_handles[3])
        time.sleep(1)
        driver.close()

        driver.switch_to.window(driver.window_handles[2])
        time.sleep(1)
        driver.close()

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

    #Open Cookies
    def test_14_openCookies(self):
        """Abrimos la configuracion de cookies ubicada en la parte inferior derecha"""
        cookies = driver.find_element(By.XPATH,'/html/body/div[1]/main/footer/div/div/div[3]/a[4]')
        cookies.click()
        time.sleep(1)

    #Cookies tecnicas propias
    def test_15_cookiesTecnicas(self):
        """Hacemos click en cookies tecnicas propias"""
        cookiesTecnicas = driver.find_element(By.ID,'ot-header-id-C0001')
        cookiesTecnicas.click()
        time.sleep(1)

    #Cookies analiticas
    def test_16_cookiesAnaliticas(self):
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
    def test_17_confirmarPreferencias(self):
        """Hacemos click en confirmar mis preferencias"""
        confirmar = driver.find_element(By.CLASS_NAME,'save-preference-btn-handler')
        confirmar.click()
        time.sleep(1)

    def test_18_multiLanguage(self):
        """Hacemos click en el selector de idiomas para cambiarlo"""
        selectLanguage = driver.find_element(By.CLASS_NAME,'language-selector')
        selectLanguage.click()
        time.sleep(1)

        english = driver.find_element(By.XPATH,'/html/body/div[1]/main/footer/div/div/div[1]/div/div/select/option[2]')
        english.click()

        selectLanguage.click()
        time.sleep(1.5)

        selectLanguage.click()
        time.sleep(0.8)

        spanish = driver.find_element(By.XPATH,'/html/body/div[1]/main/footer/div/div/div[1]/div/div/select/option[1]')
        spanish.click()

        selectLanguage.click()
        time.sleep(0.5)


#Close driver
def test_tearDown():
    """Cerramos el driver"""
    time.sleep(2)
    driver.quit()