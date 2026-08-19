# Multi-Agent-Orchestration-using-A2A
A privacy-aware multi-agent coordination platform where autonomous personal agents negotiate availability and preferences, a planning agent uses MCP tools to generate travel options, and participants approve a final itinerary before execution.

## Why this project?
Planning a trip usually means juggling between multiple websites, tools and spreadsheets. This project eliminates that headace and provide a hassel free trip planning experience. 

Before planning a trip with friends means discussing a plan on a call and noting down all the constraints each one have, solving them means pouring our precious time in a rabbit hole. 

Combining multiple agents that are speciallized in their task so they can handle provided task very efficiently. All agents are cordinated with A2A protocol with MCP-based tool integration (Travel agents are coordinated via Langgraph workflow only).

## How the workflow works
1. The coordinator agent will send a query to other friend's agent requesting the the schedule of them.
2. After accquiring the schedule, it is passed down to travel agent.
3. The weather agent uses weather api to get weather condition of destination.
4. The flight agent uses MCP backed AviationStack data.
5. The hotel agent used a remote Tavily MCP search/ Airbnb MCP tool.
6. The itineary agent creates a practical travel plan.
8. The final plan is approved by the coordinator.
7. The final response is send to everyone via email