HTKに関するメモ
===============

注意事項メモ
------------
##### Ubuntu (64 bit) にインストールしたときのメモ
+ bits/predefs.hがない　→　libc6-dev-i386 
+ -lX11 がない →　libx11-dev:i386

i386版を有効にするには以下のようにする

    dpkg --add-architecture i386
    apt-get update

##### 使用時の注意: ファイル名に関して
+ ファイル名にスペースや `'` や `.` が含まれないようにした方が安心（未検証）
+ ファイル名が長すぎるとセグメンテーション違反が起きる（おそらく64文字程度が上限？）

例えば以下のようにする
    
    LABEL="I'm_living_in_Tokyo,Japan!(2014).lab"
    LABEL2=`echo "${LABEL%.lab}" | \
        sed -e "s/'//g" | \
        sed -e "s/!//g" | \
        sed -e "s/,//g" | \
        sed -e "s/\.//g" | \
        sed -e "s/(//g" | \
        sed -e "s/)//g" | \
        cut -c 1-15`.lab
    echo ${LABEL2}
