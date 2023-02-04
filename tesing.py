import openai
import os
import pandas as pd

# OpenAI API Key
openai.api_key = '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'

# Generate a csv file with the data: Job Name, Job Description, Job Requirements, Job Pay, Job Location, Job Type, Job Company, Job Link
# The csv file should be in the same directory as this script
# The csv file should be named: jobs.csv

# Read the csv file using pandas
df = pd.read_csv('jobs.csv')

# Create a list of job descriptions etc
job_names = df['Job Name'].tolist()
job_descriptions = df['Job Description'].tolist()
job_requirements = df['Job Requirements'].tolist()
job_pays = df['Job Pay'].tolist()
job_locations = df['Job Location'].tolist()

# Take the 10 jobs and create a list of job descriptions into a gpt prompt
job_descriptions_prompt = ''
for i in range(10):
    job_descriptions_prompt += job_descriptions[i] + '

print(job_descriptions_prompt)