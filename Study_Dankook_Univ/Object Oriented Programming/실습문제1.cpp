//문제1. 빈 라인이 입력될 때까지 문장들을 입력받아 문자열에 있는 공백, 콤마, 마침표의 수를 세는 프로그램을 작성하여라 
//공백, 콤마, 마침표를 구분하기 위해 swich문을 사용하여라
/*this is a text.
  Hello!
  A,B,C are alphabet. */

#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
	int j, i, k;
	char text[100][80];
	int count = 0;

	for (i = 0; i < 100; i++)
	{
		gets(text[i]);
		
		if (!text[i][0]) 
			break;
	}

	for (j = 0; j < i; j++) // 100번 돌지 말고 받은 값을 넣는것이 현명하다 
	{
		for (k = 0; k < 80; k++)
		{
			/*if (text[j][k] == ' ' || text[j][k] == ',' || text[j][k] == '.')
			{
				count++;
			} */
			//위에는 if문 이용 밑에는 switch문 이용
			switch (true)
			{
			case 1: 
				if (text[j][k] == ' ')
				{
						count++;
						continue;
										}
			case 2: 
				if (text[j][k] == ',')
				{
						count++;
						continue;
				}
			case 3: 
				if (text[j][k] == '.')
				{
						count++;
						continue;
				}
			default:
				continue;
			}
		}
	}

	cout << count << endl;

	return 0;
}




