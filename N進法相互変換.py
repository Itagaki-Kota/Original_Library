# A進法  → 10進法
# 10進法 → B進法
# A進法  → 10進法 → B進法






def Nsinn_to_decimal(num, N):
    """N進法のnumを10進法に変換する (num:文字列, N:int, 戻り値:int)"""

    decimal = 0
    digits = len(num)   #桁数
    for i in range(digits - 1, -1, -1):
        decimal += ( int(num[digits - 1 - i]) * (N ** i) )
    
    return decimal


# N進法→10進法を,標準関数を用いると (PAST本 p375)    int("N進法文字列", base = N) → 10進法(int型)で出力
int("1101", base = 2)    # 13
int("ffff", base = 16)   # 65535
int("1101", base = 6)    # 253











def decimal_to_Nsinn(num, N):
    """10進法のnumをN進法に変換する (num:int, N:int, 戻り値は文字列)""" 

    if num == 0:
        return "0"
    else:
        tmp = []
        while num > 0:
            tmp.append(str(num % N))
            num = num // N
    
        tmp.reverse()
        return "".join(tmp)



# 11進法以降はアルファベットでAとか出てくるので, (必要なら)また別途作る必要はある。
# 10進数numに対してbin(num), oct(num), hex(num)は組み込みで有る。
