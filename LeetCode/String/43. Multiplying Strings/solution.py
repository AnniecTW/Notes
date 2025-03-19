class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        ln = len(num1) + len(num2)
        rst = [0] * ln

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1

                total = rst[pos2] + mul

                rst[pos1] += total // 10
                rst[pos2] = total % 10
        

        rst = map(str, rst)
        rst = ''.join(rst).lstrip("0")
        return rst if rst else "0"
