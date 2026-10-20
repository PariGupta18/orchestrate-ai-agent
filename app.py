import streamlit as st
from pydantic import BaseModel, Field
import math

st.set_page_config(page_title="AI Agent Prototype", page_icon="🤖")
st.title("🤖 Orchestrate AI Agent")

# 1. State Definition (Judge rubrics value state design)
class AgentState(BaseModel):
    query: str
    selected_tool: str = "None"
    tool_output: str = ""
    reasoning: str = ""

# 2. Tool Definition (Simulated Agent Tool)
def math_calculator_tool(expression: str) -> str:
    try:
        # Simple safe evaluation for demo agentic tooling
        allowed_names = {"sqrt": math.sqrt, "pow": math.pow}
        result = eval(expression, {"__builtins__": None}, allowed_names)
        return f"Calculation Result: {result}"
    except Exception as e:
        return f"Tool Execution Error: {str(e)}"

# 3. Agent Execution Logic (Decision Router)
def execute_agent(prompt: str) -> AgentState:
    state = AgentState(query=prompt)
    
    # Agent reasoning node
    if any(op in prompt for op in ["+", "-", "*", "/", "sqrt", "pow"]):
        state.selected_tool = "Math_Calculator"
        state.reasoning = "Query contains mathematical operation; routing to math tool."
        
        # Clean query for math tool
        clean_expr = "".join([c for c in prompt if c in "0123456789+-*/.() "])
        state.tool_output = math_calculator_tool(clean_expr)
    else:
        state.selected_tool = "Direct_Knowledge_Engine"
        state.reasoning = "Query is conceptual; direct natural response formulated."
        state.tool_output = f"Processed knowledge request: '{prompt}' ready for LLM synthesis."
        
    return state

# 4. Streamlit UI
user_goal = st.text_input("Assign a task to the Agent:", "Calculate 45 * 12 + 150")

if st.button("Execute Agent Loop"):
    with st.spinner("Agent planning and calling tools..."):
        result_state = execute_agent(user_goal)
        
        st.subheader("Agent Execution Log")
        st.info(f"🧠 **Reasoning:** {result_state.reasoning}")
        st.warning(f"🔧 **Tool Selected:** `{result_state.selected_tool}`")
        st.success(f"📊 **Tool Result:** {result_state.tool_output}")
        
        with st.expander("Inspect Raw State (Pydantic Schema)"):
            st.json(result_state.model_dump())