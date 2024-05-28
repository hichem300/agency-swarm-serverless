
before_names = dir()
from .tools import *
current_names = dir()
imported_tool_objects = [globals()[name] for name in current_names if name not in before_names and isinstance(globals()[name], type) and issubclass(globals()[name], BaseTool)]
imported_tool_objects = [tool for tool in imported_tool_objects if tool.__name__ != "BaseTool"]
from agency_swarm.agents import Agent


class ExpertDataAnalyst(Agent):
    def __init__(self):
        super().__init__(
            name="ExpertDataAnalyst",
            description="Analyzes sales-related data to identify trends, patterns, and actionable insights that guide the sales strategy. Collaborates with the SalesManagerCeo to ensure data-driven, tailored strategies for maximizing sales process efficacy.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=imported_tool_objects + [] 
        )