#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX_NUM 2001;
int n;
int nums[2001];
int currTotal = 0;

int canCreateSum(int leftPtr, int targetSum) {
    int currSum = 0;
    int maxSeg = 0;
    
    for (int i = leftPtr; i < n; i++) {
        currSum += nums[i];

        if (currSum == targetSum) {
            currSum = 0;
            maxSeg = max(maxSeg, i - leftPtr + 1);
            leftPtr = i+1;
        } else if (currSum > targetSum) return MAX_NUM;
    }

    if (currSum == 0) return maxSeg;
    else return MAX_NUM;
}

int solve() {
    int res = n;
    int total = 0;

    for (int i = 1; i < n; i++) {
        total += nums[i-1];
        int currSeg = max(i, canCreateSum(i, total));
        res = min(res, currSeg);
    }

    return res;
}

int main() {
    int t; cin >> t;

    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) cin >> nums[i];

        cout << solve() << endl;
    }
    return 0;
}