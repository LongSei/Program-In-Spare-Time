#include <bits/stdc++.h>
using namespace std;
int n, m;
int main()
{
    cout << "COMPILING..." << endl;
    srand(time(NULL));
    system("g++ SINH_TEST.cpp -o SINH_TEST");
    system("g++ REAL_CODE.cpp -o REAL_CODE");
    system("g++ TRAU_CODE.cpp -o TRAU_CODE");
    cout << "NUMBER_TEST_WANT_TO_CHECK: ";
    int number_test;
    cin >> number_test;
    cout << "CHECKING_STATUS: " << endl; 
    for(int iTest = 1; iTest <= number_test; iTest++)
    {
        system("SINH_TEST.exe");
        system("REAL_CODE.exe");
        system("TRAU_CODE.exe");
        if(system("fc test.out test.ans") != 0)
        {
            cout << "Test " << iTest << ": WRONG!\n";
            return 0;
        }
        cout << "Test " << iTest << ": CORRECT!\n";
    }
    return 0;
}
