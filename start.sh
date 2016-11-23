#!/bin/bash

rm test.log
if [ -d ./errorScreenShot ]
then
	echo "errorScreenShot directory is exist !"
else
	mkdir errorScreenShot
fi
rm ./errorScreenShot/*.png
python startTest.py | tee test.log

