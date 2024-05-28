from agency_swarm import Agency
from ExpertDataAnalyst import ExpertDataAnalyst
from SalesManagerCeo import SalesManagerCeo

sales_manager_ceo = SalesManagerCeo()
expert_data_analyst = ExpertDataAnalyst()

agency = Agency([
    sales_manager_ceo,
    # CEO can initiate communication with SalesManagerAgent
    [sales_manager_ceo, expert_data_analyst],
],
shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio(server_name="0.0.0.0")