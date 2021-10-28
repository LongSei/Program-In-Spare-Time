#include<bits/stdc++.h>
using namespace std;

long long random(long long l, long long h) {
    return rand() % (h - l + 1) + l;
}

signed main() {
    srand(time(NULL));
    ofstream file("test.inp");
    
    // HERE IS CODE TO CREATE TEST
    // EXAMPLE: 
    int n = random(1, 10);
    file << n;
    // EXAMPLE
    
    file.close();
}
