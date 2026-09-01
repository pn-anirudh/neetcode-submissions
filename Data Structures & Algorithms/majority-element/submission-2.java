class Solution {
    public int majorityElement(int[] nums) {
        
        int assumedElement = nums[0];
        int assumedCount = 0;

        for(int i:nums){
            if(assumedElement==i){
                assumedCount++;
            }
            else{
                assumedCount--;
                if(assumedCount==0){
                    assumedElement = i;
                    assumedCount = 1;
                }
            }
        }

        return assumedElement;
    }
}