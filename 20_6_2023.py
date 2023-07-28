def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str = ''
        
        min_len = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) >= min_len:
                min_len = len(strs[i])
        
        for i in range(min_len):
             
            letter = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] == letter:
                    str += letter
        return str

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))