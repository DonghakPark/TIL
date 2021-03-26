#include <iostream>
#include <algorithm>

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
    return 0;
}