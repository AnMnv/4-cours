#include <iostream>

int main(){
    double R1 = 22000;
    double R2 = 2000;

    double h11 = 500.0;
    double h12 = 0.5;
    double h21 = 10.0;
    double h22 = 0.025;

    double det_h = h11*h22 - h12*h21;

    double g1 = 1/R1;
    double g2 = 1/R2;


{
    std::cout << "det_h=" << det_h << std::endl;
    double r11 = det_h/h22;
    double r12 = h12/h22;
    double r21 = -h21/h22;
    double r22 = 1/h22;

    std::cout << "r11=" << r11 << std::endl;
    std::cout << "r12=" << r12 << std::endl;
    std::cout << "r21=" << r21 << std::endl;
    std::cout << "r22=" << r22 << std::endl;



    double R1m = r11-r12;
    double R2m = r12;
    double R3m = r22-r12;
    double rm = r21-r12;

    std::cout << "R1m=" << R1m << std::endl;
    std::cout << "R2m=" << R2m << std::endl;
    std::cout << "R3m=" << R3m << std::endl;
    std::cout << "rm=" << rm << std::endl;


    double g1m = 1/R1m;
    double g2m = 1/R2m;
    double g3m = 1/R3m;
    double gm = rm/R3m/R1m;

    std::cout << "g1=" << g1 << std::endl;
    std::cout << "g2=" << g2 << std::endl;
    std::cout << "g1m=" << g1m << std::endl;
    std::cout << "g2m=" << g2m << std::endl;
    std::cout << "g3m=" << g3m << std::endl;
    std::cout << "gm=" << gm << std::endl;


    double Y11 = g1 + g1m;
    double Y12 = -g1m;
    double Y13 = 0;
    double Y21 = -g1m + gm;
    double Y22 = g1m + g2m + g3m - gm;
    double Y23 = -g2m;
    double Y31 = - gm;
    double Y32 = -g2m +gm;
    double Y33 = g2m + g2;

    std::cout << "Y11=" << Y11 << std::endl;
    std::cout << "Y12=" << Y12 << std::endl;
    std::cout << "Y13=" << Y13 << std::endl;
    std::cout << "Y21=" << Y21 << std::endl;
    std::cout << "Y22=" << Y22 << std::endl;
    std::cout << "Y23=" << Y23 << std::endl;
    std::cout << "Y31=" << Y31 << std::endl;
    std::cout << "Y32=" << Y32 << std::endl;
    std::cout << "Y33=" << Y33 << std::endl;


    double delta_Y33 = Y11*Y22 - Y12*Y21;
    double delta_Y11 = Y22*Y33 - Y23*Y32;
    double delta_Y12 = Y21*Y33 - Y23*Y31;
    double delta_Y1133 = Y22;
    double delta_Y13 = Y21*Y32 - Y22*Y31;

    double detY = Y11*Y22*Y33 + Y12*Y23*Y31 + Y21*Y32*Y13 - Y13*Y22*Y31 - Y21*Y12*Y33 - Y11*Y23*Y32;

    std::cout << "det_Y=" << detY << std::endl;
    std::cout << "delta_Y33=" << delta_Y33 << std::endl;


    std::cout << "delta_Y11=" << delta_Y11 << std::endl;
    std::cout << "delta_Y12=" << delta_Y12 << std::endl;
    std::cout << "delta_Y1133=" << delta_Y1133 << std::endl;
    std::cout << "delta_Y13=" << delta_Y13 << std::endl;


    double det22Y = Y11 * Y33 - Y13 * Y31;
    double det33Y = Y11 * Y22 - Y12 * Y21;

    double Rout = det33Y/detY;


    double Rin = (Rout*delta_Y11 + delta_Y1133) / (Rout*detY+delta_Y33);
    double Rin2 = (delta_Y11/detY + delta_Y1133/delta_Y33)/2;

//std::cout << "(Rout*detY+delta_Y33)=" << (Rout*detY+delta_Y33) << std::endl;
    std::cout << "Rin=" << Rin << " " << Rin2<< " " << delta_Y11/detY << " " << delta_Y1133/delta_Y33 << std::endl;

double Ku = (Rout*delta_Y13)/(Rout*delta_Y11 + delta_Y1133);
double Ki = (delta_Y13)/(Rout*detY + delta_Y1133);
std::cout << "Ku=" << Ku << std::endl;
std::cout << "Ki=" << Ki << std::endl;


    std::cout << Rout << std::endl;

}

    std::cout << std::endl;

{
    double g11 = 1/h11;
    double g12 = - h12/h11;
    double g21 = h21/h11;
    double g22 = det_h/h11;


    std::cout << "g11=" << g11 << std::endl;
    std::cout << "g12=" << g12 << std::endl;
    std::cout << "g21=" << g21 << std::endl;
    std::cout << "g22=" << g22 << std::endl;

    double Y11 = g1 + g11;
    double Y12 = g12;
    double Y21 = g21;
    double Y22 = g22 + g2;

    double detY = Y11*Y22 - Y12*Y21;

    double det11Y = Y22;
    double det22Y = Y11;

    double Rout = det22Y/detY;

    double Rin = (Rout*det11Y+1)/(Rout*detY+det22Y);
    double Rin2 = (det11Y/detY + 1/det22Y)/2;
    std::cout << "Rout_2=" << Rout << std::endl;
    std::cout << "Rin_2=" << Rin << " " << Rin2 << det11Y/detY << " " <<1/det22Y<<std::endl;
}
}
