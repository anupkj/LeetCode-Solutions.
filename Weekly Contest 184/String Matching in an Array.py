class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = [];
        n = len(words);
        for i in range(n):
            cnt = 0;
            for j in range(n):
                if(words[i] in words[j]):
                    cnt+=1;
            if(cnt>1):
                ans.append(words[i]);
        return ans;
        
