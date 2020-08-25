// https://programmers.co.kr/learn/courses/30/lessons/12950
// 행렬의 덧셈 문제 : vector 사용

#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer = arr1;
    
    int i, j;
    
    for(i=0;i<arr1.size();i++){
        for(j=0;j<arr1[0].size();j++){
            answer[i][j] += arr2[i][j];
        }
    }
    
    return answer;
}
