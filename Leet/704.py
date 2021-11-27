class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        centerIndex = 0
        centerValue = 0


        

        while True:

            N = len(nums)
            if(N == 1):
                if(nums[0] == target):
                    return 0
                else:
                    return -1
                

            ## 중앙 Index 구하기
            # N이 짝수이면
            elif (N / 2) == 0:
                centerIndex = N/2
                centerValue = nums[centerIndex]

                ## 중앙값과 비교
                # target이 중앙값일 때
                if target == centerValue:
                    result += centerIndex
                    return result

                # target이 중앙값이 아님
                else:
                    
                    # target이 중앙값보다 크다
                    # 
                    if target > centerValue:
                        result += centerIndex
                        nums = nums[centerIndex:]

                    # target이 중앙값보다 작다
                    elif target < centerValue:
                        nums = nums[:centerIndex - 1]

            # N이 홀수이면    
            elif (N / 2 != 0):
                centerIndex = (N - 1) /2
                centerValue = nums[centerIndex]

                ## 중앙값과 비교
                # target이 중앙값일 때
                if target == centerValue:
                    result += centerIndex
                    return result

                # target이 중앙값이 아님
                else:
                    
                    # target이 중앙값보다 크다
                    # 
                    if target > centerValue:
                        result += centerIndex
                        nums = nums[centerIndex:]

                    # target이 중앙값보다 작다
                    elif target < centerValue:
                        nums = nums[:centerIndex - 1]