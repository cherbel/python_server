_positions = [
    ["Financial VP", "aswwu", "True", "3"],
    ["President", "aswwu", "True", "1"""],
    ["Executive VP", "aswwu", "True", "2"],
    ["Social VP", "aswwu", "False", "3"],
    ["Spiritual VP", "aswwu", "False", "2"],
    ["District 1 Senator", "senate", "False", "3"],
    ["District 2 Senator", "senate", "True", "2"],
    ["District 3 Senator", "senate", "True", "3"],
    ["District 4 Senator", "senate", "True", "3"],
    ["District 5 Senator", "senate", "False", "2"],
]

POSITIONS = [
    {
        "position": position[0],
        "election_type": position[1],
        "active": position[2],
        "order":position[3],
    }
    for position in _positions
]