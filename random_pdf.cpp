#include <random>
#include <iostream>
#include <cstdlib>
#include <vector>

//Declaracion de funciones
void compute_pdf(int seed, int nsamples, double mu, double sigma, double xmin, double xmax, int nbins);

int main(int argc, char **argv)
{
  const int SEED = std::atoi(argv[1]);
  const int NSAMPLES = std::atoi(argv[2]);
  const double MU = std::atof(argv[3]);
  const double SIGMA = std::atof(argv[4]);
  const double XMIN = std::atof(argv[5]);
  const double XMAX = std::atof(argv[6]);
  const int NBINS = std::atoi(argv[7]);

  compute_pdf(SEED, NSAMPLES, MU,SIGMA, XMIN, XMAX, NBINS);
}

//Implementacion de funciones
void compute_pdf(int seed, int nsamples, double mu, double sigma, double xmin, double xmax, int nbins)
{
  // random stuff
  std::mt19937 gen(seed);
  std::normal_distribution<double> dis{mu, sigma};
  //histogram stuff
  double ancho_bin = (xmax - xmin) / nbins;
  std::vector<double> histogram(nbins,0);

  for(int n = 0; n < nsamples; n++) {
    double r = dis(gen);
    int bin_indice = (r - xmin) / ancho_bin;
    if (r >= xmin && r < xmax)
    {
      histogram[bin_indice]++;
    }
  }
  //Compute and print the pdf
  std::cout << "x" <<" "<<"Conteo"<< std::endl;
  for (int i = 0; i < nbins; i++)
  {
    std::cout << xmin + i * ancho_bin <<" "<<histogram[i]<< std::endl;
  }
  
}
