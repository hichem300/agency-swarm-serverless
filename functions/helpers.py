def get_threads_from_db(conversation_id):
    from main import db
    doc = db.collection(u'conversations').document(conversation_id).get()

    if doc.exists:
        return doc.to_dict()['threads']
    else:
        return {}


def save_threads_to_db(conversation_id, threads):
    from main import db
    db.collection(u'conversations').document(conversation_id).set({
        u'threads': threads
    })


def init_agency(conversation_id):
    from agency_swarm import Agency

    # import agents
    from RevenueCreators.SalesManagerCeo import SalesManagerCeo
    from RevenueCreators.ExpertDataAnalyst import ExpertDataAnalyst
    

    # initialize agents
    ceo = SalesManagerCeo()
    data_analyst = ExpertDataAnalyst()
 

    # initialize agency - don't forget threads_callbacks
    agency = Agency([
        ceo,
        [ceo, data_analyst]],
        shared_instructions='./RevenueCreators/agency_manifesto.md',
        threads_callbacks={
            "load": lambda: get_threads_from_db(conversation_id),
            "save": lambda threads: save_threads_to_db(conversation_id, threads),
        },
        async_mode='threading')

    return agency
