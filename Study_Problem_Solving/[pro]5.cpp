#include <vector>
#include <deque>
#include <algorithm>
#include <iostream>
using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture)
{
    int number_of_area = 0;
    int max_size_of_one_area = 0;

    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};

    int visited[101][101] = {0};
    deque<vector<int>> Q;

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (picture[i][j] != 0 and visited[i][j] == 0)
            {

                vector<int> temp;
                temp = {i, j, picture[i][j]};

                Q.push_front(temp);
                visited[i][j] = 1;
                number_of_area += 1;
                int count = 1;

                while (!Q.empty())
                {
                    int x = Q[0][0];
                    int y = Q[0][1];
                    int target = Q[0][2];
                    Q.pop_front();
                    for (int i = 0; i < 4; i++)
                    {
                        int nx = x + dx[i];
                        int ny = y + dy[i];

                        if (0 <= nx and nx < m and 0 <= ny and ny < n)
                        {
                            if (visited[nx][ny] == 0 and picture[nx][ny] == target)
                            {
                                temp = {nx, ny, target};
                                Q.push_back(temp);
                                visited[nx][ny] = 1;
                                count += 1;
                            }
                        }
                    }
                }
                max_size_of_one_area = max(max_size_of_one_area, count);
            }
        }
    }

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

int main()
{
    int m = 6;
    int n = 4;
    vector<vector<int>> picture = {
        {1, 1, 1, 0},
        {1, 2, 2, 0},
        {1, 0, 0, 1},
        {0, 0, 0, 1},
        {0, 0, 0, 3},
        {0, 0, 0, 3}};
    vector<int> answer = solution(m, n, picture);
    cout << answer[0] << " " << answer[1] << endl;
    return 0;
}