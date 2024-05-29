import os
from openai import OpenAI

tf_file = os.environ.get('tf_file')
print(tf_file)

with open(tf_file) as f:
    code_to_scan =  f.read()

print(code_to_scan)
    
# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
  messages=[
    {"role": "system", "content": "You are a helpful AI assistant used for code reviews in a CI/CD pipeline. You will be given terraform resource definitions. Please suggest recommendations to fix any misconfigurations or security concerns. Provide re-written terraform code with your suggestions."},
    {"role": "user", "content": code_to_scan}
  ],
  temperature=0.0,
)


print(completion.choices[0].message)
