import streamlit as st
from riotwatcher import LolWatcher, ApiError

st.write("""
# Degrees of Separation - League of Legends

Find out how many degrees of separation you have from another player. 

For example, if you played in the same game as your target player, you have 1 degree of separation. 

If you played in the same game as somebody who played in the same game as your target player, you have 2 degrees of separation. 

Unfortunately bottlenecked by Riot API rate limiting. """)


# Parameters
numGames = 2  # Number of games to look through
maxDegrees = 2 # Max degrees of separation
my_name = 'positron23'  # Replace with desired name
other_name = 'Jenric'  # Replace with desired name

# Retrieve API key from apikey.txt
with open("apikey.txt", 'r') as f:
    api_key = f.readlines()[0].strip()
watcher = LolWatcher(api_key)
region = 'na1'


# Returns a list of account ids of the players that a certain person played with in the last n games
def getPlayedWith(name, num_games):
    player = watcher.summoner.by_name(region, name)
    matches = watcher.match.matchlist_by_account(region, player['accountId'])['matches'][:num_games]
    ret = []
    for match in matches:
        match_detail = watcher.match.by_id(region, match['gameId'])
        played_with = match_detail['participantIdentities']
        for p in played_with:
            ret.append(p['player']['summonerName'])
    return ret


def degrees_of_separation(name1, name2, maxdeg, num_games):
    played_with_2 = getPlayedWith(name2, num_games)
    if name1 == name2:
        return 0
    if maxdeg == 0:
        return 999999999 # Return very high number to signify that we did not find a link between the two players
    if name1 in played_with_2:
        return 1
    return 1 + min([degrees_of_separation(name1, p, maxdeg-1) for p in played_with_2])


my_name = st.text_input("Input the first summoner name", 'positron23')
other_name = st.text_input("Input the second summoner name", 'averagedill')
max_deg = st.number_input("Input the maximum degrees of separation you wish to look for", 2)
num_games = st.number_input("Input the number of past games you wish to look at", 2)

st.subheader("If the value does not show below, you might need to wait, or your parameters may be causing too many requests to the Riot API")

ret = degrees_of_separation(my_name, other_name, max_deg, num_games)
if ret >= 999999999:
    st.header("We could not find a link with your given parameters")
else:
    st.header("Degrees of separation: " + str(ret))

