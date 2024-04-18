from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def mostrar_contenido_carpeta():
    # Ruta de la carpeta que deseas mostrar
    ruta_carpeta = '/media/synapsido/FW-BACKUP/Grover4.iMovieProject/Media'

    # Obtener la lista de archivos en la carpeta con sus tamaños
    archivos = []
    for archivo in os.listdir(ruta_carpeta):
        ruta_completa = os.path.join(ruta_carpeta, archivo)
        if os.path.isfile(ruta_completa):
            tamanio = os.path.getsize(ruta_completa)
            archivos.append({'nombre': archivo, 'tamanio': tamanio})

    # Pasar la lista de archivos a una plantilla HTML para mostrarlos
    return render_template('content.html', archivos=archivos)

@app.route('/descargar/<path:filename>')
def descargar_archivo(filename):
    # Ruta de la carpeta que contiene los archivos
    carpeta_archivos = '/media/synapsido/FW-BACKUP/Grover4.iMovieProject/Media'
    return send_from_directory(carpeta_archivos, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)