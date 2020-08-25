// https://programmers.co.kr/learn/courses/30/lessons/12954
// STL::vector를 사용하여 리스트 다루기

#include <string>
#include <vector>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    int num = x;
    
    for(int i=0; i < n; i++) {
        answer.push_back(num);
        num += x;
    }
    
    return answer;
}