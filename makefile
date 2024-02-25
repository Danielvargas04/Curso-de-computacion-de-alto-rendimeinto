all: fig.pdf

dif_num_sumas.x: dif_num_sumas.cpp
	g++ dif_num_sumas.cpp -o dif_num_sumas.x

#%.x : %.cpp
#	g++ $^ -o $@

data.txt: dif_num_sumas.x
	./dif_num_sumas.x > data.txt

fig.pdf: script.gp data.txt
	gnuplot script.gp

.PHONY: clean
clean:
	rm -f *.o *~ *.x *.out 