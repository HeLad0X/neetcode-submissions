class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        strs = []
        i = 0
        while i < len(s):
            current_num_str = ''
            while i < len(s) and s[i] != '#':
                current_num_str += s[i]
                i += 1
            
            current_num = int(current_num_str)
            strs.append(s[i+1:i+current_num+1])

            i += current_num + 1

        return strs
