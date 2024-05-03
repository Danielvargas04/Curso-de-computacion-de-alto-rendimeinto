'''Programa pensado para graficar los diferentes datos de los programas en c++ 
para no usar gnuplot si no las ventajas de python y matplotlib'''

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def dispercion(data_path):
    datos=pd.read_csv(data_path, delim_whitespace=True , names=['N','S', 'E'])

    fig, ax = plt.subplots(2, 1, figsize = (8,10))
    ax[0].scatter(datos['N'], datos['S'], label = 'S', s=10)
    ax[0].set_xlabel("NThreads")
    ax[0].set_ylabel("Speedup")
    ax[0].legend()
    ax[0].grid(True)
    ax[0].set_title('Speed up')

    ax[1].scatter(datos['N'], datos['E'], label = 'E', s=10)
    ax[1].set_xlabel("NThreads")
    ax[1].set_ylabel("Eficiency")
    ax[1].legend()
    ax[1].grid(True)
    ax[1].set_title('Eficiency')
    plt.savefig('image/metrics.pdf')

def histograma(data_path):
    # Cargar los datos del archivo .dat
    data = pd.read_csv(data_path ,sep='\t', header=0)

    #Funcion teorica
    ejex=np.linspace(2.7, 4.6, 50)
    gauss=norm.pdf(ejex,3.5,0.4)
    ejey=gauss

    #ancho de cada bin
    bin_ancho = data['x'][1]-data['x'][0]

    # Crear el histograma
    fig, ax = plt.subplots()
    #ax.hist(data['x'], bins=data['x'].size, weights=data['conteo1'], density =True,
    #         edgecolor='black', label="Seed:1", color= 'blue', alpha=0.3)
    #ax.hist(data['x'], bins=data['x'].size, weights=data['conteo2'], density =True,
    #         edgecolor='black', label="Seed:2", color= 'orange', alpha=0.3)
    #ax.hist(data['x'], bins=data['x'].size, weights=data['conteo3'], density =True,
    #         edgecolor='black', label="Seed:5", color= 'green', alpha=0.3)
    ax.scatter(data['x'],data['p(x)1'], color= 'blue',
                marker='.', alpha=0.5, label="Seed:1")
    ax.scatter(data['x'],data['p(x)2'], color= 'orange',
               marker='.', alpha=0.5, label="Seed:2")
    ax.scatter(data['x'],data['p(x)3'], color= 'green',
                marker='.', alpha=0.5, label="Seed:5")
    ax.plot(ejex,ejey, color='red', label='Teorica')
    ax.set_xlabel('x: Numero aleatorio')
    ax.set_ylabel('p(x): Probabilidad de ocurrencia x')
    ax.set_title('Funcion densidad de probabilidad de un numero aleatorio \n con una distribucion normal centrada en 3.5 con desviación 0.4')
    ax.legend()
    ax.grid(True)
    plt.savefig('random_pdf.pdf')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python graficador.py <data_path>")
        sys.exit(1)

    data_path = sys.argv[1]
    
    dispercion(data_path)