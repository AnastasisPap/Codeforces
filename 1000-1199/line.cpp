#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;


int main()
{
    int t; cin >> t;

    while (t--) {
        int n; cin >> n;
        ll total = 0;
        int k = 1;
        char dir[n+1];

        for (int i = 1; i <= n; i++) {
            cin >> dir[i];
            if (dir[i] == 'R') total += n - i;
            else total += i - 1;
        }

        vector<ll> res;
        int j = n;
        int i = 1;
        while (i <= n/2) {
            if (dir[i] == 'L') {
                dir[i] = 'R';
                total += n + 1 - 2 * i;
                res.push_back(total);
                k++;
            } 
            if (dir[j] == 'R') {
                dir[j] = 'L';
                total += 2 * j - n - 1;
                res.push_back(total);
                k++;
            }
            i++;
            j--;
        }

        for (int i = k; i <= n; i++) res.push_back(total);
        for (int i = 0; i < n; i++) cout << res[i] << " ";
        cout << endl;
    }
    return 0;
}