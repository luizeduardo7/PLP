#include <iostream>
using namespace std;

int x = 0;
void foo(){
    x++;
}
void bar(){
    int x = 10;
    foo();
    cout << x << endl;
}

int main() {
    bar();
    short x = 5;
    cout << x << endl;
return 0;
}