#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    string s = "";
    cin >> s;

    stack<char> l;
    stack<char> r;
    for (int i = 0; i < s.size(); i++)
    {
        l.push(s[i]);
    }

    int num;
    cin >> num;
    while (num--)
    
    {
        char tmp;
        cin >> tmp;
        if (tmp == 'P')
        {
            char c;
            cin >> c;
            l.push(c);
        }
        else if (tmp == 'L')
        {
            if (l.empty())
                continue;
            else
            {
                r.push(l.top());
                l.pop();
            }
        }
        else if (tmp == 'B')
        {
            if (l.empty())
                continue;
            else
                l.pop();
        }
        else if (tmp == 'D')
        {
            if (r.empty())
                continue;
            else
            {
                l.push(r.top());
                r.pop();
            }
        }
    }
    while (!l.empty())
    {
        r.push(l.top());
        l.pop();
    }
    while (!r.empty())
    {
        cout << r.top();
        r.pop();
    }
    return 0;
}