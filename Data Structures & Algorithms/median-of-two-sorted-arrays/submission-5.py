class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums2:
            if len(nums1)%2 ==0:
                return ((nums1[len(nums1)//2-1] + nums1[(len(nums1)//2)])/2)
            else:
                return nums1[len(nums1)//2]
        elif not nums1:
            if len(nums2)%2 ==0:
                return ((nums2[len(nums2)//2-1] + nums2[(len(nums2)//2)])/2)
            else:
                return nums2[len(nums2)//2]
        i = (len(nums1))//2
        left = 0
        right = len(nums1)
        while right >= left:
            i = (right + left)//2
            j = (len(nums1)+len(nums2)+1)//2 - i
            l1 = nums1[i-1] if i>0 else -float('inf')
            r1 = nums1[i] if i<len(nums1) else float('inf')
            print(j)
            l2 = nums2[j-1] if j>0 else -float('inf')
            r2 = nums2[j] if j<len(nums2) else float('inf')
            if l1<=r2 and l2<=r1:
                if (len(nums1)+len(nums2))%2!=0:
                    return(max(l1,l2))
                return((max(l1,l2)+min(r1,r2))/2)
            elif l1>r2:
                right = i-1
            else:
                left = i+1
