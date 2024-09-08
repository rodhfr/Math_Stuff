import math 

# this python function calculates the probability of team winning over another
# a math logit function convert a designated variable to an interval of [-1, 1]  
# f(x) = (1/1+exp**-cx) thus c being an arbitrary constant.
# the designated variable "x" is the score difference betweens teams (team_X - team_Y)
# returning the probability of team X winning over Team Y. μA = Pa>b - (1 - Pa>b)

def victory_probability(K, team_X, team_Y):
    diff_skill_logit = (1 / (1 + math.exp(-K*(abs(team_X - team_Y)))))
    return (diff_skill_logit - (1 - diff_skill_logit))


def main():
    # variables
    team_a_score = 1000
    team_b_score = 1050
    K = 0.022
    max_refresh_rate = 30

    # prob calculation
    victory_rate_team_A = victory_probability(K, team_a_score, team_b_score)
    victory_rate_team_B = victory_probability(K, team_b_score, team_a_score)

    # match result
    match_outcome = 1

    # updating the team A score. this is the Elo Ranking equation, math expr: r'(A) = r(A) + k(Sa - μa)
    team_a_score += (max_refresh_rate * (match_outcome - victory_rate_team_A))
    team_b_score += (max_refresh_rate * (match_outcome - victory_rate_team_B))

    # console output
    print(f"Score do time A: {team_a_score} \nScore do time B: {team_b_score}\n")
    print(f"Probabilidade do time A Ganhar: {victory_rate_team_A}")
    print(f"Probabilidade do time B Ganhar: {victory_rate_team_B}")
    print(f"Resultado da partida: {match_outcome}")
    print(f"Novo score time A: {team_a_score}")
    print(f"Novo score time B: {team_b_score}")

if __name__ == "__main__":
    main()


