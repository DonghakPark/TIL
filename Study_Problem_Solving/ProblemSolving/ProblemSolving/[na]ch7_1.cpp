#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int sequantialSearch(int n, string target, vector<string> arr) {

	for (int i = 0; i < n; i++) {
		if (arr[i] == target)
		{
			return i + 1;
		}
	}
	return -1;
}

int n;
string target;
vector<string> arr;

int main(void) {
	cout << "������ ���� ������ �Է��� ���� �� ĭ ��� ã�� ���ڿ��� �Է��ϼ���." << "\n";
	cin >> n >> target;
	
	cout << "�ռ� ���� ���� ������ŭ ���ڿ��� �Է��ϼ���. ������ ���� �� ĭ���� �մϴ�." << "\n";
	for (int i = 0; i < n; i++) {
		string x;
		cin >> x;
		arr.push_back(x);
	}

	cout << sequantialSearch(n, target, arr) << '\n';
}