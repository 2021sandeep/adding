import uiautomator2 as u2
import time

d=u2.connect()
d.app_start("com.android.launcher3")
time.sleep(3)
d(resourceId="com.android.camera:id/shutter_button").click()
time.sleep(3)
d.press("back")

