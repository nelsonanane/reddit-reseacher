import os
from agents import CrewAgents
from tasks import CrewTasks 
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    openai_api_base="https://api.openai.com/v1",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-3.5-turbo"
)

agents = CrewAgents()
tasks = CrewTasks()
class ResearchCrew:
    def __init__(self, text: str):
        self.text = text
        self.crew = None
        self.llm = llm
        print("text from crew", text)

        research_agent = agents.researcher(subreddit_name=self.text)
        writer_agent = agents.technical_writer(subreddit_name=self.text)
        critic_agent = agents.critic()

        research_task = tasks.research(agent=research_agent, subreddit_name=self.text)
        writer_task = tasks.write(agent=writer_agent, subreddit_name=self.text)
        critic_task = tasks.critic(agent=critic_agent)

        self.crew = Crew(
            agents=[research_agent, writer_agent, critic_agent],
            tasks=[research_task, writer_task, critic_task],
            process=Process.sequential,
            manager_llm=self.llm
        )
        self.results = self.crew.kickoff()

    def get_results(self):
        return self.results
    
class WebsiteScraperScrew:
    def __init__(self, url: str):
        self.text = url
        self.crew = None
        self.llm = llm
        print("text from crew", url)
 
        #Agents
        scraper = agents.website_scraper(url=self.text)
        analyzer = agents.scraped_data_analyzer(url=self.text)
        reviewer = agents.scraped_data_reviewer(url=self.text)
        
        #Tasks
        scrape_site = tasks.scrape_website(agent=scraper, url=self.text)
        analyze = tasks.analyze_scrape_website(agent=analyzer, url=self.text)
        review = tasks.review_scrape_website(agent=reviewer)
        
        self.crew = Crew(
            agents=[scraper, analyzer, reviewer],
            tasks=[scrape_site, analyze, review],
            process=Process.sequential,
            manager_llm=self.llm
        )
        
        self.results = self.crew.kickoff() 
        
    def get_results(self):
        return self.results