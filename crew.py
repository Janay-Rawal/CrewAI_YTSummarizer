from crewai import Crew, Process
from agents import blog_writer,blog_researcher
from tasks import writing_task,research_task


crew = Crew(
    agents = [blog_researcher,blog_writer],
    tasks = [research_task,writing_task],
    process = Process.sequential,
    cache = True,
    memory = True,
    max_rpm = 100,
)

#start taks execution with enhanced feedback
result = crew.kickoff(inputs={"topic": "AI vs ML vs Data Science"})
print(result)