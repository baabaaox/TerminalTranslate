#!/bin/bash

# echo 'test' >> test.txt

basepath=$(cd `dirname $0`; pwd)
# alias tt=$basepath'/TerminalTranslate.py'
echo alias tt="$basepath/TerminalTranslate.py" >> /etc/bash.bashrc
