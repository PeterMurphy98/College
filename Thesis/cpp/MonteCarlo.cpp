#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <sstream>
#include <ctime>
#include <cstdlib>

using namespace std;



int main()
{
    /// Create Layer
    ifstream layer;
    layer.open("movie.xyz");
    vector< vector<double> > P;
    vector<double> r;
    for (int j = 0; j <3; j++) {r.push_back(0);}
    for (int i=0;i<1200;i++){
            double x, y ,z;
            layer >> x >> y >> z;
                r[0] = x;
                r[1] = y;
                r[2] = z;
                P.push_back(r);
  }

  for (int i=0; i<5; i++){
  cout << P[i][0] << ", " << P[i][1] << ", "<< P[i][2] << endl;
  }


    return 0;
}
