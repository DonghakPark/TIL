#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(int a, int b)
{
    string answer = "";
    vector<int> month_per_day = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int days = 0;
    for (int i = 0; i < (a - 1); i++)
    {
        days += month_per_day[i];
    }

    days = (days + b) % 7;

    vector<string> day = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};

    answer = day[days];
    return answer;
}

int main()
{

    string answer;
    int a = 5;
    int b = 24;
    answer = solution(a, b);
    cout << answer << endl;
    return 0;
}