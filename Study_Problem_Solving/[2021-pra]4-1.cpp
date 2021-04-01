#include <stdio.h>
#include <deque>
#include <vector>
using namespace std;

int main()
{

    int n;
    scanf("%d", &n);

    int top[500001];
    int answer[500001];
    deque<vector<int>> stack;

    for (int i = 0; i < n; i++)
    {
        int temp;
        scanf("%d", &temp);
        top[i] = temp;
    }

    for (int i = 0; i <n; i++){
        while (!stack.empty()){
            if (stack.back()[0] >= top[i]){
                answer[i] = stack.back()[1] + 1;
                vector<int> temp = {top[i], i};
                stack.push_back(temp);
                break;
            }
            else{
                stack.pop_back();
            }
        }

        if (stack.empty()){
            answer[i] = 0;
            vector<int> temp = {top[i], i};
            stack.push_back(temp);
        }
    }


    for (int i = 0; i < n; i++)
    {
        printf("%d ", answer[i]);
    }
    return 0;
}