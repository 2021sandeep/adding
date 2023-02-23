import subprocess

adb_shell = subprocess.Popen(['adb', 'shell'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = adb_shell.communicate()
print(output.decode())
#print(error.decode(), file=sys.stderr)
