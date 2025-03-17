from bs4 import BeautifulSoup
import pandas as pd

# Load HTML
with open("sofascore_pingpong.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
matches = []

# Find all match elements
match_elements = soup.select("a[class*='sc-3f813a14-0 eRKEkG']")  # Match container class

for match in match_elements:
    try:
        # Check for Czech Liga Pro (look for it in previous elements)
        league_check = match.find_previous("bdi", string="Czech Liga Pro")
        if not league_check:
            continue  # Skip non-Czech Liga Pro matches

        # Extract players
        player1_elem = match.select_one("div[data-testid='left_team'] bdi")
        player2_elem = match.select_one("div[data-testid='right_team'] bdi")
        player1 = player1_elem.text.strip() if player1_elem else "N/A"
        player2 = player2_elem.text.strip() if player2_elem else "N/A"

        # Extract final scores
        left_score_elem = match.select_one("div[data-testid='left_score'] span.currentScore")
        right_score_elem = match.select_one("div[data-testid='right_score'] span.currentScore")
        left_score = left_score_elem.text.strip() if left_score_elem else "0"
        right_score = right_score_elem.text.strip() if right_score_elem else "0"
        final_result = f"{left_score}-{right_score}"

        # Set results (placeholder - not in this HTML, needs match page)
        set_results = ["N/A"] * 5  # We’ll extend this later if needed

        # Store match data
        matches.append({
            "Player 1": player1,
            "Player 2": player2,
            "Final result": final_result,
            "Set 1 result": set_results[0],
            "Set 2 result": set_results[1],
            "Set 3 result": set_results[2],
            "Set 4 result": set_results[3],
            "Set 5 result": set_results[4]
        })
    except Exception as e:
        print(f"Error parsing match: {e}")
        continue

# Save to Excel
if matches:
    df = pd.DataFrame(matches)
    df.to_excel("ping_pong_matches.xlsx", index=False)
    print(f"Saved {len(matches)} matches to ping_pong_matches.xlsx")
else:
    print("No Czech Liga Pro matches found.")

# Print sample for verification
for match in matches[:2]:
    print(match)