from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather
from assistant import handle_input

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    gather = Gather(input="speech", timeout=3, action="/gather")
    gather.say("Hello, thanks for calling. How can I assist you today?")
    resp.append(gather)
    resp.redirect("/voice")
    return Response(str(resp), mimetype="text/xml")

@app.route("/gather", methods=["POST"])
def gather_handler():
    speech_result = request.form.get("SpeechResult")
    answer = handle_input(speech_result)
    resp = VoiceResponse()
    resp.say(answer)
    resp.hangup()
    return Response(str(resp), mimetype="text/xml")

@app.route("/")
def home():
    return "AI receptionist 3 is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
