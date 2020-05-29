#include <iostream>
using namespace std;

int main(void)
{
	int i,j;
	cout << "1000~2000 사이의 소수(Prime Number) 출력" <<endl;
	for ( i =1000; i <= 2000; i++)
	{
		for( j =2; j<= i-1; j++)
		{ if(i%j == 0) { break;} }
		if (i ==j ) cout << i <<" ";
	}
	cout<<endl;
	return 0;
}