import pandas as pd
import os

csv_path = '/media/xysong/Disk_2/protocols/ijbc_11_covariate_probe_reference.csv'
csv_pair_path = '/media/xysong/Disk_2/protocols/ijbc_11_covariate_matches.csv'

info_cordinate = pd.read_csv(csv_path,usecols = ['TEMPLATE_ID','SUBJECT_ID'])
pair_cordinate = pd.read_csv(csv_pair_path,names=["TEMPLATE_ID", "TEMPLATE_ID_2"])

template_dic = {}
template_index = {}
for i in range(0,140739):
    
    template_id = info_cordinate['TEMPLATE_ID'][i]
    subject_id = info_cordinate['SUBJECT_ID'][i]
    template_dic[template_id] = subject_id
    template_index[template_id] = i+1
f = open('covariate_pair_xysong.txt', 'w+')

label = 0
label_1_count = 0
label_0_count = 0
for j in range(0,47404001):
    tem_1 = pair_cordinate['TEMPLATE_ID'][j]
    tem_2 = pair_cordinate['TEMPLATE_ID_2'][j]
    if template_dic[tem_1] == template_dic[tem_2]:
        label = 1
        label_1_count += 1        
    else:
        label = 0
        label_0_count +=1
    f.write(str(template_index[tem_1]) + '\t' + str(template_index[tem_2]) + '\t' + str(label) + '\n') 
print('label 1 number:' + str(label_1_count))
print('label 0 number:' + str(label_0_count))

f.close()
