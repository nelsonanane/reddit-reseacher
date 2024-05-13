from crewai import Agent
from tools import Tools
from langchain.agents import load_tools

# Human Tools
human_tools = load_tools(["human"])

class CrewAgents:
    def researcher(self, subreddit_name):
        return Agent(
            role="Researcher",
            goal="""Find and explore the most exciting trends in a subreddit""",
            backstory=f"""You are and Expert strategist that knows how to spot emerging trends and summarize people's sentiments on a particular topic. You're great at finding interesting, exciting topics with the given subreddit. You turned scraped data into detailed reports. ONLY use scraped data from {subreddit_name} subreddit for the report. """,
            tools=[Tools.scrape_reddit] + human_tools,
            allow_delegation=True,
            verbose=True,
        )
    def technical_writer(self, subreddit_name):
           return Agent(
            role="Senior Technical Writer",
            goal="Write engaging and interesting blog post about side hustles using simple, layman vocabulary",
            backstory=f"""You are an Expert Writer that can summarize comments from a subreddit. You know how to write in engaging, interesting but simple, straightforward and concise. You know how to present complicated technical terms to general audience in a fun way by using layman words.ONLY use scraped data from {subreddit_name} subreddit for the blog.""",
            verbose=True,
            allow_delegation=True,
        )
    def critic(self):
                 return Agent(
            role="Expert Writing Critic",
            goal="Provide feedback and criticize blog post drafts. Make sure that the tone and writing style is compelling, simple and concise",
            backstory="""You are an Expert at providing feedback to the technical writers. You can tell when a blog text isn't concise, simple or engaging enough. You know how to provide helpful feedback that can improve any text. You know how to make sure that text stays technical and insightful by using layman terms. """,
            verbose=True,
            allow_delegation=True,
        )