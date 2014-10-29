#!/bin/bash

myProc(){
	arg1=$1
	arg2=$2
	echo $arg1 is a .txt file
	echo $arg2
}
export -f myProc

find . -name "*.txt" | xargs -I {} bash -c "myProc {} 'Hello World'"

my_rm_dir(){ # dangerous (to be modified)
	cd $1
	echo * | xargs rm
	cd -
}
export my_rm_dir
