from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

tweet_prompt = PromptTemplate(
    template="Generate a tweet on {topic} based on twitter data.",
    input_variables=['topic']
)
linkedin_prompt = PromptTemplate(
    template="Generate a post on {topic} based on LinkedIn data.",
    input_variables=['topic']
)
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(tweet_prompt,model, parser),
    'linked': RunnableSequence(linkedin_prompt, model, parser)
})

result = parallel_chain.invoke({'topic': 'AI Agents in Space Technologies.'})

print(result['tweet'])
print('-' * 70)
print(result['linked'])