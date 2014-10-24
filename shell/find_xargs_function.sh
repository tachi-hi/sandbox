#!/bin/bash

myProc(){
	arg1=$1
	arg2=$2
	echo $arg1 is a .txt file
	echo $arg2
}
export -f myProc

find . -name "*.txt" | xargs -I {} bash -c "myProc {} 'Hello World'"

