#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch2/catch_test_macros.hpp"

#include <cmath>
#include "vector_ops.hpp"

TEST_CASE( "Mean of a vector is computed", "[mean]" ) {
    //REQUIRE( factorial(0) == 1 );
    std::vector<double> vec1(5.0,0);
    std::vector<double> vec2(5,1);
    std::vector<double> vec3(1001,0);
        std::iota(vec3.begin(), vec3.end(), 0.0);
    std::vector<double> vec4(5,-5);
    std::vector<double> vec5(100,0);
        std::iota(vec5.begin(), vec5.end(), 1.0);
    std::vector<double> vec6(10000001,0);
        std::iota(vec6.begin(), vec6.end(), 0.0);
    std::vector<double> vec7(100,0.01);
    /*Metodo para error relativo con tol=1e-3:
            |Valor teorico - Valor experimental| < tol*(|Valor teorico| + 1)
      esto con el objetivo de evitar la division por 0 y que tol*(valor teorico)
      sea 0 en caso de que el valor teorico sea 0. 
    */
    REQUIRE( std::fabs(mean(vec1) - 0.0) < 1e-3*(0.0 + 1.0));
    REQUIRE( std::fabs(mean(vec2) - 1.0) < 1e-3*(1.0 + 1.0));
    REQUIRE( std::fabs(mean(vec3) - 500.0) < 1e-3*(500.0 + 1.0));
    REQUIRE( std::fabs(mean(vec4) - (-5.0)) < 1e-3*(5.0 + 1.0));
    REQUIRE( std::fabs(mean(vec5) - (50.5)) < 1e-3*(50.5 + 1.0));
    REQUIRE( std::fabs(mean(vec6) - (5000000)) < 1e-3*(5000000 + 1.0));
    REQUIRE( std::fabs(mean(vec7) - (0.01)) < 1e-3*(0.01 + 1.0));
    
}