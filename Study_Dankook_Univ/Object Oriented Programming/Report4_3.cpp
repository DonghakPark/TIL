#include "stdafx.h"
#include <iostream>
using namespace std;

template <class X> int find(X object, X *list, int size)
{

	X T = NULL;
	for (int i = 0; i < size; i++)
	{
		if (list[i] == object)
		{
			T = i;
		}
	}
	if (T != NULL)
	{
		return T;
	}
	else return -1;
}

int main(void)
{
	int size, *p, int_object;
	float *q, float_object;
	char *r, char_object;

	//int형
	cout << "size : ";
	cin >> size;

	p = new int;
	*p = size;
	for (int i = 0; i < size; i++)
	{
		cin >> p[i];
	}
	cout << "검색할 값 : ";
	cin >> int_object;
	cout << find(int_object, p, size)+1 << "번째" << endl;
	
	//float
	cout << "size : ";
	cin >> size;

	q= new float;
	*q = size;
	for (int i = 0; i < size; i++)
	{
		cin >> q[i];
	}
	cout << "검색할 값 : ";
	cin >> float_object;
	cout << find(float_object, q, size)+1 << "번째" << endl;

	// char
	cout << "size : ";
	cin >> size;

	r = new char;
	*r = size;
	for (int i = 0; i < size; i++)
	{
		cin >> r[i];
	}
	cout << "검색할 값 : ";
	cin >> char_object;
	cout << find(char_object, r, size)+1 << "번째" << endl;
	return 0;
}