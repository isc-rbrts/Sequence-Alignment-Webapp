def GlobalAlignment(match_reward, mismatch_penalty, indel_penalty, s, t):
    backtrack, score = GAbacktrack(match_reward, mismatch_penalty, indel_penalty, s, t)
    v = OutputGAv(backtrack, s, len(s), len(t))
    w = OutputGAw(backtrack, t, len(s), len(t))
    
    n = max(len(v), len(w))
    
    while len(v) < n:
        v = "-" + v
    while len(w) < n:
        w = "-" + w
        
    return score, v, w

def GAbacktrack(match_reward, mismatch_penalty, indel_penalty, v, w):
    n = len(v) + 1
    m = len(w) + 1
    Backtrack = [[" "]*m for i in range(n)]
    s = [[0]*(m) for i in range(n)]
    for i in range(1, n):
        s[i][0] = -indel_penalty * i
    for j in range(1, m):
        s[0][j] = -indel_penalty * j
            
    for i in range(1, n):
        for j in range(1, m):
            match = -(mismatch_penalty)
            if v[i - 1] == w[j - 1]:
                match = match_reward
            s[i][j] = max(s[i-1][j] - indel_penalty, s[i][j-1] - indel_penalty, s[i-1][j-1] + match)
            
            if s[i][j] == s[i-1][j] - indel_penalty:
                Backtrack[i][j] = "↓"
            elif s[i][j] == s[i][j-1] - indel_penalty:
                Backtrack[i][j] = "→"
            elif s[i][j] == s[i-1][j-1] + match:
                Backtrack[i][j] = "↘"
    
    for line in s:
        print(line)
    
    return Backtrack, s[n-1][m-1]

def OutputGAv(backtrack, v, i, j):
    if j == 0:
        return v[:i]
    if i == 0:
        return ""
    if backtrack[i][j] == "↓":
        return OutputGAv(backtrack, v, i - 1, j) + v[i - 1]
    elif backtrack[i][j] == "→":
        return OutputGAv(backtrack, v, i, j - 1) + "-"
    else:
        return OutputGAv(backtrack, v, i - 1, j - 1) + v[i - 1]
    
def OutputGAw(backtrack, w, i, j):
    if i == 0:
        return w[:j]
    if j == 0:
        return ""
    if backtrack[i][j] == "↓":
        return OutputGAw(backtrack, w, i - 1, j) + "-"
    elif backtrack[i][j] == "→":
        return OutputGAw(backtrack, w, i, j - 1) + w[j - 1]
    else:
        return OutputGAw(backtrack, w, i - 1, j - 1) + w[j - 1]