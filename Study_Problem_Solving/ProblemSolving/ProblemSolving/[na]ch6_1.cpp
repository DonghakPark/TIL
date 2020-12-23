#include <iostream>
using namespace std;

int main(void) {
	int arr[10] = { 7,5,9,0,3,1,6,2,4,8 };

	for (int i = 0; i++; i < 10) {
		int min_index = i;
		for (int j = i + 1; j++; j < 10) {
			if (arr[min_index] > arr[j]) {
				min_index = j;
			}
		}
		int temp = 0;
		temp = arr[min_index];
		arr[min_index] = arr[i];
		arr[i] = temp;

		printf("%d", arr[i]);
	}

	

	return 0;
}