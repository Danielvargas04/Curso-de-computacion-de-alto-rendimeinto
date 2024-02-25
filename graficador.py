'''Programa pensado para graficar los diferentes datos de los programas en c++ 
para no usar gnuplot si no las ventajas de python y matplotlib'''

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def dispercion(data_path):
    #datos=pd.read_csv('data/histograma.dat',sep=' ', names=['x','y'])
    datos=pd.read_csv(data_path,sep=' ', names=['x','y','z'])
    fig, ax = plt.subplots()
    ax.plot(datos['x'], datos['y'], label = 'Posicion')
    ax.legend()
    ax.grid(True)
    ax.set_title('Oscilador armonico resuelto con Rungekuta')
    plt.show()

def histograma(data_path):
    # Cargar los datos del archivo .dat
    data = pd.read_csv(data_path ,sep='\t', header=0)

    #Funcion teorica
    ejex=np.linspace(2.7, 4.6, 80)
    ejey=norm.pdf(ejex,3.5,0.4)*200

    # Crear el histograma
    fig, ax = plt.subplots()
    ax.hist(data['x'], bins=data['x'].size, weights=data['conteo1'],
             edgecolor='black', label="Seed:1", color= 'blue', alpha=0.3)
    ax.hist(data['x'], bins=data['x'].size, weights=data['conteo2'],
             edgecolor='black', label="Seed:2", color= 'orange', alpha=0.3)
    ax.hist(data['x'], bins=data['x'].size, weights=data['conteo3'],
             edgecolor='black', label="Seed:5", color= 'green', alpha=0.3)
    ax.scatter(data['x'],data['conteo1'], color= 'blue', marker='.', alpha=0.5)
    ax.scatter(data['x'],data['conteo2'], color= 'orange', marker='.', alpha=0.5)
    ax.scatter(data['x'],data['conteo3'], color= 'green', marker='.', alpha=0.5)
    ax.plot(ejex,ejey, color='red', label='Teorica')
    ax.set_xlabel('Numero aleatorio')
    ax.set_ylabel('Conteo')
    ax.set_title('Histograma de un numero aleatorio \n con una distribucion normal centrada en 3.5 con desviación 0.4')
    ax.legend()
    plt.savefig('random_pdf.pdf')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python graficador.py <data_path>")
        sys.exit(1)

    data_path = sys.argv[1]
    
    histograma(data_path)