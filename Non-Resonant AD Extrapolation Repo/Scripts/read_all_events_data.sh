#!/bin/bash

# Path to your MadGraph process directory
PROCESS_DIR="../"
cd $PROCESS_DIR

# Loop to run the Analyzer 100 times with changing run_xx and qcd_x paths
for i in {23..29}
do
    # Calculate the corresponding run and qcd file numbers
    RUN_NUM=$(printf "%02d" $((i+1)))   # This will generate 01, 02, ..., 99
    QCD_NUM=$((i -23 + 95))  # This will generate 0, 1, 2, ..., 99

    # Update the file paths based on the loop index
    ROOT_FILE_PATH="non-resonant_stuff/passport/non-res/madgraph_files/pp2jj_mc_bg/Events/run_${RUN_NUM}/tag_1_delphes_events.root"
    OUTPUT_FILE_PATH="non-resonant_stuff/passport/non-res/madgraph_files/output_files/mc_bg_out/qcd_${QCD_NUM}.txt"

    # Run the Analyzer.C script with the updated paths
    root -l examples/Analyzer.C'("'"${ROOT_FILE_PATH}"'", "'"${OUTPUT_FILE_PATH}"'")'

    echo "Completed run_$RUN_NUM (qcd_$QCD_NUM)"
done
