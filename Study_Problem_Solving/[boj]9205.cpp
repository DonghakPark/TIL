#include <vector>
#include <iostream>

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

        int possible[N + 2][N + 2] = {0,};
        for (int i = 0; i < N + 2; i++)
        {
            for (int j = 0; j < N + 2; j++)
            {
                cout << possible[i][j] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}
