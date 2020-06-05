//문제2 : 빈 라인이 입력될 때까지 문장들을 입력받아 토큰의 수를 계산하는 프로그램을 작성하라.
//this is a test
//Hello
//I am hungry
#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
	int i;
	char *p, *q;
	char token[80];
	char text[100][80];
	int count = 0;

	for (i = 0; i < 100; i++)
	{
		gets(text[i]);

		if (!text[i][0])
			break;
	}

	for (int j = 0; j < i; j++)
	{
		p = text[j];
		while (*p)
		{
			q = token;

			while (*p != ' '&&*p)
			{
				*q = *p;
				q++; p++;
			}
			if (*p)p++;
			*q = '\0';
			count++;
		}
	}
	cout << count << endl;
	return 0;
}