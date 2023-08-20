def Turn_90(A, H, W):
    """二次元配列A(H行W列)を時計回りに90度回転させる"""
    
    after_H = W  # 回転後の配列の高さ
    after_W = H  # 回転後の配列の横幅

    A_after_turn = [["" for col in range(after_W)] for row in range(after_H)]
    
    for row in range(H):
        for col in range(W):
            A_after_turn[col][H - row - 1] = A[row][col]
 
    return A_after_turn



def Turn_180(A, H, W):
    """二次元配列A(H行W列)を180度回転させる(点対称移動)(上下反転(逆さま))"""
    
    A_after_turn = [["" for col in range(W)] for row in range(H)]
    
    for row in range(H):
        for col in range(W):
            A_after_turn[H - 1 - row][W - 1 - col] = A[row][col]
 
    return A_after_turn



def Turn_270(A, H, W):
    """二次元配列A(H行W列)を時計回りに270度(反時計回りに90度)回転させる"""
    
    after_H = W  #回転後の配列の高さ
    after_W = H  #回転後の配列の横幅
    
    A_after_turn = [["" for col in range(after_W)] for row in range(after_H)]
    
    for row in range(H):
        for col in range(W):
            A_after_turn[W - 1 - col][row] = A[row][col]
 
    return A_after_turn
    


A = [[0,0,0,1,1],
     [1,1,0,0,0],
     [3,5,1,1,0]]
    
B = Turn_270(A, 3, 5)  #二次元配列A(3行5列)を270度時計回りに回転
print(B)

print()

for row in B:
    print(row)