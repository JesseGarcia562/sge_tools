# Parsing Hoffman2 UCLA qacct output

This is a fork from willem4/sge_tools and I just changed a few things to get it to work with UCLA's HPC.

## Getting the qacct_output. 

Use "qacct -j job_id > hoffman2_qacct_output.txt" to get the output into a text file. For example if your job array has the job_id as 1523 you would run:

```bash
qacct -j job_id > hoffman2_qacct_output.txt
```

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
