from langchain_openai.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

# import os


llm = OpenAI(openai_api_key="***", temperature=0.7)
def generate_resturant_name_and_items(cuisine):
    #chain 1:resturant_name
    prompt_template_name = PromptTemplate(input_variables=['cuisine'],
                                          template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
                                          )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="resturant_name")

    prompt_template_items = PromptTemplate(input_variables=['resturant_name'],
                                           template="""Suggest some menu items for {resturant_name}.Return it as a comma separated string"""
                                           )
    food_item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")


    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=['cuisine'],
        output_variables=['resturant_name',"menu_items"]

    )
    response=chain.invoke({"cuisine":cuisine})
    return response

if __name__ == "__main__":
    print(generate_resturant_name_and_items('Italian'))

