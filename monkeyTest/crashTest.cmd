@echo off

rem --------------使用说明：------------------------

rem -p参数指定要测试的包名
rem --throttle 每个事件之间的间隔事件，单位为毫秒
rem -s 指定seed值，如果sed值相同，那么两次执行的随机事件也相同
rem -v 指定日志级别，一共有3个日志级别0,1,2（-v ： 级别0；-v -v 级别1；-v -v -v 级别2）
rem  -v  默认选项 ，仅提供启动提示、测试完成和最终结果等少量信息
rem  -v -v 提供较为详细的日志，包括每个发送到Activity的事件信息
rem  -v -v -v最详细的日志，包括了测试中选中/未选中的Activity信息





rem ----------------执行monkey测试-------------------

powershell "adb shell monkey -p com.lyh.test --throttle 300 -s 10  -v -v 500 | tee crashTest.log"

pause