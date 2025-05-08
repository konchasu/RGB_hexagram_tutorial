# generate_rgb_hex.py
import numpy as np
import csv

def generate_rgb_hex(k: float, r_file="rw_hex_test_d.csv", g_file="gw_hex_test_d.csv", b_file="bw_hex_test_d.csv", n_file="nw_hex_test_d.csv"):
    m = k * 2 + 1
    Q = m * 2 + 1
    N = 4 * m + 4  # Q + 2*(m+1)

    # grid initialization
    rgb_grid = np.full((N, N), -999, dtype=int)
    r_hex = np.full((N, N), -300.0 / 256.0, dtype=np.float32)
    g_hex = np.full((N, N), -300.0 / 256.0, dtype=np.float32)
    b_hex = np.full((N, N), -999.0 / 256.0, dtype=np.float32)
    num_hex = np.full((N, N), -999.0 / 256.0, dtype=np.float32)
    
    p = 1
    c = (N - 1) // 2  # Python index adjustment
    rgb_grid[c, c] = 0
    r_hex[c, c] = 1.0
    g_hex[c, c] = 1.0
    b_hex[c, c] = 1.0
    num_hex[c, c] = 0.0

    # File output (stub - replace with actual saving as needed)
    print(f"grid size : {N}")
    print(f"center pos: {m + 1}")
    print("RGB pos for Green:")
    print(f"R: {m + 1}, {N - k}")
    print(f"G: {k + 1}, {m + 1}")
    print(f"B: {N - k}, {k + 1}")
    print("CYM pos:")
    print(f"C: {m + 1}, {k + 1}")
    print(f"Y: {k + 1}, {N - k}")
    print(f"M: {N - k}, {m + 1}")
    print("----")
    print(f"basic RGB-W grid num: {k}")
    print(f"one-cycle grid num  : {(k + 1) * 6}")
    print(f"max-cycle grid num  : {(2 * k + 1) * 6}")
    print(f"changing ratio      : {255.0 / (k + 1)}")
    print(f"min changing ratio  : {255.0 / (2 * k + 1)}")
    print("----")
    print("sample grid cycle")
    print("R->Y->G->C->B->M->...")

    
    # main loop of r_hex
    for t in range(1, 2 * m + 2):
        for i in range(1, 7):
            for j in range(1, t + 1):
                def set_cell(y, x, value):
                    nonlocal p
                    rgb_grid[y, x] = p
                    p += 1
                    r_hex[y, x] = value

                if i == 1:
                    y = c - (j - 1)
                    x = c + t
                    if t <= k + 1:
                        value = 1.0
                    elif t <= m:
                        value = float(m - (t - 1)) / (m - k)
                    elif t == m + 1:
                        value = 0.0
                    elif j == 1:
                        if t <= m + k + 1:
                            value = float(t - (m + 1)) / ((k + 1) * (Q - t + 1))
                        else:
                            value = float(t - (m + k + 1)) / (k + 1)
                    elif 1 < j <= 2 * m + 3 - t - 1:
                        tt = float(t - (m + 1)) / (k + 1)
                        value = tt if tt <= 1.0 else 1.0
                    else:
                        value = -999.0 / 256.0
                    set_cell(y, x, value)

                elif i == 2:
                    y = c - t
                    x = c + t - (j - 1)
                    if t <= k + 1:
                        value = float(k + 1 - (j - 1)) / (k + 1)
                    elif t < m + 1:
                        value = (float(m - (t - 1)) / (m - k)) * float(t - (j - 1)) / t
                    elif t == m + 1:
                        value = 0.0
                    else:
                        if j >= 2 * (t - m):
                            if j == 2 * (t - m) - 1:
                                tt = float(t - (m + 1)) / (k + 1)
                                value = tt if tt <= 1.0 else 1.0
                            else:
                                if Q - t > k:
                                    value = float(t - (j - 1)) * float(k + 1 - (m + 2 + k - t)) / ((k + 1) * (2 * m + 2 - t))
                                else:
                                    value = float(k + 1 - (j - 2 * (t - m) + 1)) / (k + 1)
                        else:
                            value = -999.0 / 256.0
                    set_cell(y, x, value)

                elif i == 3:
                    y = c - t + (j - 1)
                    x = c - (j - 1)
                    if t < k + 1:
                        value = float(k + 1 - t) / (m - k)
                    elif t < m + 1:
                        value = float(k + 2 - (t - k)) / ((k + 1) * (t + 1))
                    elif t == m + 1 or j == 1:
                        value = 0.0
                    elif t - m + 1 <= j <= m + 1:
                        value = 0.0
                    else:
                        value = -999.0 / 256.0
                    set_cell(y, x, value)

                elif i == 4:
                    y = c + (j - 1)
                    x = c - t
                    if t < k + 1:
                        value = float(k + 1 - t) / (m - k)
                    elif t < m + 1:
                        value = float(k + 2 - (t - k)) / ((k + 1) * (t + 1))
                    elif t == m + 1:
                        value = 0.0
                    elif 1 < j <= 2 * (m + 1) - t:
                        value = 0.0
                    else:
                        value = -999.0 / 256.0
                    set_cell(y, x, value)

                elif i == 5:
                    y = c + t
                    x = c - t + (j - 1)
                    if t <= k:
                        value = float(k + 1 - t + (j - 1)) / (k + 1)
                    elif t < m + 1:
                        if j == 1:
                            value = float(j) * float(k + 1 - (t - k)) / ((k + 1) * (t + 1))
                        else:
                            value = float(2 * k + 2 - t) * float(j - 1) / ((k + 1) * t)
                    elif t == m + 1 or j == 1:
                        value = 0.0
                    elif j >= 2 * (t - m):
                        if j == 2 * (t - m) - 1:
                            if Q - t >= k:
                                value = float(t - (m + 2)) / ((k + 1) * (m - (t - (m + 3))))
                            else:
                                value = float(t - (m + 2) - k) / (k + 1)
                        else:
                            jt = j - 2 * (t - m) - 1
                            if Q - t >= k:
                                value = float(jt + 2) * float(t - (m + 1)) / ((k + 1) * (m - (t - (m + 2))))
                            else:
                                value = float(jt + k - (Q - t) + 2) / (k + 1)
                    else:
                        value = -999.0 / 256.0
                    set_cell(y, x, value)

                elif i == 6:
                    y = c + t - (j - 1)
                    x = c + (j - 1)
                    if t <= k + 1:
                        value = 1.0
                    elif t <= m + 1:
                        value = float(m - (t - 1)) / (m - k)
                    elif t - m + 1 <= j <= m + 1:
                        tt = -1.0 * float(m - (t - 1)) / (m - k)
                        value = tt if tt <= 1.0 else 1.0
                    else:
                        value = -999.0 / 256.0
                    set_cell(y, x, value)

    # Save to CSV
    with open(r_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(N):
            writer.writerow(r_hex[:, i].T)
    r_hex = r_hex.T

    
    # main loop of g_hex
    for t in range(1, 2 * m + 2):
        for i in range(1, 7):
            for j in range(1, t + 1):
                #if j == 1:
                #    print("R-Y-G-C-B-M")
                #    print("RGB loop:", t)
                
                # 座標変換（Fortran → Python）
                def set_val(ix, iy, val):
                    rgb_grid[iy, ix] = p
                    g_hex[iy, ix] = val

                if i == 1:  # R->Y
                    ix, iy = c - (j - 1), c + t
                    if t <= k:
                        val = (k + 1 - t + (j - 1)) / (k + 1)
                    elif t <= m:
                        if j == 1:
                            val = (k + 2 - (t - k)) / ((k + 1) * (t + 1))
                        else:
                            val = ((m - (t - 1)) / (m - k)) * ((j - 1) / t)
                    elif t == m + 1 or j == 1:
                        val = 0.0
                    elif j <= 2 * m + 3 - t - 1:
                        if Q - t > k:
                            val = (j - 1) * (k + 1 - (m + 2 + k - t)) / ((k + 1) * (2 * m + 2 - t))
                        else:
                            val = (k - (Q - t) + j - 1) / (k + 1)
                    else:
                        val = -999.0 / 256.0
                    set_val(ix, iy, val)

                elif i == 2:  # Y->G
                    ix, iy = c - t, c + t - (j - 1)
                    if t <= k + 1:
                        val = 1.0
                    elif t < m + 1:
                        val = (m - (t - 1)) / (m - k)
                    elif t == m + 1:
                        val = 0.0
                    elif j >= 2 * (t - m):
                        tt = (t - (m + 1)) / (k + 1)
                        val = min(tt, 1.0)
                    else:
                        val = -999.0 / 256.0
                    set_val(ix, iy, val)

                elif i == 3:  # G->C
                    ix, iy = c - t + (j - 1), c - (j - 1)
                    if t <= k + 1:
                        val = 1.0
                    elif t < m + 1:
                        val = (m - (t - 1)) / (m - k)
                    elif t == m + 1:
                        val = 0.0
                    elif j == 1:
                        if t <= m + k + 1:
                            val = (t - (m + 1)) / ((k + 1) * (Q - t + 1))
                        else:
                            val = (t - (m + k + 1)) / (k + 1)
                    elif (t - m + 1) <= j <= m + 1:
                        tt = -1.0 * (m - (t - 1)) / (m - k)
                        val = min(tt, 1.0)
                    else:
                        val = -999.0 / 256.0
                    set_val(ix, iy, val)

                elif i == 4:  # C->B
                    ix, iy = c + (j - 1), c - t
                    if t <= k + 1:
                        val = (k + 1 - (j - 1)) / (k + 1)
                    elif t < m + 1:
                        val = ((m - (t - 1)) / (m - k)) * ((t - (j - 1)) / t)
                    elif t == m + 1:
                        val = 0.0
                    elif 1 < j <= 2 * (m + 1) - t:
                        if Q - t >= k:
                            jt = 2 * (m + 1) + 1 - t - j
                            val = (jt * (t - (m + 1))) / ((k + 1) * (m - (t - (m + 2)))) if jt > 0 else \
                                  ((t - 1 - (m + 1)) / ((k + 1) * (m - (t - 1 - (m + 2)))))
                        else:
                            val = (k + 1 - (j - 1)) / (k + 1)
                    else:
                        val = -999.0 / 256.0
                    set_val(ix, iy, val)

                elif i == 5:  # B->M
                    ix, iy = c + t, c - t + (j - 1)
                    if t < k + 1:
                        val = (k + 1 - t) / (m - k)
                    elif t < m + 1:
                        if j == 1:
                            val = (k + 1 - (t - k)) / ((k + 1) * (t + 1))
                        else:
                            val = (k + 2 - (t - k)) / ((k + 1) * (t + 1)) #5.0 #(k + 1 - (t - k)) / ((k + 1) * (t + 1))
                    elif t == m + 1:
                        val = 0.0
                    elif j == 1:
                        val = 0.0
                    else:
                        if j >= 2 * (t - m):
                            if j == 2 * (t - m) - 1:
                                if Q - t >= k:
                                    val = 0.0  # (t-(m+2)) / ((k+1)*(m-(t-(m+3))))
                                else:
                                    val = 0.0  # (t-(m+2)-k)/(k+1)
                            else:
                                jt = j - 2 * (t - m) - 1
                                if Q - t >= k:
                                    val = 0.0  # (jt+2)*(t-(m+1)) / ((k+1)*(m-(t-(m+2))))
                                else:
                                    val = 0.0  # (jt+k-(Q-t)+2)/(k+1)
                        else:
                            val = -999.0 / 256.0
                    set_val(ix, iy, val)

                elif i == 6:  # M->R
                    ix, iy = c + t - (j - 1), c + (j - 1)
                    if t < k + 1:
                        val = (k + 1 - t) / (m - k)
                    elif t < m + 1:
                        val = (k + 2 - (t - k)) / ((k + 1) * (t + 1))
                    elif t == m + 1:
                        val = 0.0
                    elif t > m + 1:
                        if t - m + 1 <= j <= m + 1:
                            tt = -1.0 * (m - (t - 1)) / (m - k)
                            if tt <= 1.0:
                                val = 0.0  # tt
                            else:
                                val = 0.0  # 1.0
                        else:
                            val = -999.0 / 256.0
                    set_val(ix, iy, val)
                p += 1
    
    ##########
    #for t in range(1, 2 * m + 2):
    #    for i in range(1, 7):
    #        for j in range(1, t + 1):
    #            # index in each step
    #            if i == 1:  # R->Y
    #                y, x = c - (j - 1), c + t
    #                rgb_grid[y, x] = p
    #                p += 1
    #                if t <= k:
    #                    g_hex[y, x] = (k + 1 - t + (j - 1)) / (k + 1)
    #                elif t <= m:
    #                    if j == 1:
    #                        g_hex[y, x] = (k + 2 - (t - k)) / ((k + 1) * (t + 1))
    #                    else:
    #                        g_hex[y, x] = ((m - (t - 1)) / (m - k)) * (j - 1) / t
    #                elif t == m + 1 or j == 1:
    #                    g_hex[y, x] = 0.0
    #                elif 1 < j <= 2 * m + 3 - t - 1:
    #                    if Q - t > k:
    #                        g_hex[y, x] = (j - 1) * (k + 1 - (m + 2 + k - t)) / ((k + 1) * (2 * m + 2 - t))
    #                    else:
    #                        g_hex[y, x] = (k - (Q - t) + j - 1) / (k + 1)
    #
    #            elif i == 2:  # Y->G
    #                y, x = c - t, c + t - (j - 1)
    #                rgb_grid[y, x] = p
    #                p += 1
    #                if t <= k + 1:
    #                    g_hex[y, x] = 1.0
    #                elif t < m + 1:
    #                    g_hex[y, x] = (m - (t - 1)) / (m - k)
    #                elif t == m + 1:
    #                    g_hex[y, x] = 0.0
    #                elif j >= 2 * (t - m):
    #                    tt = (t - (m + 1)) / (k + 1)
    #                    g_hex[y, x] = min(tt, 1.0)
    #
    #            elif i == 3:  # G->C
    #                y, x = c - t + (j - 1), c - (j - 1)
    #                rgb_grid[y, x] = p
    #                p += 1
    #                if t <= k + 1:
    #                    g_hex[y, x] = 1.0
    #                elif t < m + 1:
    #                    g_hex[y, x] = (m - (t - 1)) / (m - k)
    #                elif t == m + 1:
    #                    g_hex[y, x] = 0.0
    #                elif j == 1:
    #                    if t <= m + k + 1:
    #                        g_hex[y, x] = (t - (m + 1)) / ((k + 1) * (Q - t + 1))
    #                    else:
    #                        g_hex[y, x] = (t - (m + k + 1)) / (k + 1)
    #                elif t - m + 1 <= j <= m + 1:
    #                    tt = -1.0 * (m - (t - 1)) / (m - k)
    #                    g_hex[y, x] = min(tt, 1.0)
    #
    #            elif i == 4:  # C->B
    #                y, x = c + (j - 1), c - t
    #                rgb_grid[y, x] = p
    #                p += 1
    #                if t <= k + 1:
    #                    g_hex[y, x] = (k + 1 - (j - 1)) / (k + 1)
    #                elif t < m + 1:
    #                    g_hex[y, x] = ((m - (t - 1)) / (m - k)) * (t - (j - 1)) / t
    #                elif t == m + 1:
    #                    g_hex[y, x] = 0.0
    #                elif 1 < j <= 2 * (m + 1) - t:
    #                    if Q - t >= k:
    #                        jt = 2 * (m + 1) + 1 - t - j
    #                        if jt > 0:
    #                            g_hex[y, x] = jt * (t - (m + 1)) / ((k + 1) * (m - (t - (m + 2))))
    #                        else:
    #                            g_hex[y, x] = (t - 1 - (m + 1)) / ((k + 1) * (m - (t - 1 - (m + 2))))
    #                    else:
    #                        jt = 2 * (m + 1) + 1 - t - j
    #                        g_hex[y, x] = (k + 1 - (j - 1)) / (k + 1)
    #
    #            elif i == 5:  # B->M
#   #                 y, x = c + t, c - t + (j - 1)
#   #                 rgb_grid[y, x] = p
#   #                 p += 1
#   #                 if t < k + 1:
#   #                     g_hex[y, x] = (k + 1 - t) / (m - k)
#   #                 elif t < m + 1:
#   #                     g_hex[y, x] = (k + 1 - (t - k)) / ((k + 1) * (t + 1))
#   #                 elif t == m + 1 or j == 1:
#   #                     g_hex[y, x] = 0.0
#   #                 elif j >= 2 * (t - m):
#   #                     g_hex[y, x] = 0.0
#   #             elif i == 5:
    #                if t <= k + 1:
    #                    g_hex[y, x] = 2.0 #1.0
    #                elif t < m + 1:
    #                    g_hex[y, x] = 3.0 #float(m - (t - 1)) / (m - k)
    #                elif t == m + 1:
    #                    g_hex[y, x] = 0.0 #0.0
    #                elif j == 1:
    #                    if t <= m + k + 1:
    #                        g_hex[y, x] = 5.0 #float(t - (m + 1)) / ((k + 1) * (Q - t + 1))
    #                    else:
    #                        g_hex[y, x] = 6.0 #float(t - (m + k + 1)) / (k + 1)
    #                elif j >= 2 * (t - m):
    #                    print("test:",i,j)
    #                    tt = float(t - (m + 1)) / (k + 1)
    #                    g_hex[y, x] = tt if tt <= 1.0 else 1.0
    #
    #            elif i == 6:  # M->R
    #                y, x = c + t - (j - 1), c + (j - 1)
    #                rgb_grid[y, x] = p
    #                p += 1
    #                if t < k + 1:
    #                    g_hex[y, x] = (k + 1 - t) / (m - k)
    #                elif t < m + 1:
    #                    g_hex[y, x] = (k + 2 - (t - k)) / ((k + 1) * (t + 1))
    #                elif t == m + 1:
    #                    g_hex[y, x] = 0.0
    
    # Save to CSV
    g_hex = g_hex.T
    with open(g_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(N):
            writer.writerow(g_hex[:, i])
    g_hex = g_hex.T                 
    
    # main loop of b_hex
    for t in range(1, 2 * m + 2):
        for i in range(1, 7):
            for j in range(1, t + 1):
                x, y = None, None
                if i == 1:
                    x, y = c - (j - 1), c + t
                elif i == 2:
                    x, y = c - t, c + t - (j - 1)
                elif i == 3:
                    x, y = c - t + (j - 1), c - (j - 1)
                elif i == 4:
                    x, y = c + (j - 1), c - t
                elif i == 5:
                    x, y = c + t, c - t + (j - 1)
                elif i == 6:
                    x, y = c + t - (j - 1), c + (j - 1)
                else:
                    continue
    
                if 0 <= x < N and 0 <= y < N:
                    rgb_grid[x, y] = p
                    p += 1
                    val = -999.0 / 256.0
    
                    if i == 1:
                        if t < k + 1:
                            val = float(k + 1 - t) / (m - k)
                        elif t <= m:
                            val = float(k + 2 - (t - k)) / ((k + 1) * (t + 1))
                        elif t == m + 1 or j == 1:
                            val = 0.0
                        elif 1 < j <= 2 * m + 3 - t - 1:
                            tt = float(t - (m + 1)) / (k + 1)
                            val = 0.0 if tt <= 1.0 else 0.0
                    elif i == 2:
                        if t < k + 1:
                            val = float(k + 1 - t) / (m - k)
                        elif t < m + 1:
                            val = float(k + 2 - (t - k)) / ((k + 1) * (t + 1))
                        elif t == m + 1:
                            val = 0.0
                        elif j >= 2 * (t - m):
                            if j == 2 * (t - m) - 1:
                                tt = float(t - (m + 1)) / (k + 1)
                                val = 0.0 if tt <= 1.0 else 0.0
                            else:
                                val = 0.0
                    elif i == 3:
                        if t <= k:
                            val = float(k + 1 - t + (j - 1)) / (k + 1)
                        elif t < m + 1:
                            if j == 1:
                                val = float(m - t) / (m - k) / (t + 1)
                            else:
                                val = (float(m - (t - 1)) / (m - k)) * float(j - 1) / t
                        elif t == m + 1 or j == 1:
                            val = 0.0
                        elif t - m + 1 <= j <= m + 1:
                            jt = j - (t - m + 1) + 2
                            if Q - t >= k:
                                val = (float(m - (2 * m - t + 1)) / (m - k)) * float(jt - 1) / (2 * m + 2 - t)
                            else:
                                val = float(k - (Q - t) + jt - 1) / (k + 1)
                    elif i == 4:
                        if t <= k + 1:
                            val = 1.0
                        elif t < m + 1:
                            val = float(m - (t - 1)) / (m - k)
                        elif t == m + 1:
                            val = 0.0
                        elif 1 < j <= 2 * (m + 1) - t:
                            tt = float(t - (m + 1)) / (k + 1)
                            val = tt if tt <= 1.0 else 1.0
                    elif i == 5:
                        if t <= k + 1:
                            val = 1.0
                        elif t < m + 1:
                            val = float(m - (t - 1)) / (m - k)
                        elif t == m + 1:
                            val = 0.0
                        elif j == 1:
                            if t <= m + k + 1:
                                val = float(t - (m + 1)) / ((k + 1) * (Q - t + 1))
                            else:
                                val = float(t - (m + k + 1)) / (k + 1)
                        elif j >= 2 * (t - m):
                            tt = float(t - (m + 1)) / (k + 1)
                            val = tt if tt <= 1.0 else 1.0
                    elif i == 6:
                        if t <= k + 1:
                            val = float(k + 1 - (j - 1)) / (k + 1)
                        elif t <= m + 1:
                            val = (float(m - (t - 1)) / (m - k)) * float(t - (j - 1)) / t
                        elif t - m + 1 <= j <= m + 1:
                            if Q - t >= k:
                                tj = 2 * m + 2 - t
                                val = float(t - (m + 1)) * float(t - j - (t - (m + 2))) / ((k + 1) * tj)
                            else:
                                val = float(t + k - m - (j - 1)) / (k + 1)
    
                    b_hex[x, y] = val
    
    # Save to CSV
    with open(b_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(N):
            writer.writerow(b_hex[:, i])
    b_hex = b_hex.T
            
    # main loop of num
    for t in range(1, 2 * m + 2):
        for i in range(1, 7):
            for j in range(1, t + 1):
                if i == 1:  # R->Y
                    y, x = c - (j - 1), c + t
                    rgb_grid[y, x] = p
                    p += 1
                    if t <= k:
                        num_hex[y, x] = 1.0/256.0
                    elif t <= m:
                        if j == 1:
                            num_hex[y, x] = 1.0/256.0
                        else:
                            num_hex[y, x] = 1.0/256.0
                    elif t == m + 1:
                        num_hex[y, x] = 0.0/256.0
                    elif j == 1:
                        num_hex[y, x] = 13.0/256.0
                    elif 1 < j <= 2 * m + 3 - t - 1:
                        num_hex[y, x] = 7.0/256.0
    
                elif i == 2:  # Y->G
                    y, x = c - t, c + t - (j - 1)
                    rgb_grid[y, x] = p
                    p += 1
                    if t <= k + 1:
                        num_hex[y, x] = 2.0/256.0
                    elif t < m + 1:
                        num_hex[y, x] = 2.0/256.0
                    elif t == m + 1:
                        num_hex[y, x] = 0.0/256.0
                    elif j >= 2 * (t - m):
                        tt = (t - (m + 1)) / (k + 1)
                        num_hex[y, x] = 8.0/256.0
    
                elif i == 3:  # G->C
                    y, x = c - t + (j - 1), c - (j - 1)
                    rgb_grid[y, x] = p
                    p += 1
                    if t <= k + 1:
                        num_hex[y, x] = 3.0/256.0
                    elif t < m + 1:
                        num_hex[y, x] = 3.0/256.0
                    elif t == m + 1:
                        num_hex[y, x] = 0.0
                    elif j == 1:
                        if t <= m + k + 1:
                            num_hex[y, x] = 14.0/256.0
                        else:
                            num_hex[y, x] = 14.0/256.0
                    elif t - m + 1 <= j <= m + 1:
                        tt = -1.0 * (m - (t - 1)) / (m - k)
                        num_hex[y, x] = 9.0/256.0
    
                elif i == 4:  # C->B
                    y, x = c + (j - 1), c - t
                    rgb_grid[y, x] = p
                    p += 1
                    if t <= k + 1:
                        num_hex[y, x] = 4.0/256.0
                    elif t < m + 1:
                        num_hex[y, x] = 4.0/256.0
                    elif t == m + 1:
                        num_hex[y, x] = 0.0
                    elif 1 < j <= 2 * (m + 1) - t:
                        if Q - t >= k:
                            jt = 2 * (m + 1) + 1 - t - j
                            if jt > 0:
                                num_hex[y, x] = 10.0/256.0
                            else:
                                num_hex[y, x] = 10.0/256.0
                        else:
                            jt = 2 * (m + 1) + 1 - t - j
                            num_hex[y, x] = 10.0/256.0
    
                elif i == 5:  # B->M
                    y, x = c + t, c - t + (j - 1)
                    rgb_grid[y, x] = p
                    p += 1
                    if t < k + 1:
                        num_hex[y, x] = 5.0/256.0
                    elif t < m + 1:
                        num_hex[y, x] = 5.0/256.0
                    elif t == m + 1 or j == 1:
                        num_hex[y, x] = 0.0
                    elif j >= 2 * (t - m):
                        num_hex[y, x] = 11.0/256.0
                    
                    if j == 1:
                        if t > m + 1:
                            num_hex[y, x] = 15.0/256.0
    
    
                elif i == 6:  # M->R
                    y, x = c + t - (j - 1), c + (j - 1)
                    rgb_grid[y, x] = p
                    p += 1
                    if t < k + 1:
                        num_hex[y, x] = 6.0/256.0
                    elif t < m + 1:
                        num_hex[y, x] = 6.0/256.0
                    elif t == m + 1:
                        num_hex[y, x] = 0.0
                        
                    elif t - m + 1 <= j <= m + 1:
                        if Q - t >= k:
                            tj = 2 * m + 2 - t
                            num_hex[y, x] = 12.0/256.0
                        else:
                            num_hex[y, x] = 12.0/256.0
                        
                   
                    
    # Save to CSV
    with open(n_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(N):
            writer.writerow(num_hex[:, i])
    num_hex = num_hex.T

    print("rgb_hex shape:",g_hex.shape)
    print("----")
    print("output_filename-> r_file:",r_file,", g_file:",g_file,", b_file:",b_file,"n_file",n_file)
    
    return r_hex, g_hex, b_hex, num_hex
