#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    ofstream file ("layer1.txt");

    double u_x = 1.3;
    double u_y = u_x*pow(3,0.5);
    double Nx = 30;
    double Ny = 20;
    double Na = 2*Ny*Nx;
    double a_x = Nx*u_x;
    double a_y = Ny*u_y;
    vector<vector<double> > P;

/// Create 1200 position vectors
    for (int i = 0; i <Nx; i++){
        vector<double> temp;
        for (int j = 0; j <3; j++) {temp.push_back(0);}
        temp[0] = i*u_x;
        P.push_back(temp);
    }
    for (int i=0; i <Nx; i++){
        vector<double> temp;
        for (int j = 0; j <3; j++) {temp.push_back(0);}
        temp[0] = (0.5+i)*u_x;
        temp[1] = u_y*0.5;
        P.push_back(temp);
    }
    for (int i=0; i <2*Nx*(Ny-1); i++){
                vector<double> pn;
        for (int j = 0; j <3; j++) {pn.push_back(0);}
        pn[0]=P[i][0];
        pn[1]=P[i][1]+u_y;
        pn[2]=P[i][2];
        P.push_back(pn);
    }

    for(int i=0;i<1200;i++){
            file << P[i][0] << " " << P[i][1] << " " << P[i][2] << endl;
    }

    for(int i=0;i<1200;i++){
            file << P[i][0] << " " << P[i][1] << " " << P[i][2]+u_x << endl;
    }
    file << endl;

    file.close();

    return 0;
}
