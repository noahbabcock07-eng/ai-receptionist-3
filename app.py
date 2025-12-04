from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather
from assistant import handle_input

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    gather = Gather(
    input="speech",
    action="/process",
    method="POST"
)
    gather.say(
    "Hi, thanks for calling Adrian's Barber Shop. What can I do for you today?",
   voice="Polly.Kendra",
    language="en-US"
)
    resp.append(gather)
    resp.redirect("/voice")
    return Response(str(resp), mimetype="text/xml")

@app.route("/gather", methods=["POST"])
def gather_handler():
    speech_result = request.form.get("SpeechResult")
    answer = handle_input(speech_result)
    resp = VoiceResponse()
    response.say(
    "Okay, what time works best for you?",
    voice="Polly.Kendra",
    language="en-US"
)
    resp.hangup()
    return Response(str(resp), mimetype="text/xml")

@app.route("/")
def home():
    return "AI receptionist 3 is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
