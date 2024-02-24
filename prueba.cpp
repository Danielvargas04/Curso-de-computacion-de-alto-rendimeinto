#include <random>
#include <iostream>

int main(void)
{
    double xmin=2.7, xmax=4.6;
    int nbins = 8;
    std::mt19937 gen(18);
    std::normal_distribution<double> dis{3.5, 0.4};
    // declare the data struct
    double ancho_bin = (xmax - xmin) / nbins;
    std::vector<double> histogram(nbins,0);

    for (int i = 0; i < 50; ++i)
    {
        double r = dis(gen);
        int bin_indice = (r - xmin)/ancho_bin;
        if (r >= xmin && r <= xmax){
            std::cout << r <<" "<<bin_indice<< std::endl;
        }
    }

    return 0;
}
