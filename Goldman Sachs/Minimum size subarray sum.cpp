class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int sum=0;
        int r=0,l=0;
        int maxi = INT_MAX;
        int n = nums.size();
        while(r<n)
        {
            sum=sum+nums[r];
            r++;
            while(sum>=target)
            {
                maxi = min(maxi, r-l);
                sum = sum - nums[l];
                l++;
            }
                
        }
        return maxi==INT_MAX?0:maxi;
    }
};
