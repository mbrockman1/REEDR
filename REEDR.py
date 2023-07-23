#!/usr/bin/env python
# coding: utf-8

# In[1]:


from striprtf.striprtf import rtf_to_text
from os import listdir

import pandas as pd


# In[ ]:





# In[2]:


def keyword_cleaner(keyword):
    try:
        colon_index = keyword.index(':')
        len_index = len(keyword)
        return(keyword[0:colon_index].strip())
    except(ValueError):
        return(keyword.strip())

def val_cleaner(temp_line):
    for idx, char in enumerate(temp_line):
        if char.isdigit():
            break
    try:
        return(temp_line[idx: len(temp_line)].strip())
    except(UnboundLocalError):
        print(temp_line)
        
def reporting_sys(file):
    file = file.split('\n')
    for line in file:
        if 'Contributor system' in line:
            #works
            return(line.split(
                'Contributor system:\t')[1])

TWO_D_CALC_LIST = [
    ('LA vol: ', 'ml'),
    ('AI max vel: ', 'cm/sec'),
    ('EPSS: ', 'cm'),
    ('LV V1 max ', 'cm/sec'),
    ('MV dec time: ', 'sec'),
    ('MV E/A: ', 'cm'),
    ('FS ', '%'),
    ('Ao mean PG ', 'mmHg'),
    ('AVA(V,D) ', 'cm2'),
    ('MV max PG: ', 'mmHg'),
    ('ACS: ', 'cm'),
    ('MM R-R int ', 'sec'),
    ('Ao V2 max ', 'cm/sec'),
    ('EF(MOD-sp2): ', '%'),
    ('AI max PG: ', 'mmHg'),
    ('Ao V2 max: ', 'cm/sec'),
    ('MV V2 max: ', 'cm/sec'),
    ('PA mean ', 'cm/sec'),
    ('TR max PG: ', 'mmHg'),
    ('EF(MOD-sp4): ', '%'),
    ('FS: ', '%'),
    ('MV A point ', 'cm/sec'),
    ('Pulm. R-R: ', 'sec'),
    ('PA max PG ', 'mmHg'),
    ('MV E max vel: ', 'cm/sec'),
    ('PA max PG: ', 'mmHg'),
    ('EDV(MOD-sp2): ', 'ml'),
    ('% IVS thick: ', '%'),
    ('Pulm Dias Vel: ', 'cm/sec'),
    ('LVIDs: ', 'cm'),
    ('PI max vel: ', 'cm/sec'),
    ('MV A dur: ', 'sec'),
    ('EDV(MOD-sp2) ', 'ml'),
    ('LA A4 area: ', 'cm2'),
    ('RAP systole ', 'mmHg'),
    ('LA/Ao: ', 'cm'),
    ('EDV(MOD-sp4): ', 'ml'),
    ('Pulm Sys Vel: ', 'cm/sec'),
    ('PA mean PG: ', 'mmHg'),
    ('RVSP(TR): ', 'mmHg'),
    ('TR Max vel ', 'cm/sec'),
    ('LA A2 area: ', 'cm2'),
    ('MR max PG: ', 'l/min'),
    ('TR Max PG ', 'cm/sec'),
    ('LV V1 max: ', 'cm/sec '),
    ('Ao mean PG: ', 'mmHg'),
    ('LA length (vol): ', 'cm'),
    ('Ao max PG: ', 'mmHg'),
    ('IVSs: ', 'cm'),
    ('AVA (Dim Index): ', 'cm2'),
    ('Ao V2 VTI: ', 'cm'),
    ('TR max vel: ', 'cm/sec'),
    ('PI end-d vel: ', 'cm/sec'),
    ('LV EDV (BP): ', 'ml'),
    ('LVPWs: ', 'cm'),
    ('RVOT diam: ', 'cm'),
    ('LA dimension ', 'cm'),
    ('PA V2 max ', 'cm/sec'),
    ('PA acc time ', 'sec'),
    ('MV max PG ', 'mmHg'),
    ('MV P1/2t max vel ', 'cm/sec'),
    ('MV P1/2t ', 'msec'),
    ('MV V2 max ', 'cm/sec'),
    ('MVA(P1/2t) ', 'cm2'),
    ('MR max vel ', 'cm/sec'),
    ('LA Volume A-L (BP): ', 'ml'),
    ('asc Aorta Diam: ', 'cm'),
    ('RVSP ', 'mmHg'),
    ('LVOT diam: ', 'cm'),
    ('IVSd: ', 'cm'),
    ('AI VTI: ', 'cm'),
    ('LVPWs ', 'cm'),
    ('IVSd ', 'cm'),
    ('RA Volume: ', 'ml'),
    ('MR max vel: ', 'cm'),
    ('MR max PG ', 'cm'),
    ('LV V1 VTI ', 'cm'),
    ('MV mean PG ', 'mmHg'),
    ('RVSP ', 'mmHG'),
    ('Pulm. HR: ', 'BPM'),
    ('LV V1 VTI: ', 'cm'),
    ('Ao root diam ', 'cm'),
    ('RV S Vel: ', 'cm/sec'),
    ('MV dec time ', 'sec'),
    ('PI max PG: ', 'mmHg'),
    ('% IVS thick ', '%'),
    ('AVA(V,D): ', 'cm2'),
    ('RAP systole: ', 'mmHg'),
    ('MV E point ', 'cm/sec'),
    ('LV EF (MOD) BP: ', '%'),
    ('LA/Ao ', 'cm'),
    ('MM HR ', 'BPM'),
    ('MM R-R int: ', 'sec'),
    ('ACS ', 'cm'),
    ('RVDd ', 'cm'),
    ('ASC: ', 'cm'),
    ('EF(Teich): ', '%'),
    ('LVPWd ', 'cm'),
    ('ESV(MOD-sp4): ', 'ml'),
    ('EF(Teich) ', '%'),
    ('MV mean PG: ', 'mmHg'),
    ('TAPSE: ', 'cm'),
    ('LVOT diam ', 'cm'),
    ('Ao max PG ', 'mmHg'),
    ('MV P1/2t  ', 'msec'),
    ('LV ESV (BP): ', 'ml'),
    ('MV A max vel: ', 'cm/sec'),
    ('MR max PG ', 'mmHg'),
    ('Ao V2 VTI ', 'cm'),
    ('PA pr(Accel) ', 'mmHg'),
    ('RA Area 4Cs: ', 'cm2'),
    ('Pulm A Revs Dur: ', 'sec'),
    ('MM HR: ', 'BPM'),
    ('MVA(VTI): ', 'cm2'),
    ('LVIDd ', 'cm'),
    ('IVSs ', 'cm'),
    ('ESV(MOD-sp2)', 'ml'),
    ('MR max vel  ', 'cm/s'),
    ('LVIDs ', 'cm'),
    ('PA V2 max: ', 'cm/sec'),
    ('MV E max vel ', 'cm/sec'),
    ('RVDd: ', 'cm'),
    ('LA Volume A-L (BP) index: ', 'ml/m2'),
    ('TR Max PG ', 'mmHg'),
    ('AVA(I,D): ', 'cm2'),
    ('ESV(MOD-sp2): ', 'ml'),
    ('CO(MOD-sp4): ', 'l/min'),
    ('Pulm A Revs Vel: ', 'cm/sec'),
    ('AVA(I,D) ', 'cm2')
]


