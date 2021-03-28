#include <bits/stdc++.h>

#define INF 987654321

using namespace std;

int main()
{
    long long min, max;
    cin >> min >> max;

    long long ans = max - min + 1;

    vector<bool> arr(max - min + 1, false);
    long long i = 2;

    while (i * i <= max)
    {

        long long N = min / (i * i); //처음으로 나누어 떨어지는 수

        if (min % (i * i) != 0)
        {
            N += 1;
        }

        while (N * (i * i) <= max)
        {
            if (arr[N * (i * i) - min] == false)
            {
                arr[N * (i * i) - min] = true;
                ans -= 1;
            }
            N += 1;
        }
        i += 1;
    }
    cout << ans;
    return 0;
}