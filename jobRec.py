import openai
import os
import pandas as pd

# OpenAI API Key
openai.api_key = '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'

def jobSuggestion(user_prompt, cv, jobs_file, tokens=256):
    # The jobs available, taken from jobs.csv
    jobs = pd.read_json(jobs_file)

    # A gpt-3 model prompt that will search for jobs that match the user's prompt
    header = "This is a job search ranking service. It ranks the provided jobs based on their fit and gives reasoning:"

    prompt = f"""{header}
    User prompt: {user_prompt}
    User CV: {cv}
    {jobs.to_string()}
    Response:
    """

    # The response from the gpt-3 model
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens={tokens},
        top_p=1,
        frequency_penalty=1,
        presence_penalty=0.0,
        stop=["\n"]
    )
    # Print the completion:
    print(prompt)
    print(response['choices'][0]['text'])

if __name__ == '__main__':
    user_prompt_sample = "I am looking for a job as a software engineer. It should be around 100k a year. I want to work 60 min from home at most."
    cv_sample = "I have a masters in computer science, I have 10 years experience in python and 6 years experience in js"
    jobSuggestion(user_prompt=user_prompt_sample, cv=cv_sample, jobs_file='jobs.json', tokens=400)
