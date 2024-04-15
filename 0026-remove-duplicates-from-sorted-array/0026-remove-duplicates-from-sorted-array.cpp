class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 2) {
            return nums.size(); 
        }

        int writeIndex = 1; // Pointer for placing the next unique element
        for (int readIndex = 1; readIndex < nums.size(); readIndex++) {
            if (nums[readIndex] != nums[writeIndex - 1]) {
                nums[writeIndex] = nums[readIndex];
                writeIndex++; // Only increment write index when a unique element is found
            }
        }
        return writeIndex;
    }
};