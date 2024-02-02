class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        start = [ 0, 0, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
        increment = [0, 0, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111]
        for i in range(len(str(low)), min(len(str(high)), 9)+1):
            crt = start[i]
            print(crt)
            while crt<=high:
                print("Hi", crt)
                if crt<low:
                    crt += increment[i]
                    if crt%10==0:
                        break
                    continue
                res.append(crt)
                crt += increment[i]
                if crt%10==0:
                    break
        
        return res            