import numpy as np

global_aminoacids_list = [
    'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'
    ]

global_dipeptide_list = [
    'AA', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AK', 'AL', 'AM', 'AN', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AV', 'AW', 'AY', 
    'CA', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CV', 'CW', 'CY', 
    'DA', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DK', 'DL', 'DM', 'DN', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DV', 'DW', 'DY', 
    'EA', 'EC', 'ED', 'EE', 'EF', 'EG', 'EH', 'EI', 'EK', 'EL', 'EM', 'EN', 'EP', 'EQ', 'ER', 'ES', 'ET', 'EV', 'EW', 'EY', 
    'FA', 'FC', 'FD', 'FE', 'FF', 'FG', 'FH', 'FI', 'FK', 'FL', 'FM', 'FN', 'FP', 'FQ', 'FR', 'FS', 'FT', 'FV', 'FW', 'FY', 
    'GA', 'GC', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GK', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GV', 'GW', 'GY', 
    'HA', 'HC', 'HD', 'HE', 'HF', 'HG', 'HH', 'HI', 'HK', 'HL', 'HM', 'HN', 'HP', 'HQ', 'HR', 'HS', 'HT', 'HV', 'HW', 'HY', 
    'IA', 'IC', 'ID', 'IE', 'IF', 'IG', 'IH', 'II', 'IK', 'IL', 'IM', 'IN', 'IP', 'IQ', 'IR', 'IS', 'IT', 'IV', 'IW', 'IY', 
    'KA', 'KC', 'KD', 'KE', 'KF', 'KG', 'KH', 'KI', 'KK', 'KL', 'KM', 'KN', 'KP', 'KQ', 'KR', 'KS', 'KT', 'KV', 'KW', 'KY', 
    'LA', 'LC', 'LD', 'LE', 'LF', 'LG', 'LH', 'LI', 'LK', 'LL', 'LM', 'LN', 'LP', 'LQ', 'LR', 'LS', 'LT', 'LV', 'LW', 'LY', 
    'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MI', 'MK', 'ML', 'MM', 'MN', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MV', 'MW', 'MY', 
    'NA', 'NC', 'ND', 'NE', 'NF', 'NG', 'NH', 'NI', 'NK', 'NL', 'NM', 'NN', 'NP', 'NQ', 'NR', 'NS', 'NT', 'NV', 'NW', 'NY', 
    'PA', 'PC', 'PD', 'PE', 'PF', 'PG', 'PH', 'PI', 'PK', 'PL', 'PM', 'PN', 'PP', 'PQ', 'PR', 'PS', 'PT', 'PV', 'PW', 'PY', 
    'QA', 'QC', 'QD', 'QE', 'QF', 'QG', 'QH', 'QI', 'QK', 'QL', 'QM', 'QN', 'QP', 'QQ', 'QR', 'QS', 'QT', 'QV', 'QW', 'QY', 
    'RA', 'RC', 'RD', 'RE', 'RF', 'RG', 'RH', 'RI', 'RK', 'RL', 'RM', 'RN', 'RP', 'RQ', 'RR', 'RS', 'RT', 'RV', 'RW', 'RY', 
    'SA', 'SC', 'SD', 'SE', 'SF', 'SG', 'SH', 'SI', 'SK', 'SL', 'SM', 'SN', 'SP', 'SQ', 'SR', 'SS', 'ST', 'SV', 'SW', 'SY', 
    'TA', 'TC', 'TD', 'TE', 'TF', 'TG', 'TH', 'TI', 'TK', 'TL', 'TM', 'TN', 'TP', 'TQ', 'TR', 'TS', 'TT', 'TV', 'TW', 'TY', 
    'VA', 'VC', 'VD', 'VE', 'VF', 'VG', 'VH', 'VI', 'VK', 'VL', 'VM', 'VN', 'VP', 'VQ', 'VR', 'VS', 'VT', 'VV', 'VW', 'VY', 
    'WA', 'WC', 'WD', 'WE', 'WF', 'WG', 'WH', 'WI', 'WK', 'WL', 'WM', 'WN', 'WP', 'WQ', 'WR', 'WS', 'WT', 'WV', 'WW', 'WY', 
    'YA', 'YC', 'YD', 'YE', 'YF', 'YG', 'YH', 'YI', 'YK', 'YL', 'YM', 'YN', 'YP', 'YQ', 'YR', 'YS', 'YT', 'YV', 'YW', 'YY'
    ]

def get_index(aminoacid):
    for i in range(len(global_aminoacids_list)):
        if global_aminoacids_list[i] == aminoacid:
            return i
    return -1

def get_dipeptide_index(dipeptide):
    for i in range(len(global_dipeptide_list)):
        if dipeptide == global_dipeptide_list[i]:
            return i
    return -1

def aminoacids_frequencies(sequence):
    frequencies = [0 for el in global_aminoacids_list]
    for aa in sequence:
        tmp_index = get_index(aa)
        if tmp_index == -1:
            print('error in aminoacids frequencies computation. The sequence may have an unknown symbol. Return')
            return
        frequencies[tmp_index] += 1
    return np.array([el/len(sequence) for el in frequencies])
    
def multiplet_frequencies(sequence):
    return 0

def dipeptide_frequencies(sequence):
    frequencies = [0 for el in global_dipeptide_list]
    for i in range(len(sequence)-1):
        tmp_index = get_dipeptide_index(str(sequence[i]) + str(sequence[i+1]))
        if tmp_index == -1:
            print('error in dipeptide frequencies computation. The sequence may have an unknown symbol. Return')
            return
        frequencies[tmp_index] += 1
    return np.array([el/(len(sequence)-1) for el in frequencies])

def moment_computation(sequence, X_m, r):
    c = ['R', 'K', 'E', 'D'] # charged aminoacids
    moment = 0
    count = 0
    for i in range(len(sequence)):
        if sequence[i] in c:
            count += 1
            moment += (i-X_m)**r
    print(r, moment/count)
    return moment/count

def charge_composition(sequence):
    # with odds moments the M_r could be 0
    c = ['R', 'K', 'E', 'D'] # charged aminoacids
    f_c = 0
    X_m = 0
    for i in range(len(sequence)):
        if sequence[i] in c:
            f_c += 1
            X_m += i
    X_m /= f_c
    f_c /= len(sequence)
    to_return = [f_c, len(sequence)]
    for r in range(2, 26):
        to_return.append(moment_computation(sequence, X_m, r))
    return np.array(to_return)

def hydrophobic_composition(sequence):
    