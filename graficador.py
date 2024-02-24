'''Programa pensado para graficar los diferentes datos de los programas en c++ 
para no usar gnuplot si no las ventajas de python y matplotlib'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def dispercion():
    datos=pd.read_csv('data/histograma.dat',sep=' ', names=['x','y'])
    #datoskuta=pd.read_csv('data/datoskuta.dat',sep=' ', names=['x','y','z'])
    fig, ax = plt.subplots()
    ax.plot(datos['x'], datos['y'], label = 'Posicion')
    ax.legend()
    ax.grid(True)
    ax.set_title('Oscilador armonico resuelto con Rungekuta')
    plt.show()

def histograma():
    # Cargar los datos del archivo .dat
    data = pd.read_csv('data/histograma_rand.dat',sep=' ', header=0)

    # Crear el histograma
    plt.hist(data['x'], bins=data['x'].size, weights=data['Conteo'], edgecolor='black')
    plt.xlabel('x')
    plt.ylabel('Conteo')
    plt.title('Histograma')
    plt.show()

histograma()