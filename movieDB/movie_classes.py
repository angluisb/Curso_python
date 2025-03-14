''' Clases para manejar la manipulación de las películas '''
import csv
import os
import hashlib
from datetime import datetime

class Actor:
    ''' Clase para manejar los actores '''
    def __init__(self, id_estrella:int, nombre:str, fecha_nacimiento:str, ciudad_nacimiento:str, url_imagen:str, username:str):
        self.nombre = nombre
        self.id_estrella = id_estrella
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.url_imagen = url_imagen
        self.username = username

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    def to_dict(self):
        ''' Devuelve un diccionario con los datos del actor '''
        return {
            'id_estrella': self.id_estrella,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'ciudad_nacimiento': self.ciudad_nacimiento,
            'url_imagen': self.url_imagen,
            'username': self.username
        }
        
if __name__ == '__main__':
    archivo = "data/movies_db - actores.csv"
    actores={}
    with open(archivo, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        next(reader)
        for row in reader:
            actor = Actor(**row)
            actores[actor.id_estrella] = actor
    for id_estrella, actor in actores.items():
        print(f'{id_estrella}: {actor.nombre}')