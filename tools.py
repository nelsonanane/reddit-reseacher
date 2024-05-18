import praw
import time
import os
from langchain.tools import tool
from dotenv import load_dotenv
from selenium import webdriver
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Tools:
    @tool("Scrape reddit content")
    def scrape_reddit(subreddit_name):
        """Useful to scrape Reddit content"""

        max_comments_per_post = 7

        print(f"Scraping {subreddit_name}")
        reddit = praw.Reddit(
            client_id=os.environ.get("REDIT_CLIENT_ID"),
            client_secret=os.environ.get("REDIT_CLIENT_SECRET"),
            user_agent=os.environ.get("REDIT_USER_AGENTS"),
        )
        subreddit = reddit.subreddit(subreddit_name)
        scraped_data = []

        for post in subreddit.hot(limit=12):
            post_data = {"title": post.title, "url": post.url, "comments": []}

            try:
                post.comments.replace_more(limit=0)  # Load top-level comments only
                comments = post.comments.list()
                if max_comments_per_post is not None:
                    comments = comments[:7]

                for comment in comments:
                    post_data["comments"].append(comment.body)

                scraped_data.append(post_data)

            except praw.exceptions.APIException as e:
                print(f"API Exception: {e}")
                time.sleep(60)  # Sleep for 1 minute before retrying

        return scraped_data

    @tool("Scrape website")
    def scrape_website(url):
        """Useful to scrape a website's content"""

        driver = webdriver.Chrome()
        driver.get(url)
        png_data = driver.get_screenshot_as_base64()
        
        print("png data: ", png_data)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "Return a JSON structure based on the based on the requirements of the user",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Create a JSON structure for all the items in the photo. Return only the JSON structure",
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,${png_data}",
                            },
                        },
                    ],
                },
            ],
        )

        print("response", response)
        driver.quit()
        return response
