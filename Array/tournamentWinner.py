# O(n) time, where n is the number of competitions
# O(k) space, where k is the number of teams 
#       (we're only saving the teams and their points in the hashTable)

HOME_TEAM_WON = 1

def tournamentWinner(competitors, results):

    currentBestTeam = " "
    outcome = dict({currentBestTeam: 0})

    for index, values in enumerate(competitors):
        result = results[index]
        homeTeam, awayTeam = values  # DECOMPOSE string to get each individule team

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        updateScores(winningTeam, 3, outcome)
        
        if outcome[winningTeam] > outcome[currentBestTeam]:
            currentBestTeam = winningTeam
            
    return currentBestTeam

def updateScores(team, points, outcome):
    if team not in outcome:
        outcome[team] = 0
    
    outcome[team] += points

#Python is the winner 
comp = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0,0,1]

print(tournamentWinner(comp, results))

