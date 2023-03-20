#include <iostream>

using namespace std;

int main() {
    int t; cin >> t;

    while (t--) {
        int n, m; cin >> n >> m;

        if (n > m) cout << "No\n";
        else if (n % 2 == 0 && m % 2 == 1) cout << "No\n";
        else if (n % 2 == 0) {
            cout << "Yes\n";
            for (int i = 0; i < n - 2; i++) cout << 1 << " ";
            int remainder = (m - n + 2) / 2;
            cout << remainder << " " << remainder << endl;
        } else if (n % 2 == 1) {
            cout << "Yes\n";
            for (int i = 0; i < n - 1; i++) cout << 1 << " ";
            cout << m - n + 1 << endl;
        }
    }
    return 0;
}