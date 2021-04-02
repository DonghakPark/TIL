#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string S;
    cin >> S;

    int index = 0;
    int answer = 0;
    int still = 0;

    while (index < S.length())
    {
        if (S[index] == '(' and S[index + 1] == ')')
        {
            answer += still;
            index += 2;
        }
        else if (S[index] == '(')
        {
            still += 1;
            index += 1;
        }
        else if (S[index] == ')')
        {
            still -= 1;
            answer += 1;
            index += 1;
        }
    }
    cout << answer;
}