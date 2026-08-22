class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        vector<pair<int,int>> freqlist;
        vector<int> result;

        for (int x: nums)
        {
            freq[x]++;
        }
        for(auto &p: freq)
        {
            freqlist.push_back({p.first, p.second});
        
        }
        sort(freqlist.begin(), freqlist.end(),[](auto &a, auto &b){
            return a.second> b.second;
        });

        for(int i=0;i<k;i++)
        {
            result.push_back(freqlist[i].first);
        }
       
    return result;
    }
    
};
