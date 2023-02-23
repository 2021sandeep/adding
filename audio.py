import wave

obj=wave.open("C:/Users/sandeep/Downloads/file_example_WAV_1MG.wav","rb")
print("number of channels",obj.getnchannels())
print("sample width",obj.getsampwidth())
print(obj.getframerate())
print(obj.getnframes())
print(obj.getparams())

timee_audio=obj.getnframes()/obj.getframerate()
print(timee_audio)
###############################################
frames=obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames)/ 2)                    #obj.getnchannels=2
