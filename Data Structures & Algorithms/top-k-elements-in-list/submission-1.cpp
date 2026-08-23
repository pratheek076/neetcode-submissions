class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        priority_queue<pair<int,int>, vector<pair<int,int>>,
        greater<pair<int,int>>> minheap;
        vector<int> result;

        for(int x:nums)
        {
            freq[x]++;
        }
        for(auto &x: freq)
        {
            minheap.push({x.second, x.first});
            if(minheap.size()>k)
            {
                minheap.pop();
            }
        }
        while(!minheap.empty())
        {
            result.push_back(minheap.top().second);
            minheap.pop();

        }





       return result; 
    }
};
