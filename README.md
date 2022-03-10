# Parsing Hoffman2 UCLA qacct output

This is a fork from willem4/sge_tools and I just changed a few things to get it to work with UCLA's HPC.

## Getting the qacct_output. 

Use "qacct -j job_id > hoffman2_qacct_output.txt" to get the output into a text file. For example if your job array has the job_id as 1523 you would run:

```bash
qacct -j 1523 > hoffman2_qacct_output.txt
```

**Hoffman2 Cluster's accounting records are archived monthly.**  

The additional option "-f" of the qacct command is required to access records in previous months. If some of your job array elements finished in one month and the others in another month, they will not be localized in the same place. 

For example, job  1868491, some of tasks are in the archive file of February and some are in March. The tasks in February can be found by this command:

```bash
qacct -j 1868491 -f /u/systems/SGE/hoffman2/common/accounting-2022-02 > hoffman2_qacct_output.txt
```

Note the "accounting-2022-02" file. The "-02" corresponds to February. 

## Table of contents

- sge_tools.py - Function to convert existing qacct output to a pandas dataframe
- example_usage.py - An example usage script plot
- hoffman2_qacct_output.txt - Example qacct output file (use "qacct -j" to generate it)

## Dependencies

The functions have the following dependencies. In brackets the versions of the tested versions have been added
- python (3.6.6)
- pandas (0.23.4)
- matplotlib (2.3.3)

## Further reading
[1] https://gist.github.com/SamStudio8/7f2edcfda17906e3941b

[2] http://manpages.ubuntu.com/manpages/cosmic/en/man5/sge_accounting.5.html

[3] http://www.colbyimaging.com/wiki/neuroimaging/tbss
