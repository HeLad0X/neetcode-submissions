class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += f'{len(s)}#{s}'

        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1

            num = int(num)

            decoded_str.append(s[i+1 : num + i + 1])
            i+=num+1

        return decoded_str
