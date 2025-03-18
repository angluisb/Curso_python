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
        
class Pelicula:
    '''Clase para manejar las películas'''
    def __init__(self,id_pelicula,titulo_pelicula,fecha_lanzamiento,url_poster):
        '''Inicializa la película'''
        self.id_pelicula = id_pelicula
        self.titulo_pelicula = titulo_pelicula
        self.fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, '%Y-%m-%d').date()
        self.url_poster = url_poster
    
    def to_dict(self):
        '''Devuelve un diccionario con los datos de la película'''
        return {
            'id_pelicula': self.id_pelicula,
            'titulo_pelicula': self.titulo_pelicula,
            'fecha_lanzamiento': self.fecha_lanzamiento,
            'url_poster': self.url_poster
        }

class Relaciones:
    '''Clase para manejar las relaciones entre actores y películas'''
    def __init__(self,id_relacion,id_estrella,id_pelicula):
        '''Inicializa la relación'''
        self.id_relacion = id_relacion
        self.id_estrella = id_estrella
        self.id_pelicula = id_pelicula
    
    def to_dict(self):
        '''Devuelve un diccionario con los datos de la relación'''  
        return {
            'id_relacion': self.id_relacion,
            'id_estrella': self.id_estrella,
            'id_pelicula': self.id_pelicula
        }

class User:
    '''Clase para manejar los usuarios'''
    def __init__(self,username,nombre_completo,email,password,admin):
        '''Inicializa el usuario'''
        self.username = username
        self.nombre_completo = nombre_completo
        self.email = email
        self.password = password
        self.admin = admin
        
    def to_dict(self):
        '''Devuelve un diccionario con los datos del usuario'''
        return {
            'username': self.username,
            'nombre_completo': self.nombre_completo,
            'email': self.email,
            'password': self.password,
            'admin': self.admin
        }
    def hash_string(self, string):
        '''Devuelve el hash de una cadena'''
        return hashlib.md5(string.encode()).hexdigest()
    
    
class SistemaCine:
    '''Clase para manejar el sistema de cine'''
    def __init__(self):
        '''Inicializa el sistema'''
        self.actores = {}
        self.peliculas = {}
        self.relaciones = {}
        self.usuarios = {}
        
    def cargar_csv(self,archivo,clase):
        '''Carga los actores desde un archivo csv'''
        with open(archivo, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            next(reader)
            for row in reader:
                if clase == Actor:
                    objeto = Actor(**row)
                    self.actores[objeto.id_estrella] = objeto
                elif clase == Pelicula:
                    objeto = Pelicula(**row)
                    self.peliculas[objeto.id_pelicula] = objeto
                elif clase == Relaciones:
                    objeto = Relaciones(**row)
                    self.relaciones[objeto.id_relacion] = objeto
                elif clase == User:
                    objeto = User(**row)
                    self.usuarios[objeto.username] = objeto
                    
if __name__ == '__main__':
    archivo_actores = "data/movies_db - actores.csv"
    sistema=SistemaCine()
    sistema.cargar_csv(archivo_actores, Actor)
    actores = sistema.actores
    for id_estrella, actor in actores.items():
        print(f"{id_estrella}: {actor.nombre:35s} - {actor.fecha_nacimiento}")
