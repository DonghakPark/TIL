#include <stdio.h>
using namespace std;

int price[4];
int dayOfMonth[13];

int minMonth[13];
int d[13];

int min(int a, int b) {
	return (a < b) ? a : b;
}

int main() {
	int tc;
	scanf_s("%d", &tc);

	for (int t = 1; t <= tc; t++) {

		for (int i = 0; i < 4; i++) {
			scanf_s("%d", &price[i]);
		}

		for (int i = 1; i <= 12; i++) {
			scanf_s("%d", &dayOfMonth[i]);
		}

		for (int i = 1; i <= 12; i++) {
			minMonth[i] = min(price[0] * dayOfMonth[i], price[1]);
		}

		for (int i = 1; i <= 12; i++) {
			d[i] = d[i - 1] + minMonth[i];
			if (i - 3 >= 0) {
				if (d[i] > d[i - 3] + price[2]) {
						d[i] = d[i - 3] + price[2];
				}
			}
		}

		if (d[12] > price[3]) {
			d[12] = price[3];
		}
		printf("#%d %d\n", t, d[12]);
	}
}