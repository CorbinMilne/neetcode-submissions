#include <map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int,int> num_count;

        for(int num:nums)
        {
            if (num_count.contains(num))
            {
                return true;
            }
            else
            {
                num_count[num]=1;
            }
        }

        return false;

    }
};