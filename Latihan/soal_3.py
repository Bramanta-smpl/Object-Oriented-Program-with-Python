class prime_num:
    def __init__(self, n : int):
        self.n = n
    
    def cekPrima(self) -> bool:
        habisDibagi = 0
        if self.n < 2:
            return False
        for i in range(1, self.n + 1):
            if self.n % i == 0:
                habisDibagi += 1
            if habisDibagi > 2:
                break
        if habisDibagi <= 2:
            return True
        else :
            return False


