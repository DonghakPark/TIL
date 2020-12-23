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
	cout << "생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요." << "\n";
	cin >> n >> target;
	
	cout << "앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다." << "\n";
	for (int i = 0; i < n; i++) {
		string x;
		cin >> x;
		arr.push_back(x);
	}

	cout << sequantialSearch(n, target, arr) << '\n';
}