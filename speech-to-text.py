import speech_recognition
import pyttsx3
import wikipedia
from datetime import date
from datetime import datetime
#Thêm các thư viện cần thiết.

#Robot nghe và nhận dạng dọng nói của người dùng
#Đưa ra câu trả lời và phát bằng âm thanh audio
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.record(mic, duration=4)
        print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio,language="vi")
    except:
        you =""
    print("You  : "+you)
    #--Đây là bước nói
    #Nhận dạng dọng nói của bạn, máy tính sẽ hiểu và trả lời lại dựa trên từ hỏi trong câu của bạn
    if you =="":
        #Trường hợp không hiểu đầu vào người dùng, hệ thống sẽ thông báo tôi không thấy gì.
        robot_brain ="I can't hear you, try again"
    #Các trường hợp khác của người dùng
    elif "Hi" in you:
        robot_brain = "Hello Khoan Nguyen"
    elif "today" in you:
        #GET ngày tháng hiện tại
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        #Get thời gian hiện tại
        now = datetime.now()
        robot_brain = now.strftime("%H hours :%M minutues :%S seconds")
    elif "president" in you:
        robot_brain = "Donal Trump"
            
    elif "bye" in you:
        #Khi người dùng nói bye, máy tính hiểu được thì sẽ đưa ra lời chào, và kết thúc chương trình
        robot_brain = "GoodBye Khoan Nguyen"
        print("Robot: "+ robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
        
    elif you:
        wikipedia.set_lang("vi")
        robot_brain = wikipedia.summary(you,sentences=1)
        #Các kiến thức khác với kịch bản đã tạo sẵn ở trên, hệ thống sẽ lấy thông tin dựa trên 
        # nguồn Wikipeadia
        
        
    else: 
        
        robot_brain = "I'm fine thanks you and you"
    print("Robot: "+ robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    