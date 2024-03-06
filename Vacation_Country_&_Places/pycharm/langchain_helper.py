from langchain_openai.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

# import os


llm = OpenAI(openai_api_key="***", temperature=0.7)
def must_visit_place(continent):
    

    llm = OpenAI(openai_api_key="***", temperature=0.6)
    prompt_template_name = PromptTemplate(input_variables=['continent'],
                                          template="I want to visit different countries in the {continent}. Suggest me only one must-visit country name."
                                          )
    country_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="Country")

    prompt_template_items = PromptTemplate(input_variables=['Country'],
                                           template="Suggest most popular places in {Country}.Return it as a comma separated string."
                                           )
    place_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="Places")

    chain = SequentialChain(
        chains=[country_chain, place_chain],
        input_variables=['continent'],
        output_variables=['Country','Places']

    )
    response=chain.invoke({"continent":continent})
    return response

if __name__ == "__main__":
    print(must_visit_place('Europe'))

