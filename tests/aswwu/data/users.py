_users = [
    ["3241243", "Armanda Woolston", "armanda.Woolston@wallawalla.edu", "armanda.Woolston"],
    ["1234543", "Holly Garza", "Holly.garza@wallawalla.edu", "Holly.garza"],
    ["2345679", "Raeann Castor", "raeann.Castor@wallawalla.edu", "raeann.Castor"],
    ["1238798", "Tammie Treacy", "tammie.treacy@wallawalla.edu", "tammie.treacy"],
    ["1292398", "Virgilio Mccraw", "Virgilio.mccraw@wallawalla.edu", "Virgilio.mccraw"],
    ["7924798", "Lashay Semien", "Lashay.Semien@wallawalla.edu", "Lashay.Semien"],
    ["2348792", "Delcie Lauer", "delcie.Lauer@wallawalla.edu", "delcie.Lauer"],
    ["8234758", "Melva Woullard", "Melva.woullard@wallawalla.edu", "Melva.woullard"],
    ["9234820", "Eugene Burnette", "Eugene.burnette@wallawalla.edu", "Eugene.burnette"],
]

USERS = [
    {
        "wwuid": user[0],
        "full_name": user[1],
        "email": user[2],
        "username":user[3],
    }
    for user in _users
]
