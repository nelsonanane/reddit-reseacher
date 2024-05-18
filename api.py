import os
from flask import Flask, request, send_from_directory 
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from dotenv import load_dotenv  
from crews import ResearchCrew, WebsiteScraperScrew
import re

load_dotenv()

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

# Check if the string is a valid URL
def is_url(string):
    # Regular expression pattern for website URLs
    url_pattern = re.compile(r'^(http|https)://|[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(/.*)?$|^[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(/.*)?$', re.IGNORECASE)
    
    # Check if the string matches the URL pattern
    if url_pattern.match(string):
        return True
    else:
        return False

@app.event("message")
def handle_message(event, say):
    text = event.get('text', '')
        
    if text.startswith('<') and text.endswith('>'):
        text = text[1:-1] 
    
    print("text", text)
    print('isurl', is_url(text))
    
    if is_url(text):
        scrape_crew = WebsiteScraperScrew(url=text)
        print("scrape_crew", scrape_crew.get_results())
        say(f"Results: {scrape_crew.get_results()}") 
    else:
        research_crew = ResearchCrew(text=text)
        result = research_crew.get_results()
        print("result===============", result) 
        say(f"Result: {result}")

@flask_app.route('/slack/events', methods=['POST'])
def slack_events(): 
    return handler.handle(request) 

if __name__ == "__main__":
    flask_app.run(port=3000)