# In[3]:


class philips_echo(object):
    def __init__(self, file):
        file = file.split('\n')
        
        self.height = 'N/A'
        self.weight = 'N/A'
        self.bsa = 'N/A'
        self.bp = 'N/A'
        self.reason = 'N/A'
        self.hr = 'N/A'
        self.la_dimension = 'N/A'
        self.lvpwd = 'N/A'
        
        calc_key = [doublet[0] for doublet in TWO_D_CALC_LIST]
        keywords = [keyword_cleaner(calcs[0]) for calcs in TWO_D_CALC_LIST]

        self.two_d_calc_dict = {}
        
        for line in file:
            if 'Result Date' in line:
                # works
                self.results_date = line.split(
                    'Result Date:\t')[1]
                
            if 'Contributor system' in line:
                #works
                self.contrib_system = line.split(
                    'Contributor system:\t')[1]
                
            if 'Name: ' in line:
                # works
                self.name = line.split(
                    'Name: ')[1].split(
                    'Study Date:')[0].replace(' ', '')
                
            if 'Study Date: ' in line:
                # works
                self.study_date = line.split('Study Date:')[1][0:11]

            if 'MRN: ' in line:
                # works
                temp_mrn = line.split('MRN: ')[1]
                new_str = ''
                for val in temp_mrn:
                    try:
                        int(val)
                        new_str += val
                    except(ValueError):
                        break
                self.mrn = new_str
                
            if 'Height: ' in line:
                # works
                self.height = line.split(
                    'Height: ')[-1].replace(' ', '')
                
                
            if 'Location: ' in line:
                # works
                self.location = line.split(
                    'Location: ')[1][0: 3]
                
            if 'Weight: ' in line:
                # works
                self.weight = line.split(
                    'Weight: ')[-1].replace(' ', '')
                

            if 'DOB: ' in line:
                # works
                self.dob = line.split(
                    'DOB: ')[1][0:11]
                
            if 'Gender: ' in line:
                # works
                self.gender = (
                    line.split(
                    'Gender: ')[1].split(
                    'BSA')[0].replace(' ', ''))[0]
                
            if 'BSA: ' in line:
                # works
                self.bsa = line.split(
                    'BSA: ')[-1].replace(' ', '')

                
            if 'Age: ' in line:
                # works
                self.age = line.split(
                    'Age: ')[1][0:4]
                
            if '  BP: ' in line:
                # works
                self.bp = line.split(
                    'BP: ')[-1].replace(' ', '')
                
            '''
            New line
            '''
            if 'Reason For Study: ' in line:
                # works
                self.reason = line.split(
                    'Reason For Study: ')[1].split(
                    'HR: ')[0].replace(' ', '')
                
            if 'HR: ' in line:
                # works
                self.hr = line.split(
                    'HR: ')[-1].replace(' ', '')


                    
        for line in file:    
            for keyword in keywords:
                if keyword in line:
                    temp_line = line.split(keyword)[1]
                    for sub_key in keywords:
                        if sub_key != keyword:
                            temp_line = temp_line.split(sub_key)[0]
                    self.two_d_calc_dict[keyword] = val_cleaner(temp_line)
                    
    def range_cleaner(self, string):
        if '(' in string and ')' in string:
            string = string.split(')')[0] + ')'
        else:
            string = string.split('cm')[0]
        return(string)
                    


