from riotwatcher import LolWatcher, ApiError

# Retrieve API key from apikey.txt
with open("apikey.txt", 'r') as f:
    api_key = f.readlines()[0].strip()
watcher = LolWatcher(api_key)
region = 'na1'

# Show my player info and ranked history
player = watcher.summoner.by_name(region, 'positron23')
ranked = watcher.league.by_summoner(region, player['id'])
print(player)
print(ranked)

# Finds the most recent match and shows every player in that match
matches = watcher.match.matchlist_by_account(region, player['accountId'])
print(len(matches['matches']))
last_match = matches['matches'][2]
match_detail = watcher.match.by_id(region, last_match['gameId'])
print(match_detail)
participantIdentities = match_detail['participantIdentities'][5:]
playersBeat = [p['player']['summonerName'] for p in participantIdentities]
print(playersBeat)

# Shows all the attributes in match_detail
participants = []
row = match_detail['participants'][0]
for aspect in row:
    print(aspect)