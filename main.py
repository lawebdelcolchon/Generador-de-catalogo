#!/bin/bash/python3
import os
import re
import csv
from reportlab.lib import pagesizes
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


#cargamos fuentes.

directory = './fonts/'

for font_file in os.listdir(directory):
	if font_file.endswith('.ttf'):
		font_name = re.sub(r'\.ttf$', '', font_file, flags=re.IGNORECASE)
		font_name = font_name.lower()
		font_path = os.path.join(directory, font_file)
		pdfmetrics.registerFont(TTFont(font_name, font_path))








def create_pdf(file_name, products):
    # Definir tamaño de la hoja y márgenes
    page_width, page_height = pagesizes.A4
    margin = 2.6 * cm
    top_margin = 3 * cm
    bottom_margin = 1 * cm
    left_margin = 1.5 * cm
    right_margin = margin
    # Crear un canvas de ReportLab
    c = canvas.Canvas(file_name, pagesize=pagesizes.A4)
    # Iterar sobre cada producto y dibujarlos en el PDF
    fondo = True
    for i, product in enumerate(products):
        if fondo:
            c.drawImage(f"images/fondo.png", 0, 0)
            fondo = False
        # Cálculos para posicionar el rectángulo y la imagen
        x = left_margin
        y = page_height - top_margin - (i % 5) * (5 * cm)
        #imprimimos la barra
        c.drawImage(f"images/barra.png", x, y - 5 * cm)
        #imprimimos la imagen
        c.drawImage(f"images/{product['image']}", x + 0.5 * cm, y - 3.5 * cm, 3 * cm, 3 * cm)
        # Cálculos para posicionar las descripciones
        c.drawString(x + 4 * cm, y - 1 * cm, f"Código: ({product['code']})-     {product['name']}")
        c.drawString(x + 4 * cm, y - 1.5 * cm, f"Descripción: {product['description']}")
        c.drawString(x + 4 * cm, y - 3 * cm, f"Unidades por bulto: {product['units_per_bundle']}")
        c.drawString(x + 4 * cm, y - 3.8 * cm, f"Precio: ${product['price']}")
        # Agregar una nueva página después de cada sexto producto
        if (i + 1) % 5 == 0:
            c.showPage()
            fondo = True
    # Guardar el PDF
    c.save()

# Leer los datos del archivo CSV
products = []
with open("csv/products.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        products.append(row)

# Generar el PDF
create_pdf("result/products.pdf", products)
