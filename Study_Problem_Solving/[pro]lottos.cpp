#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int hit_num = 0;
    int zero_num = 0;
    
    for (int i =0; i < lottos.size(); i ++){
        if (lottos[i] == 0){
            zero_num += 1;
            continue;
        }
        for (int j =0; j < win_nums.size(); j++){
            if (lottos[i] == win_nums[j])
            {
                hit_num += 1;
                break;
            }    
        }
    }

    
    int min_prize = 0;
    int max_prize = 0;
    min_prize = 7 - hit_num;
    max_prize = 7 - (hit_num + zero_num);
    
    if (min_prize > 5){
        min_prize = 6;
    }
    if (max_prize > 5){
        max_prize = 6;
    } 
    
    answer.push_back(max_prize);
    answer.push_back(min_prize);    
    return answer;
}