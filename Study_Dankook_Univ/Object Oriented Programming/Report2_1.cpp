#include <iostream>
using namespace std;

double avg(float *arr, int size_arr); //함수의 프로토 타입 선언

int main(void)
{
	float num[50] = { 0 }; 
	int count=0;
	
	cout << "입력할 수의 갯수를 입력하시오 (최대 50개) : ";
	cin >> count;

	for (int i = 0; i <count; i++)
	{
		cout << i+1<<"번째 입력 :";
		cin >> num[i];		
	}

	cout << "평균 : " << avg(num, count) << endl; //함수 호출부분
	
	return 0;
}

double avg(float *arr, int num_2) // 평균을 구하는 함수
{
	float avg = 0;
	float sum = 0;
	
	for (int k = 0; k <num_2; k++)
	{
		sum = sum + arr[k];
	}

	avg = (sum / num_2);
	return avg;
}