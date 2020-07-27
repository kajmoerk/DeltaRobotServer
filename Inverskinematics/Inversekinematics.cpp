#include <pybind11/pybind11.h>
#include <Windows.h>
#define _USE_MATH_DEFINES
#include <math.h>

double Wp = 11.671, Sp = 40.431, Ub = 90.505, Wb = 44.904, Up = 23.343, LL = 59.21, ll = 141.427;
double a = Wb - Up;
double b = (Sp / 2) - (sqrt(3) / 2) * Wb;
double c = Wp - 0.5 * Wb;
double theta1 = 0, theta2 = 0, theta3 = 0;

double getTheta(int thetaNr, double x, double y, double z)
{
    switch (thetaNr)
    {
    case 1:
    {
        double E_1 = 2 * LL * (y + a);
        double F_1 = 2 * z * LL;
        double G_1 = pow(x, 2) + pow(y, 2) + pow(z, 2) + pow(a, 2) + pow(LL, 2) + 2 * y * a - pow(ll, 2);
        double t_1M = (-F_1 + sqrt(pow(E_1, 2) + pow(F_1, 2) - pow(G_1, 2))) / (G_1 - E_1);
        //double t_1P=(-F_1+sqrt(pow(E_1,2)+(F_1,2)-(G_1,2)))/(G_1-E_1);
        //double theta1_1=2*atan(t_1P)*180/PI;
        theta1 = -(2 * atan(t_1M)) * 180 / M_PI + 90;
        return theta1;
        break;
    }
    case 2:
    {
        double E_2 = -LL * (sqrt(3) * (x + b) + y + c);
        double F_2 = 2 * z * LL;
        double G_2 = pow(x, 2) + pow(y, 2) + pow(z, 2) + pow(b, 2) + pow(c, 2) + pow(LL, 2) + 2 * (x * b + y * c) - pow(ll, 2);
        double t_2M = (-F_2 + sqrt(pow(E_2, 2) + pow(F_2, 2) - pow(G_2, 2))) / (G_2 - E_2);
        //double t_2P=(-F_2+sqrt(pow(E_2,2)+(F_2,2)-(G_2,2)))/(G_2-E_2);
        theta2 = -(2 * atan(t_2M)) * 180 / M_PI + 90;
        return theta2;
        break;
    }
    case 3:
    {
        double E_3 = LL * (sqrt(3) * (x - b) - y - c);
        double F_3 = 2 * z * LL;
        double G_3 = pow(x, 2) + pow(y, 2) + pow(z, 2) + pow(b, 2) + pow(c, 2) + pow(LL, 2) + 2 * (-x * b + y * c) - pow(ll, 2);
        double t_3M = (-F_3 + sqrt(pow(E_3, 2) + pow(F_3, 2) - pow(G_3, 2))) / (G_3 - E_3);
        //double t_3P=(-F_3+sqrt(pow(E_3,2)+pow(F_3,2)-pow(G_3,2)))/(G_3-E_3);
        theta3 = -(2 * atan(t_3M)) * 180 / M_PI + 90;
        return theta3;
        break;
    }
    default:
        return 1;
        break;
    }
}

double angleToPulse(int servoNr, double angle)
{
    switch (servoNr)
    {
        double angleToPulse;
    case 0:
        angleToPulse = 2.02 * angle + 292.5;
        return angleToPulse;
        break;
    case 1:
        angleToPulse = 1.94 * angle + 285;
        return angleToPulse;
        break;
    case 2:
        angleToPulse = 1.94 * angle + 285;
        return angleToPulse;
        break;

    default:
        return 1;
        break;
    }
}

namespace py = pybind11;
PYBIND11_MODULE(Inversekinematics, m) {
    m.def("getTheta", &getTheta, R"pbdoc(
        Comppute joint value for a delta robot.
    )pbdoc");

    m.def("angleToPulse", &angleToPulse, R"pbdoc(
        Comppute joint value to pulse for stepper motor.
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}
