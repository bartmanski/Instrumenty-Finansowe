import numpy as np

def policz_p(Pi, c, I, t0, T, td):
    r_nom = (1 + c) * (1 + Pi) - 1
    g_nom = (1 + I) * (1 + Pi) - 1
    pi_m = (1 + Pi)**(1/12) - 1
    r_m = (1 + r_nom)**(1/12) - 1
    g_m = (1 + g_nom)**(1/12) - 1
    
    N_w = (T - t0) * 12
    N_e = (td - T) * 12
    
    k = np.arange(1, N_w + 1)
    fv_skladowe = (1 + g_m)**(k - 1) * (1 + r_m)**(N_w - k)
    fv_mnoznik = np.sum(fv_skladowe) 
    
    E1 = (1 + g_m)**(N_w - 1)
    
    j = np.arange(1, N_e + 1)
    pv_skladowe = (1 + pi_m)**(j - 1) / (1 + r_m)**j
    pv_total = E1 * np.sum(pv_skladowe)
    
    return pv_total / fv_mnoznik

print(f"p = {policz_p(0.02, 0.03, 0.05, 0, 40, 60):.4f}")
