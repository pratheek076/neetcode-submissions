class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> res;
  
        for(int i =0; i<operations.size(); i++)
        {
            if(operations[i] == "D")
            {
                res.push_back(2*res.back());
            }
            else if(operations[i]=="+")
            {
                int result = res[res.size()-1] + res[res.size()-2];
                res.push_back(result);
            }

            else if(operations[i]=="C")
            {
                res.pop_back();


            }
            else
            {
                res.push_back(stoi(operations[i]));
            }
           


        }
         int sum = 0;
            for(int x: res)
            {
                sum+=x;
            }
            return sum;
        
    }
};