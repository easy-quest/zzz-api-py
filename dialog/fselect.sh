#!/data/data/com.termux/files/usr/bin/sh
DIALOG=${DIALOG=dialog}

FILE=`$DIALOG --stdout --title "Выберите файл" --fselect $HOME/ 10 60`

case $? in
    0)
	echo "Выбран \"$FILE\"";;
    1)
	echo "Отказ от ввода.";;
    255)
	echo "Нажата клавиша ESC.";;
esac