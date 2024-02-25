all: random_pdf.pdf

random_pdf.x: random_pdf.cpp
	g++ random_pdf.cpp -o random_pdf.x

./data/histograma_rand.dat: random_pdf.x
	./random_pdf.x 1 5000 3.5 0.4 2.7 4.6 50 > ./tmp.dat
	./random_pdf.x 2 5000 3.5 0.4 2.7 4.6 50 | awk '{print $$2}' > ./tmp2.dat
	./random_pdf.x 5 5000 3.5 0.4 2.7 4.6 50 | awk '{print $$2}' > ./tmp3.dat
	paste ./tmp.dat ./tmp2.dat ./tmp3.dat | awk 'NR==1{print "x\tconteo1\tconteo2\tconteo3"} NR>1{print}' > ../data/histograma_rand.dat
	rm ./tmp.dat ./tmp2.dat ./tmp3.dat

random_pdf.pdf: ../graficador.py ../data/histograma_rand.dat
	python3 ../graficador.py ../data/histograma_rand.dat

.PHONY: clean
clean:
	rm -f *.o *~ *.x