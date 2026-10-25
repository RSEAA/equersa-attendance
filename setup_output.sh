#!/bin/bash
# python3 -v venv
# pip install rapidfuzz 
for f in *.csv; do tail -n +2 "$f" | cut -d, -f1; done | sort -u > output.txt
# for f in RSAfrica*.csv; do tail -n +2 "$f" | cut -d, -f1; done | sort -u > output_rsafrica.txt
# for f in RSAA*.csv; do tail -n +2 "$f" | cut -d, -f1; done | sort -u > output_rsaa.txt
