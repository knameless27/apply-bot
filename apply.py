from selenium import webdriver
import time

# PATH = "C:/Program Files (x86)/chromedriver.exe"
# driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome()

driver.get("https://knameless.ca")

time.sleep(100)
# Configura el controlador de Chrome (asegúrate de proporcionar la ruta correcta al archivo ejecutable)
# driver = webdriver.Chrome('./chromedriver.exe')

# Navega a la página de aplicación de empleo
# driver.get('youtube.com')

# Simula la interacción del usuario (por ejemplo, llena un formulario)
# nombre_input = driver.find_element_by_name('nombre')
# nombre_input.send_keys('Tu Nombre')

# Continúa llenando los campos y realizando acciones según sea necesario

# Envía la aplicación
# submit_button = driver.find_element_by_id('search-icon-legacy')
# print(submit_button)
# submit_button.click()

# Cierra el navegador después de completar la aplicación
# driver.quit()
