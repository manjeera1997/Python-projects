import pandas as pd
wikipedia = pd.read_html('https://en.wikipedia.org/wiki/2020_United_States_presidential_election')
election = wikipedia[4]
print(election)

candidate1 = election[1]
first_cand_name = candidate1[1]
first_cand_votes = candidate1[5]
first_can_popular = candidate1[7]
first_cand_party = candidate1[2]

candidate2 = election[2]
second_cand_name = candidate2[1]
second_cand_votes = candidate2[5]
second_can_popular = candidate2[7]
second_cand_party = candidate2[2]

if first_cand_votes > second_cand_votes:
    print(first_cand_name, "Is the winner from the ", first_cand_party, "Party with majority votes of ",first_cand_votes)
else:
    print(second_cand_name, "Is the winner from the ", second_cand_party, "Party with majority votes of ",second_cand_votes)
    
