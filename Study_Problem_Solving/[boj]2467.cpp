#include <iostream>
using namespace std;

int main()
{
	int N;
	cin >> N;

	long long int K[100001];

	for (int i = 0; i < N; i++)
	{
		cin >> K[i];
	}

	int minus = 0;
	int plus = N-1;

	int answer = abs(K[minus] + K[plus]);
	
	long long int first = K[minus];
	long long int second = K[plus];

	while (minus < plus)
	{
		int now_answer = (K[minus] + K[plus]);
		if (abs(now_answer) < answer)
		{
			answer = abs(now_answer);
			first = K[minus];
			second = K[plus];
		}
		
		if (now_answer < 0)
			minus++;
		else
			plus--;
			
	}

	cout << first << " " << second << "\n";

	return 0;
}