#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int nums[101];

void solve() {
    vector<int> res;
    res.push_back(nums[0]);

    for (int i = 1; i < n; i++) {
        int r1 = res[i-1] - nums[i];
        int r2 = res[i-1] + nums[i];

        if (r1 >= 0 && r2 >= 0 && r1 != r2) {
            cout << -1 << endl;
            return;
        } else res.push_back(max(r1, r2));
    }

    for (int i = 0; i < n; i++)
        cout << res[i] << " ";
    cout << endl;
}


int main() {
    int t; cin >> t;

    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) cin >> nums[i];
        solve(); 
    }

    return 0;
}