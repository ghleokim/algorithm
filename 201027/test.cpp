#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int alpha_cnt[26];
string alpha_order;
string answer;
string solution(string s){
	int num = 0;
	int target = -1;
	
	// 끝처리
	s.push_back('a');
	for (int i = 0; i < s.size(); i++) {
		if (s[i] >= 'a' && s[i] <= 'z') {
			
			if (target != -1) {
				alpha_cnt[target] += num;
				num = 0;
			}

			int cur = s[i] -'a';
			// 이전에 안나왔음
			if (alpha_cnt[cur] == 0) {
				alpha_order.push_back(s[i]);
			} 
			target = cur; 
			
		}
		else {
			num = num * 10 + s[i] -'0';
        }
	}

	for (auto alpha : alpha_order) {
		answer.push_back(alpha);
		string tmp = to_string(alpha_cnt[alpha-'a']);
        cout << tmp << endl;
        answer += tmp;
    }
    return answer;
}

int main() {
    string s = "a1c10b2c3";

    // expectd output a1c13b2
    cout << solution(s) << endl;
    cout << "ASD" << endl;
    return 0;
}