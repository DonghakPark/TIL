//����1. �� ������ �Էµ� ������ ������� �Է¹޾� ���ڿ��� �ִ� ����, �޸�, ��ħǥ�� ���� ���� ���α׷��� �ۼ��Ͽ��� 
//����, �޸�, ��ħǥ�� �����ϱ� ���� swich���� ����Ͽ���
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

	for (j = 0; j < i; j++) // 100�� ���� ���� ���� ���� �ִ°��� �����ϴ� 
	{
		for (k = 0; k < 80; k++)
		{
			/*if (text[j][k] == ' ' || text[j][k] == ',' || text[j][k] == '.')
			{
				count++;
			} */
			//������ if�� �̿� �ؿ��� switch�� �̿�
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




