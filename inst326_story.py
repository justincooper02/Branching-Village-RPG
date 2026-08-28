scenario_branches = {
    "start": {
        "Scenario Description": "Your town is messed up from war, famine and disease, what do you do?",
        "choices": {
            "A": {"text": "Gather a raiding party and pillage the nearby town for resources", "next": "raid"},
            "B": {"text": "Negotiate with the nearby town", "next": "negotiate"} 
            #For negotiate, jump to line ...
        }
    },
    "raid": {
        "Scenario Description": "You've successfully occupied the town, will you integrate them into your raiding party or execute leaders to lessen the chance of uprising?",
        "choices": {
            "A": {"text": "Raiding party", "next": "expansion"},
            "B": {"text": "Execute leaders", "next": "retaliation"} 
            #For retaliation, jump to line ...
        }
    },
    "expansion": {
        "Scenario Description": "Having built up your forces, you decide to expand your influence further. Will you ambush a nearby village or consolidate your power?",
        "choices": {
            "A": {"text": "Ambush the nearby village", "next": "cat_death"},
            "B": {"text": "Consolidate your power", "next": "coward"} 
        }
    },
    "cat_death": {
        "Scenario Description": "You ambush the village, sustaining heavy casualties. Your pet cat, Ronald, gets active and perishes in the melee. You have successfully occupied the region.",
        "choices": None,
        "next": "victory"
    },
    "coward": {
        "Scenario Description": "This is an RPG, don't be reasonable. Should've chosen war, coward.",
        "choices": None,
        "next": "death"
    },
    "retaliation": {
        "Scenario Description": "The occupied village population is in uproar. They plan to hire mercenaries to seek revenge. Do you seek the help of another neighboring village to quell the rebellion?",
        "choices": {
            "A": {"text": "Do not seek help", "next": "no_help"},
            "B": {"text": "Seek help", "next": "help"} 
            #For help, jump to line 48
        }
    },
    "no_help": {
        "Scenario Description": "You raid the village and are quickly overwhelmed. Should've gotten help, you're not that guy, pal.",
        "choices": None,
        "next": "death"
    },
    "help": {
        "Scenario Description": "Battle ensues, your forces are greatly outnumbered and are sustaining heavy losses. Suddenly, you hear the thunder of hooves as your allies arrive, turning the tide of the battle. You go on to occupy the rest of the region.",
        "choices": None,
        "next": "victory"
    },
    "negotiate": {
        "Scenario Description": "The nearby town agrees to trade with you, and requests assistance in building a well in exchange for food. What will you do?",
        "choices": {
            "A": {"text": "Accept the trade", "next": "labor_deficit"},
            "B": {"text": "Deny the trade", "next": "food_deficit"} 
            #For food_deficit, jump to line 78
        }
    },
        "labor_deficit": {
        "Scenario Description": "Over the next 2 years, your village prospers, but you lack a standing militia to defend yourself. Will you accept outsiders and nomads into your community?",
        "choices": {
            "A": {"text": "Take on outsiders", "next": "good_guy"},
            "B": {"text": "Do not take on outsiders", "next": "bad_guy"} 
        }
    },
        "good_guy": {
        "Scenario Description": "Over time, the outsiders assimilate into your community and restore your manpower. You are now the most powerful village in the region. Good job, I guess",
        "choices": None,
        "next": "victory"
    },
        "bad_guy": {
        "Scenario Description": "Though you prosper, you still lack the necessary manpower to defend your village. Your village succumbs to Raiders in the coming years. Your cat, Ronald, is the sole survivor.",
        "choices": None,
        "next": "death"
    },
        "food_deficit": {
        "Scenario Description": "You retain the necessary workforce and man power to defend your village. Your men grow weary, as food stores have gotten low. How will you address the food crisis?",
        "choices": {
            "A": {"text": "Claim dissidents are heretics", "next": "heresy"},
            "B": {"text": "Return to negotiate with the nearby village", "next": "labor_deficit"} 
            #For labor_deficit, jump to line 61
        }
    },
        "heresy": {
        "Scenario Description": "You declare the dissidents as heretics. For some reason, unbeknownst to you the majority of your town had converted to atheism. They label you a traitor and cast you out. What will you do?",
        "choices": {
            "A": {"text": "Wage war on your village", "next": "death"},
            "B": {"text": "Apologize", "next": "peasant"} 
            #For peasant, jump to line 94
        }
    },
        "peasant": {
        "Scenario Description": "They demote you to resident serf. You starve to death, your cat, Ronald, is elected village chieftain.",
        "choices": None,
        "next": "death"
    },
        "victory": {
        "Scenario Description": "Your village prospers, you are remembered as a hero for years to come.",
        "choices": None,
        "end": "victory"
    },
        "death": {
        "Scenario Description": "You are the worst thing to happen to this village. You are remembered as an imbecile.",
        "choices": None,
        "end": "death"
    },       
        
}
