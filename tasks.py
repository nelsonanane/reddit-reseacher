from crewai import Task

class CrewTasks:
    def research(self, agent, subreddit_name):
        return Task(
            description=f"""Use and summarize scraped data from subreddit {subreddit_name} to make a detailed report on the latest trends in the topic. Use ONLY scraped data from {subreddit_name} to generate the report. Your final answer MUST be a full analysis report, text only, ignore any code or anything that isn't text. The report has to have bullet points and with 5-10 exciting new trends and sentiments about the topic. """,
            agent=agent,
            expected_output=f"""
            ## Latest Trends Report for r/{subreddit_name}
            - Trend 1: [Description of trend 1 based on scraped data]
            - Trend 2: [Description of trend 2 based on scraped data]
            - Trend 3: [Description of trend 3 based on scraped data]
            - Trend 4: [Description of trend 4 based on scraped data]
            - Trend 5: [Description of trend 5 based on scraped data]
            - Sentiment 1: [Description of sentiment 1 based on scraped data]
            - Sentiment 2: [Description of sentiment 2 based on scraped data]
            - Sentiment 3: [Description of sentiment 3 based on scraped data]
            - Sentiment 4: [Description of sentiment 4 based on scraped data]
            - Sentiment 5: [Description of sentiment 5 based on scraped data]
            """
        )
    
    def write(self, agent, subreddit_name):
        return Task(
            description=f"""Write a blog article with text only and with a short but impactful headline and at least 10 paragraphs. Blog should summarize the report. Style and tone should be compelling and concise, fun, technical but also use layman words for the general public. Name specific new, exciting trends and sentiments discussed. Don't write "\*\*Paragraph \[number of the paragraph\]:\*\*", instead start the new paragraph in a new line. ONLY include information from {subreddit_name}. For your Outputs use the following markdown format: \`\`\` ## \[Title of post\] - Interesting facts - Own thoughts on how it connects to the overall theme of the newsletter """,
            agent=agent,
            expected_output=f"""
            ## [Catchy and Impactful Headline for the Blog Post]

            [Paragraph 1: Introduction to the topic and the latest trends and sentiments from r/{subreddit_name}]

            [Paragraph 2: Elaborate on Trend 1 and its significance, using layman words]

            [Paragraph 3: Discuss Trend 2 and provide interesting facts and insights]

            [Paragraph 4: Highlight Sentiment 1 and its impact on the topic]

            [Paragraph 5: Explore Trend 3 and its potential implications]

            [Paragraph 6: Delve into Sentiment 2 and its relevance to the overall theme]

            [Paragraph 7: Analyze Trend 4 and its connection to the topic]

            [Paragraph 8: Discuss Sentiment 3 and its influence on the subject matter]

            [Paragraph 9: Examine Trend 5 and its importance in the context of the topic]

            [Paragraph 10: Summarize the key points and provide a compelling conclusion]
            """
        )
    def critic(self, agent):
        return Task(
            description="""The Output MUST have the following markdown format: \`\`\` ## \[Title of post\] - Interesting facts - Own thoughts on how it connects to the overall theme of the newsletter \`\`\` Make sure that it does and if it doesn't, rewrite it accordingly. """,
            agent=agent,
               expected_output=f"""
            ## [Title of the Blog Post]
            - Interesting Fact 1: [Relevant and captivating fact from the blog post]
            - Interesting Fact 2: [Another engaging fact or statistic from the blog post]
            - Interesting Fact 3: [A third compelling fact or insight from the blog post]
            - Connection to the Overall Theme: [Explanation of how the blog post relates to the broader theme of the newsletter, highlighting the significance of the trends and sentiments discussed]
            """
        )