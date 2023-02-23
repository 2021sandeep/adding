from uiautomator import device as d
import time

# Start the Recorder app
d.start_activity(action='android.media.action.RECORD_SOUND')

# Wait for the recording button to appear
d(resourceId='com.android.soundrecorder:id/recordButton').wait.exists()

# Start recording
d(resourceId='com.android.soundrecorder:id/recordButton').click()

# Wait for the desired recording time
time.sleep(10)

# Stop recording
d(resourceId='com.android.soundrecorder:id/stopButton').click()

# Save the recording
d(resourceId='com.android.soundrecorder:id/saveButton').click()
