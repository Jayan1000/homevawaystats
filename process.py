import csv

data = []

# import csv as list of lists inside data
with open('fantasy-nfl-standings-1985.csv', newline='') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	line_count = 0
	for row in csv_reader:
		# print(row)
		if line_count != 0:
			data.append(row)
		line_count += 1

home_wins_total = 0
home_losses_total = 0

away_wins_total = 0
away_losses_total = 0

for row in data:
	# process initial data
	team_name = row[0]
	home_score = row[8].split(" - ")
	away_score = row[9].split(" - ")

	# assign wins and losses
	home_wins = home_score[0]
	home_losses = home_score[1]
	away_wins = away_score[0]
	away_losses = away_score[1]

	# update totals
	home_wins_total += int(home_wins)
	home_losses_total += int(home_losses)
	away_wins_total += int(away_wins)
	away_losses_total += int(away_losses)

print("Home wins percentage")
print(home_wins_total / (home_wins_total + home_losses_total))
print("Away wins percentage")
print(away_wins_total / (away_wins_total + away_losses_total))