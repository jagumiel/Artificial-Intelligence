#!/bin/bash
input=output.csv
while IFS= read -r line
do
	cc=$(echo $line | cut -d ";" -f1)
	dni=$(echo $line | cut -d ";" -f2)
	tarifa=$(echo $line | cut -d ";" -f3)
	codPos=$(echo $line | cut -d ";" -f4)
	maxPow=$(echo $line | cut -d ";" -f5)
	timeStmp=$(echo $line | cut -d ";" -f6)
	EnergyW=$(echo $line | cut -d ";" -f7)

	cc_hash=$(echo -n "$cc" | openssl dgst -sha256 | cut -d " " -f2)
	dni_hash=$(echo -n "$dni" | openssl dgst -sha256 | cut -d " " -f2)

	hashed_line="$cc_hash;$dni_hash;$tarifa;$codPos;$maxPow;$timeStmp;$EnergyW"
	echo "$hashed_line"
done < "output.csv"
