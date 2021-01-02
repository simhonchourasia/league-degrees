# league-degrees
Streamlit application to connect to Riot API and calculate degrees of separation in League of Legends. 

## How to use: 
Download the files, making sure that you have the riotwatcher and streamlit libraries installed for Python. Then, get a Riot API key from https://developer.riotgames.com/ and create a text file named apikey.txt with your API key as the first line in the same directory as app.py. Finally, navigate to the directory containing app.py and apikey.txt in your terminal and type `streamlit run app.py`. 

## Limitations

Unfortunatley, the Riot API is rate limited for normal developers, so only 20 requests can be made per second. Therefore, trying to find connections over large numbers of games or for large degrees of separation may cause errors. 
