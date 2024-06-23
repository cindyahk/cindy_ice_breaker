from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

def ice_break_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    summary_template = """
           given the information {information} about a person, I want you to create:
           1. a short summary
           2. two interesting facts about them
       """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm;

    res = chain.invoke(input={"information": linkedin_data})
    print(res)


if __name__ == "__main__":
    load_dotenv()
    print("Enter IceBreaker")
    ice_break_with(name="Eden Marco")
