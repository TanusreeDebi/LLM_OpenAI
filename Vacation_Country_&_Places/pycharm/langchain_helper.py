from langchain_openai.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

# import os


llm = OpenAI(openai_api_key="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", temperature=0.7)
def must_visit_place(continent):
    #chain 1:resturant_name
    # prompt_template_name = PromptTemplate(input_variables=['cuisine'],
    #                                       template="I want to open a resturant for {cuisine} food. Suggest a fency name for this."
    #                                       )
    # name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="resturant_name")
    #
    # prompt_template_items = PromptTemplate(input_variables=['resturant_name'],
    #                                        template="""Suggest some menu items for {resturant_name}.Return it as a comma separated string"""
    #                                        )
    # food_item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
    llm = OpenAI(openai_api_key="***", temperature=0.6)
    prompt_template_name = PromptTemplate(input_variables=['continent'],
                                          template="I want to visit different countries in the {continent}. Suggest me only one must visit country name."
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

