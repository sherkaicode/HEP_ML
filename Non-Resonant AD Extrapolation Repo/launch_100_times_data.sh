#!/bin/bash

# Path to your MadGraph process directory
PROCESS_DIR="passport/non-res/madgraph_files/pp2jj_data_test/"
cd $PROCESS_DIR
# Loop to run MadEvent 100 times
for i in {1..100}
do

    ./bin/madevent launch -f

    echo "Completed run_$i"
done
