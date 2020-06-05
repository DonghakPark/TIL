#include "stdafx.h"
#include <iostream>
using namespace std;

template <class X> void min(X a, X b)
{
	if (a > b)
	{
		cout << a <<endl;
	}
	else if (a<b)
	{
		cout << b <<endl;
	}
}
int main(void)
{
	int x = 5;
	int y = 6;
	char c1 = 'a';
	char c2 = 'z';

	min(x, y);
	min(c1,c2);

	return 0;
}