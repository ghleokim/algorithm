#include <iostream>
#include <vector>
#include <typeinfo>

using namespace std;

struct person {
    char nose = 'A';
};

class animal {
    public: char nose = 'a';
};

int main() {
    
    person* p = new person();
    cout << p->nose << endl;

    p->nose='B';

    cout << p->nose << endl;

    animal* a = new animal();
    cout << a->nose << endl;

    return 0;
}