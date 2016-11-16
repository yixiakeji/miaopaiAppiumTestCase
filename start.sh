#!/bin/bash

rm test.log
rm ./errorScreenShot/*.png
python startTest.py | tee test.log

