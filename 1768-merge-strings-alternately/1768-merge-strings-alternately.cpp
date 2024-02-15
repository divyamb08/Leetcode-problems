#include<string>
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        
        int a = word1.size();
        int b = word2.size();
        if(a==0){
            return word2;
        }
        if(b==0){
            return word1;
        }
        int c = min(a,b);
        string res = "";
        for(int i=0; i<c;i++){
            res+=word1[i];
            res+=word2[i];
        }
        res+=word1.substr(c,a);
        res+=word2.substr(c,b);
        return res;
    }
};