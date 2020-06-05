#include <iostream>
using namespace std;

class coord {
private:
	int x, y;
public:
	coord() { x = 0; y = 0; }
	coord(int i, int j) { x = i; y = j; }
	void get_xy(int &i, int &j) { i = x; j = y; }
	void show();
	coord operator*(coord op2); // 좌표값 곱하기 
	coord operator/(coord op2); // 좌표값 나누기
	bool operator==(coord op2); // 좌표가 동일한지 비교
	bool operator&&(coord op2); // 길이가 같은지 비교
	coord operator--();
	coord operator--(int notused);
	friend coord operator-(coord op1, coord op2);
	// friend coord operator/(coord op1, coord op2);
};
void coord::show()
{cout << "x = " << x << " y = " << y << endl;}
coord coord::operator*(coord op2)
{	coord temp;
	temp.x = x * op2.x;
	temp.y = y * op2.y;
	return temp;}
coord coord::operator/(coord op2)
{	coord temp;
	temp.x = x / op2.x;
	temp.y = y / op2.y;
	return temp;}
bool coord::operator==(coord op2)
{	return (x == op2.x && y == op2.y);}
bool coord::operator&&(coord op2)
{	double t1,t2;
	t1 = sqrt((x*x)+(y*y));
	t2 = sqrt((op2.x*op2.x) + (op2.y*op2.y));
	return (t1 == t2);}
coord coord::operator--()
{	x--;
	y--;
	return *this;}
coord coord::operator--(int notused)
{	coord temp = *this;
	x--;
	y--;
	return temp;}

coord operator-(coord op1, coord op2)
{	coord temp;
	temp.x = op1.x - op2.x;
	temp.y = op1.y - op2.y;
	return temp;}

/*coord operator/(coord op1, coord op2)
{	coord temp;
	temp.x = op1.x / op2.x;
	temp.y = op1.y / op2.y;
	return temp;}*/

int main()
{	coord a(15, 15), b(3,3), c;
	cout << "x와 y의 값" << endl;
	a.show();
	b.show();
	cout << "------------" << endl;
	cout << "*연산" << endl;
	c=a*b;
	c.show();
	cout << "------------" << endl;
	cout << "/연산" << endl;
	c = a / b;
	c.show();
	cout << "------------" << endl;
	cout << "==연산" << endl;
	cout << (a == b)<<endl;
	cout << "------------" << endl;
	cout << "&&연산" << endl;
	cout << (a&&b)<<endl;
	cout << "------------" << endl;
	cout << "--후행 연산" << endl;
	a--;
	a.show();
	cout << "------------" << endl;
	cout << "--선행 연산" << endl;
	--b;
	b.show();
	cout << "------------" << endl;
	cout << "-연산" << endl;
	c = a - b;
	c.show();
	cout << "------------" << endl;
    return 0;
}
