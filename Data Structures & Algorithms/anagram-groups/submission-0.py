class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for string in strs:
            temp_arr = [0]*26

            for char in string:
                temp_arr[ord(char)-ord('a')]+=1
            
            if str(temp_arr) in hash_map:
                hash_map[str(temp_arr)].append(string)
            
            else:
                hash_map[str(temp_arr)] = []
                hash_map[str(temp_arr)].append(string)
        

        return list(hash_map.values())