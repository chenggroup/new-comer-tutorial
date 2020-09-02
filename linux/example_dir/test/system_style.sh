#!/bin/bash

SYSTEM=`uname -s` # 获取操作系统类型

if [ $SYSTEM = "Linux" ] ; then # 如果是linux话输出linux字符串

    echo "Linux"

    elif [ $SYSTEM = “FreeBSD” ] ; then # 如果是FreeBSD话输出FreeBSD字符串

        echo "FreeBSD"

    else

        echo “What?” # 如果两者都不是就输出What字符串

fi # 判断结束， 以fi结尾


