#include <iostream>
#include <deque>

using namespace std;

int main(int argc, char **argv)
{
    int p;
    int n;
    int total_virus = 0;
    deque<int> virus;

    cin >> p >> n;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;

        virus.push_back(temp);
    }

    while (!virus.empty())
    {
        int now_virus;
        now_virus = virus[0];
        virus.pop_front();

        total_virus *= p;
        total_virus %= 1000000007;
        total_virus += now_virus;
    }

    total_virus %= 1000000007;
    cout << total_virus;

    return 0;
}