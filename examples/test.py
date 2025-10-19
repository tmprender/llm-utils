import os
from openai import OpenAI

# ------------------------------------------------------------------
# Example Terraform code – replace this with any snippet you want to
# analyze. The script no longer reads from an external file.
# ------------------------------------------------------------------
terraform_code = """
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"
  acl    = "public-read"
}
"""

# ------------------------------------------------------------------
# Connect to a local Ollama instance.
# Ollama exposes an OpenAI‑compatible API at http://localhost:11434/v1
# ------------------------------------------------------------------
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Ollama does not require a real key; any string works.
)

# ------------------------------------------------------------------
# Ask the model to review the Terraform snippet.
# ------------------------------------------------------------------
completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful AI assistant used for code reviews in a CI/CD pipeline. "
                "You will be given Terraform resource definitions. "
                "Please suggest recommendations to fix any misconfigurations or security concerns. "
                "Provide rewritten Terraform code with your suggestions."
            ),
        },
        {"role": "user", "content": terraform_code},
    ],
    temperature=0.0,
)

# ------------------------------------------------------------------
# Print the model's recommendation.
# ------------------------------------------------------------------
print(completion.choices[0].message.content)