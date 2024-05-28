from helpers import init_agency
from agency_swarm import set_openai_key

if __name__ == '__main__':
    set_openai_key("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")

    agency = init_agency("RevenueCreators")

    schema = agency.get_customgpt_schema("https://agency-6yuqkpcx3a-uc.a.run.app") # paste your url from terminal here

    # save to schema.json
    with open('schema.json', 'w') as outfile:
        outfile.write(schema)

    print("schema.json saved\n")

    print("Use these instructions to setup your agent in custom gpt:\n")

    print(agency.agents[0].instructions)