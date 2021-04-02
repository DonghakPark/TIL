#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
    string target;
    cin >> target;
    float need[10] = {0};

    for(int i =0; i <target.size(); i++){
        cout << target[i] << " ";
        if (target[i] == '6' or target[i] == '9'){
            need[6] += 0.5;
        }
        else{
            int index = (int)target[i];
            need[index] += 1;
        }
    }
    cout << endl;
    float temp = 0;

    for (int i =0; i < 10; i ++){
        cout << need[i] << " ";
        if (temp < ceil(need[i])){
            temp = ceil(need[i]);
        }
    }
    cout << endl;
    int answer = int(temp);

    cout << answer;

    return 0;
}