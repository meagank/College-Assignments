#!/bin/bash

product(){
	local prod=1
	for arg in "$@"; do
		((  prod *= arg ))

	done
	echo "The product of $@ is $prod"

}

if [ -z $1 ]; then
	echo "Usage: $0 val [val [...]]"
	echo "e.g., $0 17 49 3 466"
	exit 0

else
	product $@ 
fi
