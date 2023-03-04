import openai
import os
import pandas as pd

# OpenAI API Key
openai.api_key = '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'

# User prompt for what the user is seeking
user_prompt = "I am looking for a job as a software engineer. It should be around 100k a year. I want to work 60 min from home at most."
# The user's cv
cv = "I have a masters in computer science, I have 10 years experience in python and 6 years experience in js"
# The jobs available, taken from jobs.csv
jobs = pd.read_csv('jobs.csv')

# A gpt-3 model prompt that will search for jobs that match the user's prompt
prompt = f"""Take the following user prompt and explain which job is the best fit for the user and why.
User prompt: {user_prompt}
User CV: {cv}
Jobs available:
{jobs}
Response:
"""

# The response from the gpt-3 model
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.7,
    max_tokens=250,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.0,
    stop=["\n"]
)
# Print the completion:
print(prompt)
print(response['choices'][0]['text'])
