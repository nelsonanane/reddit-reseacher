import os
from flask import Flask, request, send_from_directory 
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from dotenv import load_dotenv  
from crews import ResearchCrew

load_dotenv()

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@app.event("message")
def handle_message(event, say):
    text = event.get('text', '')
   
    research_crew = ResearchCrew(text=text)
    result = research_crew.get_results()
    print("result===============", result) 
    say(f"Result: {result}")

@flask_app.route('/slack/events', methods=['POST'])
def slack_events(): 
    return handler.handle(request) 

if __name__ == "__main__":
    flask_app.run(port=3000)