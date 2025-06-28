# This example demonstrates a pipeline that takes a block of technical or educational text and automatically generates two key outputs in parallel:

# A tweet-sized summary for quick sharing on social media.

# A list of keywords that can be used for SEO, tagging, or categorization.

# The results are then merged into a well-formatted content block suitable for blog posts, newsletters, or documentation. This setup helps automate content repurposing, making it easier for creators, marketers, or educators to generate high-quality promotional and metadata content instantly.

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

# Define models
openai_model = ChatOpenAI()
claude_model = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

# Prompt to extract keywords
keyword_prompt = PromptTemplate(
    template='Identify 10 important keywords or phrases from this text:\n\n{text}',
    input_variables=['text']
)

# Prompt to generate a tweet-style summary
tweet_prompt = PromptTemplate(
    template='Summarize the following text in a style suitable for a tweet (max 280 characters):\n\n{text}',
    input_variables=['text']
)

# Prompt to merge outputs into a single response
final_prompt = PromptTemplate(
    template='You are formatting content for a blog snippet.\nInclude the following:\n\nKeywords: {keywords}\n\nSummary: {summary}',
    input_variables=['keywords', 'summary']
)

parser = StrOutputParser()

# Run keyword and summary generation in parallel
parallel = RunnableParallel({
    'keywords': keyword_prompt | claude_model | parser,
    'summary': tweet_prompt | openai_model | parser
})

# Combine outputs
final_chain = final_prompt | openai_model | parser

# Compose the full chain
pipeline = parallel | final_chain

# Example input
text = """
Stochastic Gradient Descent (SGD) is a simple yet very efficient approach to fitting linear classifiers and regressors under convex loss functions such as (linear) Support Vector Machines and Logistic Regression. Even though SGD has been around in the machine learning community for a long time, it has received a considerable amount of attention just recently in the context of large-scale learning.

SGD has been successfully applied to large-scale and sparse machine learning problems often encountered in text classification and natural language processing. Given that the data is sparse, the classifiers in this module easily scale to problems with more than 
 training examples and more than 
 features.

Strictly speaking, SGD is merely an optimization technique and does not correspond to a specific family of machine learning models. It is only a way to train a model. Often, an instance of SGDClassifier or SGDRegressor will have an equivalent estimator in the scikit-learn API, potentially using a different optimization technique. For example, using SGDClassifier(loss='log_loss') results in logistic regression, i.e. a model equivalent to LogisticRegression which is fitted via SGD instead of being fitted by one of the other solvers in LogisticRegression. Similarly, SGDRegressor(loss='squared_error', penalty='l2') and Ridge solve the same optimization problem, via different means.

The advantages of Stochastic Gradient Descent are:

Efficiency.

Ease of implementation (lots of opportunities for code tuning).

The disadvantages of Stochastic Gradient Descent include:

SGD requires a number of hyperparameters such as the regularization parameter and the number of iterations.

SGD is sensitive to feature scaling.
"""

# Execute the chain
result = pipeline.invoke({'text': text})

# Print result
print(result)

# Visualize DAG
pipeline.get_graph().print_ascii()
