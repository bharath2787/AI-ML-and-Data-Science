
# This pipeline automatically analyzes incoming customer support tickets to determine whether the issue is urgent or normal. Based on the urgency, it generates an appropriate response—either quick and reassuring for urgent issues or polite and informative for regular ones.

# It uses a conditional chain that first classifies the urgency using a language model and then branches the response generation logic accordingly. This kind of automation can significantly reduce response time and improve customer satisfaction.


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# Initialize OpenAI model
model = ChatOpenAI()
parser = StrOutputParser()

# Step 1: Define schema for classification
class TicketUrgency(BaseModel):
    urgency: Literal["urgent", "normal"] = Field(description="The urgency level of the support ticket")

urgency_parser = PydanticOutputParser(pydantic_object=TicketUrgency)

# Step 2: Classification prompt
urgency_prompt = PromptTemplate(
    template="Classify the urgency of the following customer support ticket as either 'urgent' or 'normal':\n\n{ticket}\n\n{format_instruction}",
    input_variables=["ticket"],
    partial_variables={"format_instruction": urgency_parser.get_format_instructions()}
)

# Step 3: Chain to classify ticket urgency
classifier_chain = urgency_prompt | model | urgency_parser

# Step 4: Two response templates
urgent_prompt = PromptTemplate(
    template="This ticket is urgent. Draft a quick and reassuring response:\n\n{ticket}",
    input_variables=["ticket"]
)

normal_prompt = PromptTemplate(
    template="This ticket is normal priority. Draft a polite and informative response:\n\n{ticket}",
    input_variables=["ticket"]
)

# Step 5: Conditional branch chain based on urgency
response_chain = RunnableBranch(
    (lambda x: x.urgency == "urgent", urgent_prompt | model | parser),
    (lambda x: x.urgency == "normal", normal_prompt | model | parser),
    RunnableLambda(lambda _: "Could not determine urgency.") #runnable lambda converts lambda func into runnable , runnable can then be used as chain
)

# Final composed chain
ticket_chain = classifier_chain | response_chain

# Run example
# sample_ticket = {
#     "ticket": "My server has been down for over an hour and we are losing customers. Please help ASAP!"
# }

sample_ticket = {
    "ticket": "Thanks for your help"
}

print(ticket_chain.invoke(sample_ticket))

ticket_chain.get_graph().print_ascii()

print(response_chain.branches)
