from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
) 

text = '''
As artificial intelligence continues to evolve, the dynamics between 
human decision-makers and intelligent systems are rapidly shifting. What began 
as simple automation has transformed into highly contextual AI agents capable of 
assisting with creative problem-solving, language generation, and even emotional 
analysis. This growing synergy isn't about AI replacing humans—it’s about enhancing 
human capabilities. By offloading repetitive and computationally intensive tasks, 
AI allows professionals to focus on higher-level thinking, strategy, and innovation.

However, this collaboration requires deliberate design. Trust, transparency, and 
explainability in AI systems are becoming critical. Developers must ensure these 
systems are interpretable and ethically aligned with human values. Moreover, upskilling 
the workforce to understand and effectively interact with AI is just as important as 
building the models themselves. The future won't belong to AI or humans alone, but to 
those who can work seamlessly at the intersection of both.
'''

result = splitter.split_text(text)
print(result)