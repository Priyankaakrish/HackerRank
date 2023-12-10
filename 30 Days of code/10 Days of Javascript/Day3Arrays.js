function getSecondLargest(nums) {
    
    var max=0,secondmax=0;
    
    for(var i=0;i<nums.length;i++)
    {
        if(nums[i]>max)
        {
            secondmax=max;
            max=nums[i];
        }
        else if(nums[i]<max && nums[i]>secondmax)
        {
            secondmax=nums[i];
        }
    }
    return secondmax; 
}