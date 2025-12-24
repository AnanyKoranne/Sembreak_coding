#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void getAllSubsets(vector<int> &arr, vector<int> &ans, int i, vector<vector<int>> &allSubsets) {
        if (i == arr.size()) {
            allSubsets.push_back(ans);
            return;
        }
        //include
        ans.push_back(arr[i]);
        getAllSubsets(arr, ans, i+1, allSubsets);
        ans.pop_back();

        //exclude
        getAllSubsets(arr, ans, i+1, allSubsets);

    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> allSubsets;
        vector<int> ans;
        getAllSubsets(nums, ans, 0, allSubsets);
        return allSubsets;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = sol.subsets(nums);
    
    cout << "All subsets are:\n";
    for (const auto &subset : result) {
        cout << "[ ";
        for (int num : subset) {
            cout << num << " ";
        }
        cout << "]\n";
    }
    
    return 0;
}