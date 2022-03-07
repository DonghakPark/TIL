#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#pragma warning(disable : 4996)
using namespace std;

int main()
{
	int N, M;
	int degree[32001] = { 0, };
	vector<int> node_vec[32001];
	priority_queue<int, vector<int>, greater<int>> heapq;

	cin >> N >> M;
	for (int i = 0; i < M; i++)
	{
		int from, to;
		cin >> from >> to;
		node_vec[from].push_back(to);
		degree[to]++;

	}

	for (int i = 1; i <= N; i++)
	{
		if (degree[i] == 0)
			heapq.push(i);
	}

	while (!heapq.empty())
	{
		int now = heapq.top();
		heapq.pop();
		cout << now << " ";

		for (int i = 0; i < node_vec[now].size(); i++)
		{
			if (--degree[node_vec[now][i]] == 0)
				heapq.push(node_vec[now][i]);
		}
	}
	return 0;
}