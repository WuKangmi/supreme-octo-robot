import speech_recognition as sr

# 创建一个recognizer对象
recognizer = sr.Recognizer()

# 使用麦克风录制音频
with sr.Microphone() as source:
    print("Please Speak...")
    audio = recognizer.listen(source)

try:
    print("Recognizing...")
    # 使用Google的Web API进行语音识别
    text = recognizer.recognize_google(audio, language='zh-CN')
    print("Result:", text)
except sr.UnknownValueError:
    print("Sorry, your speech is unrecognized。")
except sr.RequestError as e:
    print("Unable to connect the internet;{0}".format(e))
