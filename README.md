# Creating a more accessible platform for Neurofeedback using an open source EEG

This project takes recorded EEG data from the OpenBCI GUI, formats it work with brainflow, and scores each session for EEG metrics of concentration and relaxation.

# How to:
1. run 'python process.py' to format the files in the recording folder
2. run 'python .\eeg_metrics.py --board-id -3 --other-info 0 --file 'Filter\file_name.txt.fil' to score file