#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void getAllCombin(vector<vector<int>> &ans, vector<int> &combin, int idx, int target, vector<int> &arr) {
    if (target == 0) {
        ans.push_back(combin);
        return;
    }
    if (target < 0 || idx >= arr.size()) {
        return;
    }
    
    // Include the current number
    combin.push_back(arr[idx]);
    getAllCombin(ans, combin, idx, target - arr[idx], arr);
    combin.pop_back(); // backtrack
    
    // Exclude the current number and move to the next
    getAllCombin(ans, combin, idx + 1, target, arr);
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> ans;
    vector<int> combin;
    getAllCombin(ans, combin, 0, target, candidates);
    return ans;
}

int main() {
    vector<int> candidates = {2, 3, 6, 7};
    int target = 7;
    vector<vector<int>> result = combinationSum(candidates, target);
    
    for (const auto& comb : result) {
        for (int num : comb) {
            cout << num << " ";
        }
        cout << endl;
    }
    
    return 0;
}