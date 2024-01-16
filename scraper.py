import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://basketball.realgm.com/nba/teams/Golden-State-Warriors/9/Regular-Season-History'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('table', class_='basketball compact')

seasons = []
wl_ratios = []

for row in table.find_all('tr')[1:]:  # Skipping the header row
    cells = row.find_all('td')
    if len(cells) > 2:  # Ensuring there are enough cells
        season = cells[0].text.strip()
        wins = cells[1].text.strip()
        losses = cells[2].text.strip()

        try:
            wins = int(wins)
            losses = int(losses)
        except ValueError:
            continue  # Skip rows where conversion fails

        if losses != 0:
            wl_ratio = wins / losses
        else:
            wl_ratio = float('inf')  # Assigning infinity if losses are zero

        seasons.append(season)
        wl_ratios.append(wl_ratio)
nth_label = 5  # Change this value to show more or fewer labels
plt.figure(figsize=(10, 6))
plt.plot(seasons, wl_ratios, marker='o')

# Set xticks
plt.xticks([seasons[i] if i % nth_label == 0 else '' for i in range(len(seasons))], rotation=45)

plt.xlabel('Season')
plt.ylabel('W:L Ratio')
plt.title('W:L Ratio Progression of Golden State Warriors')
plt.tight_layout()
plt.show()