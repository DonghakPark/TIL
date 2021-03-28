#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

bool desc(int a, int b){
    return a < b;
}

int main(void) {
    int arr[10] = {1,2,6,53,4,6,7,2,3,1};

    sort(arr, arr+10, desc);

    for (int i = 0; i <10; i ++){
        cout << arr[i] << endl;
    }
    int a = 10;
    int b = 15;
    cout << "smaller num is " << min(a,b) << endl;

    cout << abs(-123124231423423) << endl;

    return 0;
}