# 自然数Nの約数列挙は, 約数の候補を√N くらいまで調べればよい


# 約数列挙
def div_enu(N):
    """自然数Nの約数を列挙した集合を返す"""

    div_set = set()
    for div in range(1, int(N ** (0.5) + 1)):
        if N % div == 0:
            div_set.add(div)
            div_set.add(N // div)

    return div_set



# 素数判定 (試し割り法で, √Nまでの数で割っていき, 1以外の約数が無ければ素数)
def is_prime(n):
    """自然数nが素数ならTrue"""

    if n == 1:
        return False
    
    for div in range(2, int(n ** (0.5)) + 1):
        if n % div == 0:
            return False
    else:
        return True




# 素因数分解
def  factorization(N):
    """ 自然数N(>=2)を素因数分解した結果の, 素因子が入ったリストを返す O(√N)"""
    
    factor = []
    for div in range(2, int(N ** (0.5)) + 1):
        while N % div == 0:
            N //= div
            factor.append(div)
            
    if N != 1:      
        factor.append(N)  
    
    return factor
 
 
#print(factorization(12))
# [2, 2, 3]

