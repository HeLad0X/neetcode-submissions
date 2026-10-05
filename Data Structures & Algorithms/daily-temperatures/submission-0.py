class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len (temperatures) == 1:
            return [0]
        elif len (temperatures) == 0:
            return temperatures

        temp_stack = None
        res_arr = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if temp_stack is None or len(temp_stack) == 0:
                temp_stack = [i]
                continue
            while len(temp_stack) > 0 and temperatures[i] > temperatures[temp_stack[-1]]:
                res_arr[temp_stack[-1]] = i - temp_stack[-1]
                temp_stack.pop()
                
            
            temp_stack.append(i)

        return res_arr