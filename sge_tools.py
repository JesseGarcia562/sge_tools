import pandas as pd
import numpy as numpy

def convert_to_gb(string):
    conversion = {'T':1024.,'G':1.,'M':1./1024.,'K':1./1024./1024}
    string_updated = str(string)
    stem = string_updated[:-1]
    suffix = string_updated[-1]
    conversion_factor = conversion[suffix]
    try:
        number_of_gb = conversion_factor * float(stem)
    except:
        number_of_gb = numpy.nan
    return number_of_gb

def sge_qacct_parse(file_path):
    """A simple function that parses qacct -j output from the hoffman2 cluster at UCLA into a pandas dataframe.
    
    In order to get the qacct output, you need the job id number. With the job id number (job_id) run "qacct -j job_id > qacct_output.txt" without
    the quotation marks and have the text 'job_id' be the job_id number. Run this function on the file path to retrieve a pandas dataframe of the text.
    """
   
    # Parse qacct log file into dictionary 
    dicts=[]
    with open(file_path, 'r') as f: 
        d = {}
        for line in f:
            if line[0:3] == "===" or line[0:18] == 'Total System Usage':
                dicts.append(d)
                d = {}
                continue
            if line[0:13] == "    WALLCLOCK":
                break
            field = line[0:13].strip()
            value = line[13:-1].strip()
            d[field] = value
    # Remove first element in dicts list, which is empty
    del dicts[0]
    
    
    
    # Load data into dataframe and set correct types
    df = pd.DataFrame(dicts)
    # set_trace()
    floatfields = ['priority',
    'ru_wallclock',
    'ru_utime',
    'ru_stime',
    'ru_maxrss',
    'ru_ixrss',
    'ru_ismrss',
    'ru_idrss',
    'ru_isrss',
    'ru_minflt',
    'ru_majflt',
    'ru_nswap',
    'ru_inblock',
    'ru_oublock',
    'ru_msgsnd',
    'ru_msgrcv',
    'ru_nsignals',
    'ru_nvcsw',
    'ru_nivcsw',
    'cpu',
    'mem',
    'io',
    'iow']
    for field in floatfields: 
            df[field] = df[field].astype('float')
    
    df["maxvmem"] = df["maxvmem"].apply(lambda s: convert_to_gb(s) )
    df["maxvmem"] = df["maxvmem"].astype('float')
    datefields = ['qsub_time','start_time','end_time']
    for field in datefields: 
        df[field] = pd.to_datetime(df[field])  #,format='%m/%d/%y %I:%M%p'
    intfields = ['slots','jobnumber','taskid','exit_status'] 
    for field in intfields: 
        df[field] = df[field].astype('int')

    return df