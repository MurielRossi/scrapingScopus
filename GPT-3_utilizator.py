import openai

openai.api_key = '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'
response = openai.Completion.create(
    engine="davinci",
    prompt="Today I'm feeling very happy and",
    max_tokens=15,
    echo=True
)

openai.Answer.create(

)

print(response.choices[0].text)