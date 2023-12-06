import openai
from dotenv import load_dotenv
def request_gpt_turbo(messages):
    load_dotenv()
    client = openai.OpenAI()
    # prompt = "\n".join([message['content'] for message in messages])
    qry = messages[-1]['content']
    answer = client.completions.create(
                              model="gpt-3.5-turbo-instruct",
                              prompt = "Give a friendly answer to the query" + qry,
                              max_tokens = 200
                          )
    return answer.choices[0].text