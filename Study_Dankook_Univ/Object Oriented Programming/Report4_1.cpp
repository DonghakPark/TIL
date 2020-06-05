#include "stdafx.h"
#include <iostream>
using namespace std;

class Distance{
protected:
	double x, y;
public:
	Distance() { x = 0; y = 0; }
	Distance(double a, double b) { x = a; y = b; }
	virtual double trav_time()
	{
		double T=0;
		T = ((x - y) / 60);
		return T;
	}

};

class metric : public Distance {
public:
	metric(double a, double b) { x = a; y = b; }
	double trav_time()
	{
		double T;
		T = ((x - y)/100); // 킬로미터로 변환 후 속도로 나눔
		return T;
	}
};

int main()
{
	Distance mile(120,45);
	metric km(140, 40);

	cout << mile.trav_time() << "H" << endl;
	cout << km.trav_time() << "H" << endl;

    return 0;
}