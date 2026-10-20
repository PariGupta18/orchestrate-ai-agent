# Agent Architecture & Engineering Iterations Log

## 1. System Overview
- **Framework**: LangGraph / Python Architecture
- **State Schema**: Pydantic validated `AgentState` (Query, Tool Decision, Output, Reasoning)
- **Execution Pattern**: Router-based Tool Delegation with Fallbacks

## 2. Tools & Capabilities
- `Math_Calculator`: Evaluates mathematical expressions safely.
- `Direct_Knowledge_Engine`: Handles general conversational and reasoning prompts without external tools.

## 3. Engineering Iterations & AI Usage
- **Iteration 1**: Initial script setup with Pydantic state management.
- **Iteration 2**: Integrated UI with Streamlit for live debugging and execution state visualization.
- **Iteration 3**: Implemented tool-calling router logic to prevent unneeded external executions and avoid infinite loops.

## 4. Edge Cases & Safeguards
- **Malformed Input**: Handled with fallback routing to prevent code termination.
- **Safety**: Safe expression evaluations isolated from arbitrary code execution.
-