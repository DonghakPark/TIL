#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string str;
	int eng = 0; //English char
	int num = 0; //number
	int special = 0; //Special char
	int other = 0; //others

	cout << "input str : ";
	cin >> str;

	for (int i = 0; i < str.length(); i++)
	{
		if (str[i] >= '0' && str[i] <= '9')
		{
			num++;
		}
		else if (str[i] >= 'a' && str[i] <= 'z' || str[i] >= 'A' && str[i] <= 'Z')
		{
			eng++;
		}
		else if (str[i] == ',' || str[i] == '.' || str[i] == '!')
		{
			special++;
		}
		else { other++; }
	}

	cout << "English : " << eng << endl;
	cout << "Number : " << eng << endl;
	cout << "Special : " << eng << endl;
	cout << "Others : " << eng << endl;

	return 0;
}