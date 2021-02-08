#include <iostream>

using namespace std;

int arr[7] = { 1,2,3,4 };


void swap(int index1, int index2) {
	int temp = arr[index1];
	arr[index1] = arr[index2];
	arr[index2] = temp;
}
void permutation(int arrSize) {
	if (arrSize == 1) {
		for (int i = 0; i < 4; i++) {
			printf("%d", arr[i]);
		}
		printf("\n");
		return;
	}
	for (int i = 0; i < arrSize; i++) {
		swap(i, arrSize - 1);
		permutation(arrSize - 1);
		swap(i, arrSize - 1);
	}
}

int main() {

	permutation(4);
	
	return 0;
}