#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool search(vector<int> array, int number)
{
    for (int i = 0; i < array.size(); i++)
    {
        if (number == array[i])
        {
            return true;
        }
    }
    return false;
}

vector<int> solution(vector<int> numbers)
{
    vector<int> answer;

    for (int i = 0; i < numbers.size(); i++)
    {
        for (int j = 0; j < numbers.size(); j++)
        {
            if (i == j)
            {
                continue;
            }
            else
            {
                if (!search(answer, numbers[i] + numbers[j]))
                {
                    answer.push_back(numbers[i] + numbers[j]);
                }
            }
        }
    }
    sort(answer.begin(), answer.end());

    return answer;
}

int main()
{
    vector<int> numbers = {2, 1, 3, 4, 1};
    vector<int> ret;
    ret = solution(numbers);
    return 0;
}