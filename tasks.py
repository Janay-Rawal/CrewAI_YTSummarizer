from crew_ai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

#Research Task
research_task = Task(
    desrciption = (
        "Identify the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_outputs = 'A comprehensive 3 paragraph long report based on the {topic} of the video content.',
    tools = [yt_tool],
    agent = blog_researcher
)

#Writing task
writing_task = Task(
    description = (
        "Get the info from the youtube channel on the topic {topic}."
    ),
    expected_outputs = "Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog",
    tools = [yt_tool],
    agent = blog_writer,
    async_execution = False,
    output_file = "new-blog-post.md"
)
