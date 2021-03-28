#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>

#define INF 987654321
using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int test_case = 0; test_case < T; test_case++)
    {
        int N;
        cin >> N;

        vector<vector<int>> arr;
        int x = 0;
        int y = 0;

        for (int i = 0; i < N + 2; i++)
        {
            cin >> x >> y;
            vector<int> temp;
            temp.push_back(x);
            temp.push_back(y);
            arr.push_back(temp);
        }

        int possible[103][103];

        for (int i = 0; i < N + 2; i++)
        {
            for (int j = 0; j < N + 2; j++)
            {
                possible[i][j] = INF;
            }
        }

        for (int i = 0; i < N + 2; i++)
        {
            for (int j = 0; j < N + 2; j++)
            {
                if (i != j)
                {
                    int diff;
                    diff = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]);
                    if (diff <= 1000)
                    {
                        possible[i][j] = 1;
                    }
                }
            }
        }

        for (int k = 0; k < N + 2; k++)
        {
            for (int a = 0; a < N + 2; a++)
            {
                for (int b = 0; b < N + 2; b++)
                {
                    possible[a][b] = min(possible[a][b], possible[a][k] + possible[k][b]);
                }
            }
        }

        if (possible[0][N + 1] == INF)
        {
            cout << "sad" << endl;
        }
        else
        {
            cout << "happy" << endl;
        }
    }
    return 0;
}
