#include <iostream>

using namespace std;

int recursiveSum(int n) {
	if (n == 1) return 1;

	return n + recursiveSum(n - 1);
}

int main() {
	int answer = 0;

	answer = recursiveSum(10);

	printf("%d", answer);
	return 0;
}