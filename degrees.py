from riotwatcher import LolWatcher, ApiError

# Parameters
numGames = 2  # Number of games to look through
maxDegrees = 2 # Max degrees of separation
my_name = 'positron23'  # Replace with desired name
other_name = 'Jenric'  # Replace with desired name
intermediate = 'eggajane'

# Retrieve API key from apikey.txt
with open("apikey.txt", 'r') as f:
    api_key = f.readlines()[0].strip()
watcher = LolWatcher(api_key)
region = 'na1'


# Returns a list of account ids of the players that a certain person played with in the last n games
def getPlayedWith(name):
    player = watcher.summoner.by_name(region, name)
    matches = watcher.match.matchlist_by_account(region, player['accountId'])['matches'][:2]
    ret = []
    for match in matches:
        match_detail = watcher.match.by_id(region, match['gameId'])
        played_with = match_detail['participantIdentities']
        for p in played_with:
            ret.append(p['player']['summonerName'])
    return ret


def degreesOfSeparation(name1, name2, maxdeg):
    if name1 == name2:
        return 0
    if maxdeg == 0:
        return 999999 # Return very high number to signify that we did not find a link between the two players
    if name1 in getPlayedWith(name2):
        return 1
    return 1 + min([degreesOfSeparation(name1, p, maxdeg-1) for p in getPlayedWith(name2)])


# TESTING
#print(getPlayedWith(my_name))
#print(getPlayedWith(other_name))
#print(getPlayedWith(intermediate))
#print(degreesOfSeparation(my_name, intermediate, maxDegrees))
print(degreesOfSeparation(my_name, other_name, maxDegrees))
