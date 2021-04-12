#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
int digit[10];

int main(void){
    string N;
    cin >> N;

    int len = N.length();
    for (int i = 0; i < len;  i++){
        digit[N[i] - '0']++;
    }
    int six_nine = (digit[6] + digit[9] + 1) / 2;
    digit[6] = six_nine;
    digit[9] = six_nine;

    int m =0;
    for (int i =0; i <10; i++){
        if (digit[m] < digit[i]) m =i;
    }
    cout << digit[m] << endl;
    return 0;
}