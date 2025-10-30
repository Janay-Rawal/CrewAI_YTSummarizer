from crewai import Agent, LLM
from tools import yt_tool

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
llm = LLM(model = "llama-3.1-8b-instant")

#Creating content researcher agent
blog_researcher = Agent(
    role = "Blog Researcher",
    goal = "Get the relevant video content for the topic{topic} from YT channel",
    verbose = True,
    memory = True,
    backstory ="This person is expert in understanding videos in AI, data science, machine learning, and providing suggestions.",
    tools = [yt_tool],
    allow_delegation = True,
    llm = llm
)

#Creating blog writer agent with YT tool
blog_writer = Agent(
    role = "Blog Writer",
    goal = "Narrate compelling tech stories about the video {topic} for the YT channel",
    verbose = True,
    memory = True,
    backstory = (
    "This individual is a seasoned tech blogger with a flair for transforming complex AI and data science topics "
    "into engaging and digestible narratives. With years of experience writing for popular developer blogs and tech media, "
    "they specialize in capturing the essence of technical videos and turning them into insightful blog posts that spark curiosity, "
    "drive traffic, and educate readers. Their writing balances technical depth with creative storytelling to make each post memorable and impactful."
    ),
    tools = [yt_tool],
    allow_delegation = False
)

