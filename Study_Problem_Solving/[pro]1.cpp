#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands)
{
    vector<int> answer;

    for (int i = 0; i < commands.size(); i++)
    {
        vector<int> new_array;

        for (int j = commands[i][0] - 1; j <= commands[i][1] - 1; j++)
        {
            new_array.push_back(array[j]);
        }
        sort(new_array.begin(), new_array.end());

        int k_th = new_array[commands[i][2] - 1];

        answer.push_back(k_th);
    }

    return answer;
}

int main()
{
    vector<int> array = {1, 5, 2, 6, 3, 5, 4};
    vector<vector<int>> commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
    vector<int> answer;

    answer = solution(array, commands);

    for (int i = 0; i < answer.size(); i++)
    {
        printf("%d|", answer[i]);
    }
    return 0;
}