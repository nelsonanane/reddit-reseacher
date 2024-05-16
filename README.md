## Reddit Trend Analysis with CrewAI

This repository contains a Python project using CrewAI to analyze trends and sentiment from Reddit subreddits. It leverages LangChain for tool integration, OpenAI's GPT-3.5-turbo for language processing, and the PRAW library for Reddit data scraping.

**Project Structure:**

- **agents.py:** Defines CrewAI Agents for research, technical writing, and criticism.
- **api.py:** Handles Slack integration to receive subreddit names and send results back.
- **crews.py:** Defines the ResearchCrew class to orchestrate the agents and tasks.
- **tasks.py:** Defines tasks for research, writing, and criticism with specific instructions and expected outputs.
- **tools.py:** Implements the "scrape_reddit" tool to fetch Reddit post data using PRAW.

**Usage:**

1. **Prerequisites:**
    - Install Python 3.8+
    - Create a virtual environment and install the required packages:
      ```bash
      pip install -r requirements.txt
      ```
    - Obtain API keys:
        - **OpenAI API Key:** Sign up for an OpenAI account ([https://platform.openai.com/](https://platform.openai.com/)) and get your API key.
        - **Reddit API Credentials:** Create a Reddit app ([https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)) and obtain the `client_id`, `client_secret`, and `user_agent`.
    - Set environment variables
      ```
      OPENAI_API_KEY=your_openai_api_key
      REDIT_CLIENT_ID=your_reddit_client_id
      REDIT_CLIENT_SECRET=your_reddit_client_secret
      REDIT_USER_AGENTS=your_reddit_user_agent
      SLACK_BOT_TOKEN=your_slack_bot_token
      SLACK_SIGNING_SECRET=your_slack_signing_secret
      ```
2. **Run the API server:**
    ```bash
    python api.py
    ```
3. **Interact with the Slack bot:**
    - Send a message to your Slack channel with the name of the subreddit you want to analyze (e.g., `r/MachineLearning`).
    - The bot will fetch data from the subreddit, run the analysis, and send back a detailed report and blog post.

**Features:**

- **Trend Analysis:** Identifies the latest and most exciting trends within a subreddit.
- **Sentiment Analysis:** Captures the overall sentiment and opinions expressed in the subreddit.
- **Technical Writing:** Generates a concise, engaging, and technical blog post summarizing the findings.
- **Critical Feedback:** Provides feedback and revisions to the generated blog post to ensure its quality and coherence.
- **Slack Integration:** Enables seamless interaction through a Slack bot.

**Further Development:**

- **Expand to Other Social Media Platforms:** Integrate with Twitter, Facebook, or Instagram APIs.
- **Improve Data Analysis:** Implement sentiment analysis and topic modeling for deeper insights.
- **Enhance Blog Post Quality:** Experiment with different writing styles and add visual elements.
- **Extend Agent Capabilities:** Introduce more specialized agents to handle specific tasks like image analysis or code generation.

**Disclaimer:**

This project is for educational and demonstration purposes only. Use it responsibly and adhere to Reddit's API usage policies.
