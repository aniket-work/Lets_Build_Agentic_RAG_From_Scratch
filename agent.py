from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool


def setup_agent(retriever_tool, llm_model_name):
    llm_engine = Ollama(model=llm_model_name)

    prompt = PromptTemplate.from_template(
        """You are an AI assistant equipped with a range of tools designed to help answer human queries effectively. Follow the steps outlined below to provide accurate and thorough responses:

            1. Begin by analyzing the human’s question to determine the best tool or combination of tools needed to retrieve the necessary information.
            2. Clearly document each step of your reasoning process and tool usage.
            
            Use the following structured format:
            
            **Human:** <question>
            **Thought:** I need to use a tool to help me answer this question.
            **Action:** <tool_name>
            **Action Input:** <input_to_tool>
            **Observation:** <output_of_tool>
            **Thought:** I now have the information needed.
            **Human:** <answer>
            
            **Instructions:** Begin by addressing the human’s query systematically. First, retrieve relevant information, then analyze and respond comprehensively.
            
            **Human:** {input}
            **Thought:** Let's approach this step-by-step:
            1. Identify the necessary information for answering the question.
            2. Retrieve this information using the appropriate tools.
            3. Analyze the retrieved information to formulate a comprehensive answer.
            
            {agent_scratchpad}
            
            **Available tools:** {tool_names}

        """
    )

    tool = Tool(
        name="Retriever",
        func=retriever_tool,
        description="Use this tool to retrieve information from the vector database."
    )

    agent = create_react_agent(llm_engine, [tool], prompt)

    return AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=[tool],
        verbose=True,
        handle_parsing_errors=True
    )


def run_agentic_rag(agent_executor, question):
    enhanced_question = f"""Utilize the knowledge base accessible via the 'retriever' tool to provide a well-rounded and concise response to the question below. Focus exclusively on the question asked, ensuring that your answer is both relevant and complete.

**Instructions:**
- If initial retrieval attempts do not yield sufficient information, perform additional queries with varied search terms.
- Construct these queries in the affirmative form (e.g., instead of asking "How do I load a model from the Hub in bf16?", state "Load a model from the Hub with bf16 weights").
- Your goal is to thoroughly cover the topic by retrieving and synthesizing information from multiple retrievals if necessary.

**Question:**  
{question}
"""

    response = agent_executor.invoke({"input": enhanced_question})
    return response['output'] if 'output' in response else str(response)