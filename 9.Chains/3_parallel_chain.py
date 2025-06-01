from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI(model='gpt-3.5-turbo')
model2 = ChatOpenAI(
    model='gpt-4o',
    max_completion_tokens=300
)

prompt1 = PromptTemplate(
    template="Generate a short, concise text notes for the following text  \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short hard level quiz for the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} & quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser  

chain = parallel_chain | merge_chain

text ='''
Why is Transfer Learning Important?
Transfer learning offers solutions to key challenges like:

Limited Data: Acquiring extensive labelled data is often challenging and costly. Transfer learning enables us to use pre-trained models, reducing the dependency on large datasets.
Enhanced Performance: Starting with a pre-trained model which has already learned from substantial data allows for faster and more accurate results on new tasks ideal for applications needing high accuracy and efficiency.
Time and Cost Efficiency: Transfer learning shortens training time and conserves resources by utilizing existing models hence eliminating the need for training from scratch.
Adaptability: Models trained on one task can be fine-tuned for related tasks making transfer learning versatile for various applications from image recognition to natural language processing.
How Does Transfer Learning Work?
Transfer learning involves a structured process to use existing knowledge from a pre-trained model for new tasks:

Pre-trained Model: Start with a model already trained on a large dataset for a specific task. This pre-trained model has learned general features and patterns that are relevant across related tasks.
Base Model: This pre-trained model, known as the base model, includes layers that have processed data to learn hierarchical representations, capturing low-level to complex features.
Transfer Layers: Identify layers within the base model that hold generic information applicable to both the original and new tasks. These layers often near the top of the network capture broad, reusable features.
Fine-tuning: Fine-tune these selected layers with data from the new task. This process helps retain the pre-trained knowledge while adjusting parameters to meet the specific requirements of the new task, improving accuracy and adaptability.
Low-level features learned for task A should be beneficial for learning of model for task B.
'''

result = chain.invoke({'text': text})

# print(result)

chain.get_graph().print_ascii()