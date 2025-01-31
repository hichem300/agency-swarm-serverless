
before_names = dir()
from .tools import *
current_names = dir()
imported_tool_objects = [globals()[name] for name in current_names if name not in before_names and isinstance(globals()[name], type) and issubclass(globals()[name], BaseTool)]
imported_tool_objects = [tool for tool in imported_tool_objects if tool.__name__ != "BaseTool"]
from agency_swarm.agents import Agent


class SalesManagerCeo(Agent):
    def __init__(self):
        super().__init__(
            name="SalesManagerCeo",
            description="Oversees the strategic sales direction for the RevenueCreators agency, integrating analytical insights to guide the sales strategy. Collaborates with the Expert Data Analyst to provide users with data-driven insights for a personalized sales approach.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=imported_tool_objects + [] 
        )
