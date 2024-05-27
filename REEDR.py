#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from striprtf.striprtf import rtf_to_text
from os import listdir

import pandas as pd
import re


# In[ ]:


def interp_eval(interp_str):
    result_dict = {}
    try:
        result_dict['Wall Motion'] = re.findall(r"([^.]*?wall motion abnormalities[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Wall Motion'] = "None"
        
    try:
        result_dict['Aortic Valve'] = re.findall(r"([^.]*?aortic valve[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Aortic Valve'] = "None"
    
    try:
        result_dict['Mitral Valve'] = re.findall(r"([^.]*?mitral valve[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Mitral Valve'] = "None"
        
    try:
        result_dict['Tricuspid Valve'] = re.findall(r"([^.]*?tricupsid valve[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Tricuspid Valve'] = "None"
        
    try:
        result_dict['Pulmonic Valve'] = re.findall(r"([^.]*?pulmonic valve[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Pulmonic Valve'] = "None"
        
    try:
        result_dict['Pericardial Effusion'] = re.findall(r"([^.]*?pericardial[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Pericardial Effusion'] = "None"
        
    try:
        result_dict['Pulm HTN'] = re.findall(r"([^.]*?pulmonary[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Pulm HTN'] = "None"
        
    try:
        result_dict['ASD Assessment'] = re.findall(r"([^.]*?ASD[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['ASD Assessment'] = "None"
        
    try:
        result_dict['VSD Assessment'] = re.findall(r"([^.]*?VSD[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['VSD Assessment'] = "None"
        
    try:
        result_dict['Thrombus Assessment'] = re.findall(r"([^.]*?thrombus[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Thrombus Assessment'] = "None"
        
    try:
        result_dict['Dissection Assessment'] = re.findall(r"([^.]*?dissection[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Dissection Assessment'] = "None"
        
    try:
        result_dict['Strain Assessment'] = re.findall(r"([^.]*?strain[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Strain Assessment'] = "None"
        
    try:
        result_dict['Tamponade Assessment'] = re.findall(r"([^.]*?tamponade[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Tamponade Assessment'] = "None"
        
    try:
        result_dict['Dehiscence Assessment'] = re.findall(r"([^.]*?dehisc[^.]*\.)",interp_str)[0]
    except(IndexError):
        result_dict['Dehiscence Assessment'] = "None"
        
    return(result_dict)


# In[ ]:


def reporting_sys(file):
    file = file.split('\n')
    contrib_sys = ''
    for line in file:
        if 'Contributor system' in line:
            #works
            contrib_sys = line.split(
                'Contributor system:\t')[1]
    if contrib_sys == 'LABHIST':
        return(labhist_demographics(text))
    elif contrib_sys == 'PHILIPS':
        return(philips_demographics(text))

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

DICT_VARS = ['results_date', 'contrib_system', 'name', 'study_date',
'mrn', 'gender', 'dob', 'location', 'age', 'height', 'weight',
'bsa', 'reason', 'hr', 'MM HR', 'MM R-R int', 'ACS', 'MV E point',
'MV P1/2t max vel', 'MV P1/2t', 'MV A point', 'MVA(P1/2t)',
'MR max vel', 'MR max PG', 'PA mean', 'RVSP(TR)', 'RVSP', 
'PA pr(Accel)', 'PA acc time', 'EDV(MOD-sp4)', 'LV EDV (BP)',
'LV EF (MOD) BP', 'LV ESV (BP)', 'ESV(MOD-sp4)', 'ESV(MOD-sp2)',
'EF(MOD-sp4)', 'EF(MOD-sp2)', 'IVSs', 'LA Volume A-L (BP)',
'LA Volume A-L (BP) index', 'RA Area 4Cs', 'Pulm. R-R', 
'Pulm. HR', 'MV A dur', 'MV A max vel', 'AVA (Dim Index)',
'MVA(VTI)','Pulm Sys Vel','Pulm Dias Vel','PA mean PG',
'Pulm A Revs Vel', 'Pulm A Revs Dur','ivc_diam', 'ao_root_diam',
'lvidd', 'lvids', 'ivsd', 'TR Max vel', 'TR Max PG', 'TAPSE']


# In[ ]:


def philips_demographics(file):
    file = file.split('\n')
    demo_dict = {}
    for idx, line in enumerate(file):
        if 'Result Date' in line:
            # works
            demo_dict['Results Date'] = line.split(
                'Result Date:\t')[1]

        if 'Contributor system' in line:
            #works
            demo_dict['Contrib System'] = line.split(
                'Contributor system:\t')[1]
            
        if 'Encounter info' in line:
            encounter_list = line.strip('Encounter info:\t').split(',')
            fin = encounter_list[0]
            admit_location = encounter_list[2].strip(' ')
            admit_date, discharge_date = encounter_list[3].replace(' ', '').split('-')
            demo_dict['fin'] = fin
            demo_dict['admit_location'] = admit_location
            demo_dict['admit_date'] = admit_date
            demo_dict['discharge_date'] = discharge_date
            

        if 'Name: ' in line:
            # works
            demo_dict['Name'] = line.split(
                'Name: ')[1].split(
                'Study Date:')[0].replace(' ', '')

        if 'Study Date: ' in line:
            # works
            demo_dict['Study Date'] = line.split('Study Date:')[1][0:11]

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
            demo_dict['MRN'] = new_str

        if 'Height: ' in line:
            # works
            demo_dict['Height'] = line.split(
                'Height: ')[-1].replace(' ', '')


        if 'Location: ' in line:
            # works
            demo_dict['Location'] = line.split(
                'Location: ')[1][0: 3]

        if 'Weight: ' in line:
            # works
            demo_dict['Weight'] = line.split(
                'Weight: ')[-1].replace(' ', '')


        if 'DOB: ' in line:
            # works
            demo_dict['DOB'] = line.split(
                'DOB: ')[1][0:11]

        if 'Gender: ' in line:
            # works
            demo_dict['Gender'] = (
                line.split(
                'Gender: ')[1].split(
                'BSA')[0].replace(' ', ''))[0]

        if 'BSA: ' in line:
            # works
            demo_dict['BSA'] = line.split(
                'BSA: ')[-1].replace(' ', '')


        if 'Age: ' in line:
            # works
            demo_dict['AGE'] = line.split(
                'Age: ')[1][0:4]

        if '  BP: ' in line:
            # works
            demo_dict['BP'] = line.split(
                'BP: ')[-1].replace(' ', '')

        if 'inferior vena cava' in line and 'appeared' in line:
            next_line = 1
            if 'inferior vena cava' in line and 'appeared' in line:
                ivc_diam = line.split('appeared')[-1]
                while '.' not in ivc_diam:
                    ivc_diam += file[idx + next_line]
                    next_line += 1
                ivc_diam = ivc_diam.split('.')[0]
            demo_dict['IVC Diam'] = ivc_diam

        '''
        New line
        '''
        if 'Reason For Study: ' in line:
            # works
            demo_dict['Reason'] = line.split(
                'Reason For Study: ')[1].split(
                'HR: ')[0].replace(' ', '')

        if 'HR: ' in line:
            # works
            demo_dict['HR'] = line.split(
                'HR: ')[-1].replace(' ', '')
    return(demo_dict)

def labhist_demographics(file):
    file = file.split('\n')
    demo_dict = {}
    for idx, line in enumerate(file):
        if 'Result Date' in line:
            # works
            demo_dict['Results Date'] = line.split(
                'Result Date:\t')[1]

        if 'Contributor system' in line:
            #works
            demo_dict['Contrib System'] = line.split(
                'Contributor system:\t')[1]

        if 'Name: ' in line:
            # works
            demo_dict['Name'] = line.split(
                'Name: ')[1].split(
                'Study Date:')[0].replace(' ', '')

        if 'Study Date: ' in line:
            # works
            demo_dict['Study Date'] = line.split('Study Date:')[1][0:11]

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
            demo_dict['MRN'] = new_str

        if 'Height: ' in line:
            # works
            demo_dict['Height'] = line.split(
                'Height: ')[-1].replace(' ', '')


        if 'Location: ' in line:
            # works
            demo_dict['Location'] = line.split(
                'Location: ')[1][0: 3]

        if 'Weight: ' in line:
            # works
            demo_dict['Weight'] = line.split(
                'Weight: ')[-1].replace(' ', '')


        if 'DOB: ' in line:
            # works
            demo_dict['DOB'] = line.split(
                'DOB: ')[1][0:11]

        if 'Gender: ' in line:
            # works
            demo_dict['Gender'] = (
                line.split(
                'Gender: ')[1].split(
                'BSA')[0].replace(' ', ''))[0]

        if 'BSA: ' in line:
            # works
            demo_dict['BSA'] = line.split(
                'BSA: ')[-1].replace(' ', '')


        if 'Age: ' in line:
            # works
            demo_dict['AGE'] = line.split(
                'Age: ')[1][0:4]

        if '  BP: ' in line:
            # works
            demo_dict['BP'] = line.split(
                'BP: ')[-1].replace(' ', '')

        if 'inferior vena cava' in line and 'appeared' in line:
            next_line = 1
            if 'inferior vena cava' in line and 'appeared' in line:
                ivc_diam = line.split('appeared')[-1]
                while '.' not in ivc_diam:
                    ivc_diam += file[idx + next_line]
                    next_line += 1
                ivc_diam = ivc_diam.split('.')[0]
            demo_dict['IVC Diam'] = ivc_diam

        '''
        New line
        '''
        if 'Reason For Study: ' in line:
            # works
            demo_dict['Reason'] = line.split(
                'Reason For Study: ')[1].split(
                'HR: ')[0].replace(' ', '')

        if 'HR: ' in line:
            # works
            demo_dict['HR'] = line.split(
                'HR: ')[-1].replace(' ', '')
    return(demo_dict)


# In[ ]:





# In[ ]:


data_dict = {}

FILE_DIR = './echos/'

dir_list = [FILE_DIR + file for file in listdir(FILE_DIR)
            if file.endswith('.rtf')]

for file_loc in dir_list:
    with open(file_loc, 'r') as file:
        text = file.read()
        text = rtf_to_text(text)
        demo_dict = reporting_sys(text)
        temp_dict = {}
        text_for_interp = text.split('\n')
        after_interp = False
        interp_qualifier = "Interpretation Summary"
        interp_data = ""
        for idx, data in enumerate(text_for_interp):
            if idx > 20 and data == interp_qualifier:
                after_interp = True
            if after_interp == True:
                if "___________________________________" in data:
                    after_interp = False
                else:
                    interp_data += data + " " 
        temp_dict['interpretation_summary'] = interp_data
        for val_unit in TWO_D_CALC_LIST:
            if val_unit[0] in text:
                echo_val = text.split(
                    val_unit[0])[1].split(val_unit[1])[0] + val_unit[1]
                echo_val = echo_val.split('\n')[0]
                echo_val = echo_val.split('          ')[0]
                temp_dict[val_unit[0]] = echo_val
        temp_dict = dict(sorted(temp_dict.items()))
        try:
            demo_dict.update(temp_dict)
            demo_dict.update(interp_eval(interp_data))
            data_dict[demo_dict['MRN']] = demo_dict
        except(AttributeError):
            print("Error")


# In[ ]:


df = pd.DataFrame.from_dict(data_dict).transpose()
df = df.reindex(sorted(df.columns), axis=1)


# In[ ]:


df


# In[ ]:




