#include <math.h>

#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
#define lli long long int
#define li long int
#define ld long double
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    lli sum = 0LL;
    vector<lli> ip;
    cin >> n;
    for (int i = 0; i < n; i++) {
        lli b;
        cin >> b;
        ip.push_back(b);
        sum += b;
    }
    lli mindiff = (1 << 30);
    lli tmp, cmp;
    for (int i = 0; i < (1 << n); i++) {
        tmp = 0;
        for (int j = 0; j < n; j++) {
            if ((i >> j) & 1) {
                tmp += ip[j];
            }
        }
        cmp = abs(tmp - (sum - tmp));
        if (cmp < mindiff) {
            mindiff = cmp;
        }
    }
    cout << mindiff << endl;
    return 0;
}
