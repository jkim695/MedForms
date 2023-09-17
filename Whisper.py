import whisper 
import sounddevice as sd
from scipy.io.wavfile import write
import openai

openai.api_key = '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'


fs = 44100  # Sample rate
seconds = 45  # Duration of recording
message_history = [] #history for message

print("start recording")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 

model = whisper.load_model("medium")
result = model.transcribe("output.wav")

text = result["text"]

print(text)

q0 = "Provide answers with less than 4 words for the following questions"
q1 = "Give the name of the drug being prescribed in the text"
q2 = "Give the dosage of the drug being prescribed "
q3 = "Give the frequency of drug dosage per day being prescribed"
q4 = "Give the date of beginning date in numbers"
q5 = "Give the date of the end date in numbers"


def chat(inp, role="user"):
    message_history.append({"role": role, "content": inp})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
    )

    reply_content = completion.choices[0].message.content
    ##print(reply_content)
    message_history.append({"role": "assistant", "content": reply_content})
    return reply_content

def short():
    q0 = "provide the least amount of words from this point"
    chat(q0)

def sort(inp):
    short()
    global a1
    global a2
    global a3
    global a4
    global a5

    a1 = chat(q1+inp)
    a2 = chat(q2+inp)
    a3 = chat(q3+inp)
    a4 = chat(q4+inp)
    a5 = chat(q5+inp)

    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)


user_input = text
sort(user_input)