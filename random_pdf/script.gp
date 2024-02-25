set term pdf
set out "random_pdf.pdf"

# Cargar los datos del archivo
datafile = '../data/histograma_rand.dat'

# Función teórica
set samples 80
ejex = 2.7
ejey(x) = exp(-(x-3.5)**2/(2*0.4**2))/(0.4*sqrt(2*pi))*200

# Configurar el estilo de las líneas y puntos
set style line 1 lc rgb 'blue' pt 7 ps 0.5
set style line 2 lc rgb 'orange' pt 7 ps 0.5
set style line 3 lc rgb 'green' pt 7 ps 0.5
set style line 4 lc rgb 'red' lw 2

# Configurar el histograma y la función teórica
plot datafile using 1:2 with boxes title 'Seed:1' lc rgb 'blue' fill solid 0.3,\
     datafile using 1:3 with boxes title 'Seed:2' lc rgb 'orange' fill solid 0.3,\
     datafile using 1:4 with boxes title 'Seed:5' lc rgb 'green' fill solid 0.3,\
     ejey(x) title 'Teorica' lc rgb 'red'

