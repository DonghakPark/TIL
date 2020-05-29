#include <iostream>
using namespace std;

void rev_str(char *s_1);
void rev_str(char *s_1, char *s_2); //동일한 이름의 함수를 중복

int main(void)
{
	char s1[80] = "Dankook University";
	char s2[80];

	cout << "원본 문자열1 :" << s1 << "\n\n";
		
	cout << "rev_str(s1,s2)의 사용 " << endl;
	rev_str(s1,s2);
	cout << "처리된 문자역1 :" << s1 << endl<< "처리된 문자역2 :" << s2 << "\n\n";

	cout << "rev_str(s1)의 사용 " << endl;
	rev_str(s1);
	cout << "처리된 문자역1 :" << s1 << endl;

	return 0;
}

void rev_str(char *s_1)
{
	int temp;
	int L1 = strlen(s_1);

	for (int i = 0; i < (L1/2); i++) // swap을 통한 문자열의 역전
	{
		temp = s_1[i];
		s_1[i] = s_1[L1 - (i+1)];
		s_1[L1 - (i + 1)] = temp;
	}

}

void rev_str(char *s_1, char *s_2)
{
	
	int temp;
	char new_str[80]; //두번째 인수에 저장하기 위한 새로운 배열 선언
	strcpy(new_str, s_1);

	int L1 = strlen(new_str);
	int L2 = strlen(s_2);

	for (int i = 0; i < (L1 / 2); i++)
	{
		temp = new_str[i];
		new_str[i] = new_str[L1 - (i + 1)];
		new_str[L1 - (i + 1)] = temp;
	}
	strcpy(s_2, new_str);

	//// swap을 통한 문자열 역전
	
}