# In[4]:


class labhist_echo(object):
    def __init__(self, file):
        file = file.split('\n')
        
        self.height = 'N/A'
        self.weight = 'N/A'
        self.bsa = 'N/A'
        self.bp = 'N/A'
        self.reason = 'N/A'
        self.hr = 'N/A'
        self.la_dimension = 'N/A'
        self.ao_root_diam = 'N/A'
        self.lvidd = 'N/A'
        self.lvids = 'N/A'
        self.ivsd = 'N/A'
        self.lvpwd = 'N/A'
        


        calc_key = [doublet[0] for doublet in TWO_D_CALC_LIST]
        keywords = [keyword_cleaner(calcs[0]) for calcs in TWO_D_CALC_LIST]

        self.two_d_calc_dict = {}
        
        for line in file:
            if 'Result Date' in line:
                # works
                self.results_date = line.split(
                    'Result Date:\t')[1]
                
            if 'Contributor system' in line:
                #works
                self.contrib_system = line.split(
                    'Contributor system:\t')[1]
                
            if 'Name: ' in line:
                # works
                self.name = line.split(
                    'Name: ')[1].split(
                    'Study Date:')[0].replace(' ', '')
                
            if 'Study Date: ' in line:
                # works
                self.study_date = line.split('Study Date:')[1][0:11]

            if 'MRN: ' in line:
                # works
                temp_mrn = line.split('MRN: ')[1]
                new_str = ''
                for val in temp_mrn:
                    try:
                        int(val)
                        new_str += val
                    except(ValueError):
                        break
                self.mrn = new_str
                
            if 'Height: ' in line:
                # works
                self.height = line.split(
                    'Height: ')[-1].replace(' ', '')
                
                
            if 'Location: ' in line:
                # works
                self.location = line.split(
                    'Location: ')[1][0: 3]
                
            if 'Weight: ' in line:
                # works
                self.weight = line.split(
                    'Weight: ')[-1].replace(' ', '')
                

            if 'DOB: ' in line:
                # works
                self.dob = line.split(
                    'DOB: ')[1][0:11]
                
            if 'Gender: ' in line:
                # works
                self.gender = (
                    line.split(
                    'Gender: ')[1].split(
                    'BSA')[0].replace(' ', ''))[0]
                
            if 'BSA: ' in line:
                # works
                self.bsa = line.split(
                    'BSA: ')[-1].replace(' ', '')

                
            if 'Age: ' in line:
                # works
                self.age = line.split(
                    'Age: ')[1][0:4]
                
            if '  BP: ' in line:
                # works
                self.bp = line.split(
                    'BP: ')[-1].replace(' ', '')
                
            '''
            New line
            '''
            if 'Reason For Study: ' in line:
                # works
                self.reason = line.split(
                    'Reason For Study: ')[1].split(
                    'HR: ')[0].replace(' ', '')
                
            if 'HR: ' in line:
                # works
                self.hr = line.split(
                    'HR: ')[-1].replace(' ', '')
        for line in file:    
            for keyword in keywords:
                if keyword in line:
                    temp_line = line.split(keyword)[1]
                    for sub_key in keywords:
                        if sub_key != keyword:
                            temp_line = temp_line.split(sub_key)[0]
                    self.two_d_calc_dict[keyword] = val_cleaner(temp_line)
                   


