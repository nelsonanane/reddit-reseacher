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

class ResearchCrew:
    def __init__(self, text: str):
        self.text = text
        self.crew = None
        self.llm = llm
        print("text from crew", text)

        agents = CrewAgents()
        tasks = CrewTasks()

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