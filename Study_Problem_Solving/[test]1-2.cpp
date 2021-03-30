#include <iostream>
#include <deque>

using namespace std;

int main(int argc, char **argv)
{
    int n;
    int k;
    deque<char> arr;
    deque<int> visited;
    int answer = 0;

    cin >> n >> k;

    for (int i = 0; i < n; i++)
    {
        char temp;
        cin >> temp;
        arr.push_back(temp);
        visited.push_back(0);
    }

    for (int i = 0; i < n; i++)
    {
        if (arr[i] == 'H')
        {
            continue;
        }
        else
        {
            int start = 0;
            int end = i + k + 1;

            if ((i - k) >= 0)
            {
                start = (i - k);
            }

            if ((i + k) >= n)
            {
                end = n;
            }

            for (int j = start; j < end; j++)
            {
                if (arr[j] == 'H' and visited[j] == 0)
                {
                    visited[j] = 1;
                    answer += 1;
                    break;
                }
            }
        }
    }

    cout << answer;

    return 0;
}