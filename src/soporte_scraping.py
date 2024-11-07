# Importación de librerías necesarias para el proyecto

# Automatización de navegadores (Selenium)
# -----------------------------------------------------------------------
from selenium import webdriver                      # Control automático del navegador para realizar scraping web
from selenium.webdriver.chrome.service import Service  # Manejo del servicio de ChromeDriver
from selenium.webdriver.common.by import By         # Selección de elementos en el DOM
from selenium.webdriver.chrome.options import Options  # Configuración de opciones del navegador (headless mode, etc.)
import time                                         # Gestión de pausas y temporización
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Tratamiento y manipulación de datos
# -----------------------------------------------------------------------
import pandas as pd                                 # Manipulación y análisis de datos en estructuras DataFrame
import numpy as np                                  # Cálculos numéricos y manejo de arrays
import datetime                                     # Manipulación de fechas y tiempos

# Visualización de progreso
# -----------------------------------------------------------------------
from tqdm import tqdm                               # Creación de barras de progreso durante bucles

# Manejo de tiempo y solicitudes con espera
# -----------------------------------------------------------------------
from time import sleep                              # Pausas en la ejecución del código


def nombre_productos(urls):
    lista_productos = []
    for url in urls:
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        productos = driver.find_elements("xpath","/html/body/main/div/div[5]/div/div[2]/div[3]/div[2]/div/div")
        sleep(1)

        for _ in range(4):  
            driver.execute_script("window.scrollBy(0, 750);")
            sleep(0.3)  

        for i, _ in enumerate(productos,start=1):
            nombre = driver.find_element("xpath",f"/html/body/main/div/div[5]/div/div[2]/div[3]/div[2]/div/div[{i}]/div/div/div[2]/div[1]/div/a/h3").text
            lista_productos.append(nombre)
    driver.quit()
    return lista_productos

def get_valoraciones(urls):
    return

def df_productos(urls):
    productos = nombre_productos(urls)
    valoraciones = get_valoraciones(urls)
    nombres = []
    colores = []
    categorias = []
    for producto in productos:
        nombre = producto.split(" - ")[0]
        nombres.append(nombre)
        color = producto.split(" - ")[1]
        colores.append(color)
        categoria = producto.split()[0]
        categorias.append(categoria)
    
    df = pd.DataFrame({
        "categoria": categorias,
        "producto" : nombres,
        "color" : colores
    })
    return df