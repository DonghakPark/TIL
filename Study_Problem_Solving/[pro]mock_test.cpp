#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b){
    if (a.first == b.first){
        return a.second < b.second;
    }
    else{
        return a.first > b.first;
    }
}
vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> case1 = {1,2,3,4,5};
    vector<int> case2 = {2,1,2,3,2,4,2,5};
    vector<int> case3 = {3,3,1,1,2,2,4,4,5,5};
    
    vector<pair<int, int>> student;
    student.push_back(pair<int, int>(0,1));
    student.push_back(pair<int, int>(0,2));
    student.push_back(pair<int, int>(0,3));
    
    for( int i =0; i<answers.size(); i++){
        
        if (answers[i] == case1[i%case1.size()]){
            student[0].first += 1;
        }    
        if (answers[i] == case2[i%case2.size()]){
            student[1].first += 1;
        }    
        if (answers[i] == case3[i%case3.size()]){
            student[2].first += 1;
        }    
    }
    sort(student.begin(), student.end(), cmp);

    if (student[0].first != student[1].first){
        answer.push_back(student[0].second);
    }
    else{
        if(student[0].first == student[2].first){
            answer.push_back(student[0].second);
            answer.push_back(student[1].second);
            answer.push_back(student[2].second);
            
        }
        else{
            answer.push_back(student[0].second);
            answer.push_back(student[1].second);
        }
    }
    
    return answer;
}