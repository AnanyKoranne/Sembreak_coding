#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> digitToChar = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    void helper(vector<string> &res, string current, string digits, int idx) {
        if (current.size() == digits.size()) {
            res.push_back(current);
            return;
        }
        string chars = digitToChar[digits[idx] - '0'];

        for (char c : chars) {
            helper(res, current + c, digits, idx+1);
        }
    }
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits.empty()) return res;
        helper(res, "", digits, 0);
        return res;
        
    }
};

int main() {
    Solution sol;
    string digits = "24";
    vector<string> combinations = sol.letterCombinations(digits);
    
    cout << "Letter combinations for digits " << digits << " are:\n";
    for (const string &combination : combinations) {
        cout << combination << " ";
    }
    cout << endl;
    
    return 0;
}