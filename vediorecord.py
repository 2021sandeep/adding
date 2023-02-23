import time
from uiautomator import device as d

# Start the Camera app
d.start_activity(action='android.media.action.VIDEO_CAMERA')

# Wait for the record button to appear
d(resourceId='com.android.camera:id/v6_shutter_button_video').wait.exists()

# Start recording
d(resourceId='com.android.camera:id/v6_shutter_button_video').click()

# Wait for 2 minutes
time.sleep(120)

# Stop recording
d(resourceId='com.android.camera:id/v6_shutter_button_video').click()

# Save the recording
d(resourceId='com.android.camera:id/v6_btn_done').click()
