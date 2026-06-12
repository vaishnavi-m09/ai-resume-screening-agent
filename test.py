from backend.agents.parser_agent import ParserAgent

agent = ParserAgent()

text = agent.parse(
    r"sample_data/resumes/test_resume.pdf"
)

print(text[:500])