#!/bin/bash
conda activate hotspots

#nohup python create_databases.py "akt1" > akt1.out 2> akt1.err &
#nohup python create_databases.py "ampc" > logs/ampc.out 2> logs/ampc.err &
#nohup python create_databases.py "cp3a4" > cp3a4.out 2> cp3a4.err &
#nohup python create_databases.py "cxcr4" > logs/cxcr4.out 2> logs/cxcr4.err &
#nohup python create_databases.py "gcr" > gcr.out 2> gcr.err &
nohup python create_databases.py "hivpr" > hivpr.out 2> hivpr.err &
#nohup python create_databases.py "hivrt" > hivrt.out 2> hivrt.err &
#nohup python create_databases.py "kif11" > kif11.out 2> kif11.err &