# ESTE EJERCICIO SE HA REALIZADO CON PYTHON Y SELENIUM
# SE HA UTILIZADO EL IDE PYCHARM CON COMPLEMENTO SELENIUM PERO SE PUEDE EJECUTAR CON LA CONSOLA
# SIEMPRE QUE ESTE INSTALADO SELENIUM Y WEBDRIVER_MANAGER UTILIZANDO EL COMANDO PIP

# Librerias importadas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Ruta de chromedriver
driver_service = Service(executable_path="./chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

# Acceso a google.com
driver.get("http://www.google.com/")

# Maximizar ventana
driver.maximize_window()

# Rechazar cookies
driver.find_element("xpath", "id('CXQnmb')//*[text()='Rechazar todo']").click()

#Escribir y buscar la palabra automatizacion
driver.find_element("xpath", "//form//textarea").send_keys("automatización")
driver.implicitly_wait(10)
driver.find_element("xpath", "(//*[@value='Buscar con Google'])[2]").click()
driver.implicitly_wait(10)

# Hacer click en el enlace de wikipedia que lleva a la entrada automatizacion.
driver.find_element("xpath", "//a[@href='https://es.wikipedia.org/wiki/Automatizaci%C3%B3n']").click()

# Vas al apartado Historia en la entrada automatizacion y saca una captura de pantalla
driver.find_element("xpath", "//a[@href='#Historia']").click()
driver.get_screenshot_as_file("./img/historiaAutomatizacion.png")

# Comprueba que en el primer parrafo del apartado historia esta la palabra primer para comprobar la primera fecha de una automatizacion.
try:
    assert ("primer" or "primera") in driver.find_element("xpath", "//*[@id='Historia_temprana']/..//following-sibling::p[1]").text
    print("===========================================")
    print("Word primer o primera found in first paragraph of history of automation succesfully.")
except:
    print("===========================================")
    print("Word primer o primera not found in first paragraph of history of automation.")
finally:
    print("===========================================")
    print("TEST FINISHED!")