# In[ ]:





# In[5]:


FILE_DIR = './echos/'

dir_list = [FILE_DIR + file for file in listdir(FILE_DIR)
            if file.endswith('.rtf')]

echo_list = []
for file_loc in dir_list:
    with open(file_loc, 'r') as file:
        text = file.read()
        text = rtf_to_text(text)
        rep_sys = reporting_sys(text)
        if rep_sys == 'LABHIST':
            echo_list.append(labhist_echo(text))
        elif rep_sys == 'PHILIPS':
            echo_list.append(philips_echo(text))


# In[6]:


data_dict = {}

for pt_data in echo_list:
    data_dict[pt_data.mrn] = {}
    for key, val in pt_data.__dict__.items():
        if key != 'two_d_calc_dict':
            data_dict[pt_data.mrn][key] = val
        else:
            data_dict[pt_data.mrn].update(
                pt_data.two_d_calc_dict)


# In[7]:


df = pd.DataFrame(data_dict).T


# In[ ]:





# In[8]:


df = df.fillna('N/A')


# In[9]:


'''
Combinator
'''


# In[10]:


cleaned_data_dict = {}

def combination_func(var_1, var_2):
    if var_1 != 'N/A' and var_2 == 'N/A':
        return(var_1)
    elif var_1 == 'N/A' and var_2 != 'N/A':
        return(var_2)
    elif var_1 == var_2:
        return(var_1)
    elif var_1 != 'N/A' and var_2 != 'N/A':
        return('COMBO ERROR')
    else:
        return('N/A')

