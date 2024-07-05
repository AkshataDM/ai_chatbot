import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

class CrewSearch:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        self._setup_environment()
        self.search_tool = DuckDuckGoSearchRun(backend="news")
        self.researcher = self._create_researcher_agent()
        self.research_task = self._create_research_task()
        self.crew = self._create_crew()

    def _setup_environment(self):
        os.environ["OPENAI_API_KEY"] = self.openai_api_key

    def _create_researcher_agent(self):
        return Agent(
            role="Senior Researcher",
            goal="Find one relevant article about technology.",
            backstory="An expert researcher with a keen eye for market trends in technology.",
            verbose=True,
            tools=[self.search_tool],
            allow_delegation=False,
        )

    def _create_research_task(self):
        return Task(
            description="Search for the latest news article on technology. "
                        "Provide the title and description to the most recent and relevant articles.",
            agent=self.researcher,
            expected_output="The latest news article with a title and a 10 word description.",
        )

    def _create_crew(self):
        return Crew(
            agents=[self.researcher],
            tasks=[self.research_task],
            process=Process.sequential,
        )

    def run_search(self, topic="technology"):
        # result = self.crew.kickoff(inputs={"topic": topic})
        result = self.crew.kickoff()
        return result

if __name__ == "__main__":
    openai_api_key = "sk-proj-hzQCI5uutQ08Rk3JmY0fT3BlbkFJDQ6zLRjdgqFJ8cWSIwIt"
    search_instance = CrewSearch(openai_api_key)
    result = search_instance.run_search()
    print(result)
