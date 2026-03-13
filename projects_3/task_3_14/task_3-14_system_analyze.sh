#!/bin/bash

df -h | awk 'NR > 1 {
	print $1, $5
}'
df -h | awk 'NR > 1 {
	if ($5 > 90){
		print "Внимание! Заполнено более 90% файловой системы."
	}
}'
