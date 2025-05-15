from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt


load_dotenv()
model = ChatOpenAI()
st.header("Research Tool")

# user_input = st.text_input("Enter your prompt")

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformer", "GPT-3: Language Models are Few-Shor Learners", "Diffusion Models Beats GANs on Image Synthesis"])
style_input = st.selectbox("Select Explaination Style", ["Beginner Friendly", "Technical", "Code-Oriented", "Mathematical"])
# length_input = st.selectbox("Select Explaination Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraph)", "Long (detailed explaination)"])
# Length selection with slider instead of dropdown

length_options = ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
length_idx = st.select_slider(
    "📏 Select Explanation Length",
    options=range(len(length_options)),
    format_func=lambda x: length_options[x]
)
length_input = length_options[length_idx]

template = load_prompt("5.Prompts/template.json")



# prompt = template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input
# })

# if st.button("Summarize"):
#     result = model.invoke(prompt)
#     st.write(result.content)

# Chaining can be used 
if st.button("Summerize"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    }) 
    st.write(result.content) 
    
# Footer information
st.markdown("---")
st.caption("This tool uses AI to summarize research papers. Results may vary in accuracy and completeness.")

