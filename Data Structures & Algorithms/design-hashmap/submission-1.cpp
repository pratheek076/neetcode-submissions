class MyHashMap {
    private: 
            int myarr[1000001] = {};
            bool present[1000001] = {};
public:
    MyHashMap() {
        
    }
    
    void put(int key, int value) {

        if (present[key] == false)
        {
           myarr[key] = value;
           present[key] = true;
        }
        else
        {
            myarr[key] = value;
        }

    }
    
    int get(int key) {
        if (present[key] == false)
        {
            return -1;
        }
        return myarr[key];
        
    }
    
    void remove(int key) {
        if (present[key] != false)
        {
            myarr[key] = 0;
            present[key] = false;
        }

        
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */