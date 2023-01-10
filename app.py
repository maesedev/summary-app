from hooks.getaudio import get_audio
from  flask import Flask, request

app= Flask(__name__)

@app.route("/api/v1/audio",methods=["POST"])
def createSummary():
    response = get_audio(request)
    
    status = {
        "response":response
        }

    return response



if __name__ == "__main__":
    app.run()