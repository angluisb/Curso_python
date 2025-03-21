from flask import Flask, render_template, request
import funciones as fn


app = Flask(__name__)

archivo_csv='booklist2000.csv'
lista_libros=fn.lee_archivo_csv(archivo_csv)
diccionario_titulos = fn.crea_diccionario(lista_libros, 'title')
diccionario_autores = fn.crea_diccionario(lista_libros, 'author')
diccionario_id = fn.crea_diccionario(lista_libros, 'id')

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/titulos', methods=['POST','GET'])
def busqueda_titulo():
    resultado = []
    if request.method == 'POST':
        titulo = request.form['titulo']
        resultado = fn.busca_en_diccionario(diccionario_titulos, titulo)
    return render_template('titulos.html', lista_libros=resultado)

@app.route('/libro/<id_libro>', methods=['GET'])
def libro(id_libro:str):
    """Pagina de informacion de un libro"""
    if id_libro in diccionario_id:
        book = diccionario_id[id_libro]
        return render_template('libro.html', libro=book)
    else:
        return render_template('libro.html', libro=None)
    
@app.route('/titulo', methods=['POST','GET'])
def title():
    print(request.method)
    resultado = []
    if request.method == 'POST':
        titulo = request.form.get['searchInput','']
        resultado = fn.busca_en_diccionario(diccionario_titulos, titulo)
    return render_template('titulo .html', lista_libros=resultado)

if __name__ == "__main__":
    app.run(debug=True)