for index, data in df.iterrows():
    temp_dict = {}
    temp_dict['results_date'] = data['results_date']
    temp_dict['contrib_system'] = data['contrib_system']
    temp_dict['name'] = data['name']
    temp_dict['study_date'] = data['study_date']
    temp_dict['mrn'] = data['mrn']
    temp_dict['gender'] = data['gender']
    temp_dict['dob'] = data['dob']
    temp_dict['location'] = data['location']
    temp_dict['age'] = data['age']
    temp_dict['height'] = data['height']
    temp_dict['weight'] = data['weight']
    temp_dict['bsa'] = data['bsa']
    temp_dict['reason'] = data['reason']
    temp_dict['hr'] = data['hr']
    temp_dict['mm_hr'] = data['MM HR']
    temp_dict['mm_rr_int'] = data['MM R-R int']
    temp_dict['acs'] = data['ACS']
    temp_dict['mv_e_point'] = data['MV E point']
    temp_dict['mv_p1_2t_max_vel'] = data['MV P1/2t max vel']
    temp_dict['mv_p1_2t'] = data['MV P1/2t']
    temp_dict['mv_a_point'] = data['MV A point']
    temp_dict['mva_p12t'] = data['MVA(P1/2t)']
    temp_dict['mr_max_vel'] = data['MR max vel']
    temp_dict['mr_max_pg'] = data['MR max PG']
    temp_dict['pa_mean'] = data['PA mean']
    temp_dict['rvsp_tr'] = data['RVSP(TR)']
    temp_dict['rvsp'] = data['RVSP']
    temp_dict['PA pr(Accel)'] = data['PA pr(Accel)']
    temp_dict['PA acc time'] = data['PA acc time']
    temp_dict['EDV(MOD-sp4)'] = data['EDV(MOD-sp4)']
    temp_dict['LV EDV (BP)'] = data['LV EDV (BP)']
    temp_dict['LV EF (MOD) BP'] = data['LV EF (MOD) BP']
    temp_dict['LV ESV (BP)'] = data['LV ESV (BP)']
    temp_dict['ESV(MOD-sp4)'] = data['ESV(MOD-sp4)']
    temp_dict['ESV(MOD-sp2)'] = data['ESV(MOD-sp2)']
    temp_dict['EF(MOD-sp4)'] = data['EF(MOD-sp4)']
    temp_dict['EF(MOD-sp2)'] = data['EF(MOD-sp2)']
    temp_dict['IVSs'] = data['IVSs']
    temp_dict['LA Volume A-L (BP)'] = data['LA Volume A-L (BP)']
    temp_dict['LA Volume A-L (BP) index'] = data['LA Volume A-L (BP) index']
    temp_dict['RA Area 4Cs'] = data['RA Area 4Cs']
    temp_dict['Pulm. R-R'] = data['Pulm. R-R']
    temp_dict['Pulm. HR'] = data['Pulm. HR']
    temp_dict['MV A dur'] = data['MV A dur']
    temp_dict['MV A max vel'] = data['MV A max vel']
    temp_dict['AVA (Dim Index)'] = data['AVA (Dim Index)']
    temp_dict['MVA(VTI)'] = data['MVA(VTI)']
    temp_dict['Pulm Sys Vel'] = data['Pulm Sys Vel']
    temp_dict['Pulm Dias Vel'] = data['Pulm Dias Vel']
    temp_dict['PA mean PG'] = data['PA mean PG']
    temp_dict['Pulm A Revs Vel'] = data['Pulm A Revs Vel']
    temp_dict['Pulm A Revs Dur'] = data['Pulm A Revs Dur']


    temp_dict['la_dimension'] = combination_func(data['la_dimension'], data['LA dimension'])
    temp_dict['ao_root_diam'] = combination_func(data['ao_root_diam'], data['Ao root diam'])
    temp_dict['lvidd'] = combination_func(data['lvidd'], data['LVIDd'])
    temp_dict['lvids'] = combination_func(data['lvids'], data['LVIDs'])
    temp_dict['ivsd'] = combination_func(data['ivsd'], data['IVSd'])
    temp_dict['lvpwd'] = combination_func(data['lvpwd'], data['LVPWd'])
    temp_dict['rvdd'] = combination_func(data['RVDd'], data['RVDd'])
    temp_dict['fs'] = combination_func(data['FS'], data['FS'])
    temp_dict['ef_teich'] = combination_func(data['EF(Teich)'], data['EF(Teich)'])
    temp_dict['lvpws'] = combination_func(data['LVPWs'], data['LVPWs'])
    temp_dict['%_ivs_thick'] = combination_func(data['% IVS thick'], data['% IVS thick'])
    temp_dict['lvot_diam'] = combination_func(data['LVOT diam'], data['LVOT diam'])
    temp_dict['lvot_diam'] = combination_func(data['LVOT diam'], data['LVOT diam'])
    temp_dict['edv_mod_sp2'] = combination_func(data['EDV(MOD-sp2)'], data['EDV(MOD-sp2)'])
    temp_dict['edv_mod_sp2'] = combination_func(data['EDV(MOD-sp2)'], data['EDV(MOD-sp2)'])
    temp_dict['mv_v2_max'] = combination_func(data['MV V2 max'], data['MV V2 max'])
    temp_dict['mv_max_pg'] = combination_func(data['MV max PG'], data['MV max PG'])
    temp_dict['mv_mean_pg'] = combination_func(data['MV mean PG'], data['MV mean PG'])                                              
    temp_dict['mv_dec_time'] = combination_func(data['MV dec time'], data['MV dec time']) 
    temp_dict['ao_v2_max'] = combination_func(data['Ao V2 max'], data['Ao V2 max'])
    temp_dict['lv_v1_max'] = combination_func(data['LV V1 max'], data['LV V1 max'])
    temp_dict['ao_max_pg'] = combination_func(data['Ao max PG'], data['Ao max PG'])
    temp_dict['lv_v1_vti'] = combination_func(data['LV V1 VTI'], data['LV V1 VTI'])
    temp_dict['ao_mean_pg'] = combination_func(data['Ao mean PG'], data['Ao mean PG'])
    temp_dict['ao_v2_vti'] = combination_func(data['Ao V2 VTI'], data['Ao V2 VTI'])
    temp_dict['ava_id'] = combination_func(data['AVA(I,D)'], data['AVA(I,D)'])
    temp_dict['ava_vd'] = combination_func(data['AVA(V,D)'], data['AVA(V,D)'])
    temp_dict['pa_v2_max'] = combination_func(data['PA V2 max'], data['PA V2 max'])
    temp_dict['tr_max_vel'] = combination_func(data['TR Max vel'], data['TR max vel'])
    temp_dict['mv_e_max_vel'] = combination_func(data['MV E max vel'], data['MV E max vel'])
    temp_dict['rap_systole'] = combination_func(data['RAP systole'], data['RAP systole'])
    temp_dict['pa_max_pg'] = combination_func(data['PA max PG'], data['PA max PG'])
    temp_dict['tr_max_pg'] = combination_func(data['TR Max PG'], data['TR max PG'])
    cleaned_data_dict[data['mrn']] = temp_dict


# In[11]:


df = pd.DataFrame(cleaned_data_dict).T
df.to_excel('results.xlsx')


# In[ ]:





# In[ ]:




