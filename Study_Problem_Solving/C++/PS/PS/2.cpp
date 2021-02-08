#include <stdio.h>

int T, N, M;
int input[501][501];
int visit[501][501] = { 0, };
int answer = 0;

typedef struct point {
	int x, y;
};

point STACK[5];
int top = -1;
point pop() {
	return STACK[top--];
}

void push(int x, int y) {
	STACK[++top].x = x;
	STACK[top].y = y;
}

int dArr[][4] = { {0,1}, {0,-1}, {1,0}, {-1,0} };

void dfs(int n, int m, int sum, int depth) {
	sum += input[n][m];

	if (depth == 1) {
		if (sum > answer)
			answer = sum;
		return;
	}

	push(n, m);
	visit[n][m] = 1;

	for (int k = 0; k <= top; k++) {
		for (int a = 0; a < 4; a++) {
			int newX = STACK[k].x + dArr[a][0];
			int newY = STACK[k].y + dArr[a][1];

			if (newX >= N || newY >= M || newX < 0 || newY < 0)
				continue;

			if (visit[newX][newY] == 0)
				dfs(newX, newY, sum, depth - 1);
		}
	}

	visit[n][m] = 0;
	pop();

	return;
}

int main() {
	int temp;
	scanf_s("%d %d", &N, &M);
	for (int i =0; i < N; i++)
		for (int j = 0; j < M; j++) {
			scanf_s("%d", &temp);
			input[i][j] = temp;

		}
	for (int i =0; i < N; i ++)
		for (int j = 0; j < M; j++) {
			dfs(i, j, 0, 4);
		}

	printf("%d", answer);

}