Today's Goal
Transform the Gemini chatbot into BuySense AI, an AI shopping consultant that gives structured, helpful, and trustworthy shopping advice.

1. What is Prompt Engineering?
Prompt Engineering is the process of designing clear instructions that tell the AI how it should behave.
Think of it like giving instructions to a new employee.


Bad instruction:
Help customers.

Good instruction:
Help customers compare products, explain pros and cons, recommend the best value product, never invent specifications, and ask follow-up questions when information is missing.

The better the instructions, the better the AI's responses.


2. Why Do We Need a System Prompt?
Without a system prompt:                                  
User
↓
Gemini
↓
General AI
----------------------------------------------------
With a system prompt:
User
↓
System Prompt
↓
Gemini
↓
BuySense AI

The system prompt gives the AI its identity.


3. Why is Prompt Engineering Important?

Later our project will use:

Product database
Price comparison
Reviews
PDFs
RAG
AI Agents

The LLM must know how to use all of them.

Prompt engineering is the foundation.


🏗 Today's Architecture:

                 User

                  │
                  ▼

           User Question

                  │
                  ▼

          System Prompt

                  │
                  ▼

          Gemini 2.5 Flash

                  │
                  ▼

        Shopping Recommendation


Changes Done:
1.adding in chatbot.py

from prompts import SHOPPING_SYSTEM_PROMPT

This imports the shopping prompt from prompts.py so we can send it to Gemini along with the user's question.

2.Inside your while True: loop adding the code where the along with the user question the prompts(instructions) will also go to ai.

full_prompt = f"""
{SHOPPING_SYSTEM_PROMPT}

User Question:
{user_input}
"""


What Changed?
❌ Before
Gemini only received:

Suggest a laptop under ₹70,000.


✅ Now
Gemini receives:

You are BuySense AI.

Rules:
- Recommend products...
- Explain pros and cons...
- Never invent prices...
...

User Question:
Suggest a laptop under ₹70,000.

Now Gemini knows how it should behave before answering.

 