// https://programmers.co.kr/learn/courses/30/lessons/12969?language=cpp
// 별찍기 문제

#include <iostream>

using namespace std;

int main(void) {
    int a, b;
    cin >> a >> b;
    
    int i, j;
    
    for(i=0; i<b; i++) {
        for(j=0; j<a; j++) {
            cout << "*";
        }
        cout << endl;
    }
        return 0;
}