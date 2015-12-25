#!/bin/sh

# echo 'test' >> test.txt

basepath=$(cd `dirname $0`; pwd)
case $SHELL in
*/zsh)
    echo alias tt="'$basepath/TerminalTranslate.py -w'" >> ~/.zshrc
    # source ~/.zshrc
    ;;
*/bash)
    echo alias tt="'$basepath/TerminalTranslate.py -w'" >> ~/.bashrc
    # source ~/.bashrc
    ;;
esac
