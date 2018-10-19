import sys

from adb_android import adb_android


def my_except_hook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print "Handler code goes here"
        m = 0
        while m <= i:
            adb_android.pull("/sdcard/demo{0}.mp4".format(m), ".")
            m = m + 1
            print m
    else:
        sys.__excepthook__(exctype, value, traceback)


sys.excepthook = my_except_hook

adb_android.get_state()
adb_android.wait_for_device()

i = 0
while i < 100000000:
    adb_android.wait_for_device()
    adb_android.shell("screenrecord --time-limit 180 /sdcard/demo{0}.mp4".format(i))
    print i
    i = i + 1
pass
