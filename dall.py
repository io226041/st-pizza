from openai import OpenAI
client = OpenAI(api_key='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')

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url