all: fig.pdf

prueba.x: dif_num_sumas.cpp
	g++ dif_num_sumas.cpp -o dif_num_sumas.x

#%.x : %.cpp
#	g++ $^ -o $@

data.txt: dif_num_sumas.x
	./dif_num_sumas.x > data.txt

fig.pdf: script.gp data.txt
	gnuplot script.gp

prueba: prueba.x
	./prueba.x 10000 10000

prueba.x: prueba.cpp
	g++ prueba.cpp -o prueba.x

paralel: ./a.out
	for nth in {1..16}; do echo -n "$nth " ; OMP_NUM_THREADS=$nth ./a.out 6800 2 2> /dev/null; done | tee times.txt
	auk '{print &1, 35/$3, 35/$3/$1}' times.txt > metric.txt


.PHONY: clean
clean:
	rm -f *.o *~ *.x *.out 