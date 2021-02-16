#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <sstream>
#include <ctime>
#include <cstdlib>

using namespace std;

    double e = 1;
    double sig = 1;

/// Potential between two particles
double U(vector<double> r_i, vector<double> r_j, vector<double> S_i, vector<double> S_j)
{
    double r_1 = r_j[0]-r_i[0];
    double r_2 = r_j[1]-r_i[1];
    double r_3 = r_j[2]-r_i[2];
    double dot1 = S_i[0]*S_j[0]+S_i[1]*S_j[1]+S_i[2]*S_j[2];
    double dot2 = r_1*S_i[0]+r_2*S_i[1]+r_3*S_i[2];
    double dot3 = r_1*S_j[0]+r_2*S_j[1]+r_3*S_j[2];
    double d = pow((pow(r_1,2)+pow(r_2,2)+pow(r_3,2)),0.5);
    double pot = 4*e*pow(sig/d,12)-e*pow(sig,3)*((dot1/pow(d,3))-(3*(dot2)*(dot3)/pow(d,5)));
    return pot;
}
    double u_x = 1.3;
    double u_y = u_x*pow(3,0.5);
    int Nx = 30;
    int Ny = 20;
    int Na = 2*Ny*Nx;
    double a_x = Nx*u_x;
    double a_y = Ny*u_y;

/// Energy of configuration with position vectors P1 and spin vectors S1
double U_tot(vector<vector<double> > P1, vector<vector<double> > S1)
{
    double U_t;
    double U_j;
    vector <double> v;
    for (int i = 0; i <3; i++){v.push_back(0);}
    for (int j=0; j<2*Na; j++){
            U_j=0;
            for (int i=0; i<2*Na; i++){
                if (i!=j){
                    double dx = P1[i][0]-P1[j][0];
                    double dy = P1[i][1]-P1[j][1];
                    v[0]=P1[i][0];
                    v[1]=P1[i][1];
                    v[2]=P1[i][2];
                    if (dx >  a_x/2){v[0] -= a_x;}
                    if (dx < -a_x/2){v[0] += a_x;}
                    if (dy >  a_y/2){v[1] -= a_y;}
                    if (dy < -a_y/2){v[1] += a_y;}
                    U_j += U(P1[j],v,S1[j],S1[i]);
                }
            }
            U_t += U_j;
    }
    return U_t/2;
}

int main()
{
    /// Create Layer
    /// Position vectors
    ifstream layer;
    layer.open("layer1.txt");
    vector< vector<double> > P;
    vector<double> r;
    for (int j = 0; j <3; j++){r.push_back(0);}
    for (int i=0;i<2*Na;i++){
            double x, y ,z;
            layer >> x >> y >> z;
                r[0] = x;
                r[1] = y;
                r[2] = z;
                P.push_back(r);
    }
    /// Spin Vectors
    vector<vector<double> > S;

    vector <double> S_u;
    for (int i = 0; i <3; i++){S_u.push_back(0);}
    S_u[2]=1;

    vector <double> S_d;
    for (int i = 0; i <3; i++){S_d.push_back(0);}
    S_d[2]=-1;

    for (int i = 0; i <Na; i++){S.push_back(S_u);}
    for (int i = 0; i <Na; i++){S.push_back(S_d);}

    for (int i = 0; i <2*Na; i++){
            cout << i << " = " << "(" << P[i][0] << "," << P[i][1] << "," << P[i][2] << ") (" << S[i][0] << "," << S[i][1] << "," << S[i][2] << ")" << endl;
    }

    /// Calculate energy
    double E_old = U_tot(P,S);
    cout << "E_0 = " << E_old << endl;

    return 0;
}
