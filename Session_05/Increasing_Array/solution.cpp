#include <bits/stdc++.h>

using namespace std;
int main() {
    int n, curr;
    long long ans = 0;
    priority_queue<int> q;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> curr;
        q.push(curr);
        ans += q.top() - curr;
        q.pop();
        q.push(curr);
    }
    cout << ans << endl;
}
