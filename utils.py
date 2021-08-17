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

groups_for_hydroph = [['K', 'E', 'D', 'R'], ['S', 'T', 'N', 'Q'], ['P', 'H'], ['A', 'G', 'Y', 'C', 'W'], ['L', 'V', 'I', 'F', 'M']]
hydroph_scores = [-8, -4, -2, 1, 2]

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
    if len(sequence) == 0:
        return 0
    frequencies = [0 for el in global_aminoacids_list]
    for aa in sequence:
        tmp_index = get_index(aa)
        if tmp_index == -1:
            print('error in aminoacids frequencies computation. The sequence may have an unknown symbol. Return')
            return
        frequencies[tmp_index] += 1
    return np.array([el/len(sequence) for el in frequencies])

def get_aminoacid_mask(sequence, aa):
    new_sequence = []
    for el in sequence:
        if el == aa:
            new_sequence.append(1)
        else:
            new_sequence.append(0)
    return new_sequence

def automata_for_multiplets(binary_seq, n):
    if n <= 2:
        print('error in the multiplets automata. Return')
        return
    state = 0
    counts = 0
    for el in binary_seq:
        if el == 0:
            state = 0
        else:
            state += 1
        if state == n:
            counts += n
        if state > n:
            counts += 1
    return counts
    
def multiplet_frequencies(sequence, n): # count the number of multiplets in total
    if n <= 2:
        print('error in multiplet frequencies computation. n has to be greater than 2. Return')
    if len(sequence) == 0:
        return np.array([0 for el in global_aminoacids_list])
    to_ret = []
    for a in global_aminoacids_list:
        to_ret.append(automata_for_multiplets(get_aminoacid_mask(sequence, a), n))
    to_ret = [el/len(sequence) for el in to_ret]
    return np.array(to_ret)

def dipeptide_frequencies(sequence):
    if len(sequence) == 0:
        np.array([0 for el in global_aminoacids_list])
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
    if count == 0:
        return 0
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
    if f_c == 0:
        X_m = 0
    else:
        X_m /= f_c
    f_c /= len(sequence)
    to_return = [f_c, len(sequence)]
    for r in range(2, 26):
        to_return.append(moment_computation(sequence, X_m, r))
    return np.array(to_return)

def moment_for_hydrophobic_aa(sequence, group, r):
    if (group not in range(5)) or (r not in range(2, 11)):
        print('error in moment computation for hydrophobic amino acids. Return.')
        return
    aa_group = groups_for_hydroph[group]
    mean = 0
    count = 0
    for i in range(len(sequence)):
        if sequence[i] in aa_group:
            count += 1
            mean += i
    if count == 0:
        mean = 0
    else:
        mean /= count
    # moment computation
    to_ret = 0
    for i in range(len(sequence)):
        if sequence[i] in aa_group:
            to_ret += (i-mean)**r
    if count == 0:
        return 0
    return to_ret/count

def hydrophobic_composition(sequence):
    total_score = 0
    groups_scores = [0 for _ in range(5)]
    for el in sequence:
        for i in range(5):
            if el in groups_for_hydroph[i]:
                group_index = i
                score = hydroph_scores[i]
        total_score += score
        groups_scores[group_index] += score
    if total_score == 0:
        hydroph_feature = [0 for group in groups_scores]
    else:
        hydroph_feature = [group/total_score for group in groups_scores]
    print(hydroph_feature)
    # compute the moments
    for group in range(5):
        for j in range(2, 11):
            hydroph_feature.append(moment_for_hydrophobic_aa(sequence, group, j))
    return np.array(hydroph_feature)