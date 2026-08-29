class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        sort(nums.begin(), nums.end());

        vector<vector<int>> res;

        int first = 0, sum;
        int left, right;

        while (first < nums.size() - 2) {

            // Skip duplicate first values
            if (first > 0 && nums[first] == nums[first - 1]) {
                first++;
                continue;
            }

            sum = nums[first];

            left = first + 1;
            right = nums.size() - 1;

            while (left < right) {

                int total = sum + nums[left] + nums[right];

                if (total == 0) {

                    res.push_back({sum, nums[left], nums[right]});

                    // Skip duplicate left values
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }

                    // Skip duplicate right values
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                    left++;
                    right--;
                }
                else if (total > 0) {
                    right--;
                }
                else {
                    left++;
                }
            }

            first++;
        }

        return res;
    }
};