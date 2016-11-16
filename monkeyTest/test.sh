#!/bin/bash

# --------------使用说明：------------------------

# -p参数指定要测试的包名
# --throttle 每个事件之间的间隔事件，单位为毫秒
# -s 指定seed值，如果sed值相同，那么两次执行的随机事件也相同
# -v 指定日志级别，一共有3个日志级别0,1,2（-v ： 级别0；-v -v 级别1；-v -v -v 级别2）
#  -v  默认选项 ，仅提供启动提示、测试完成和最终结果等少量信息
#  -v -v 提供较为详细的日志，包括每个发送到Activity的事件信息
#  -v -v -v最详细的日志，包括了测试中选中/未选中的Activity信息

adb shell monkey -p com.yixia.videoeditor --throttle 500 -s 12  -v -v 5000 | tee monkeyTest.log

