#include <iostream>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n; cin >> n;
        int nums[1000];

        for (int i = 0; i < 1000; i++)
            nums[i] = -1;

        for (int i = 0; i < n; i++) {
            int num; cin >> num;
            nums[num - 1] = i + 1;
        }

        int currMax = -1;

        for (int i = 1; i <= 1000; i++) {
            for (int j = 1; j <= 1000; j++) {
                if (nums[i-1] != -1 && nums[j-1] != -1 && gcd(i, j) == 1)
                    currMax = max(currMax, nums[i-1] + nums[j-1]);
            }
        }

        cout << currMax << endl;
    }

    return 0;
}