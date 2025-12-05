from get_input import fetch_input

rock, paper, scissor = 1,2,3
moves_dict = {k:v for k,v in zip(["A","B","C","X","Y","Z"], ["rock","paper","scissor"]*2)}
scores_dict = {k:v for k,v in zip(["rock","paper","scissor"], [1,2,3])}
lose_win_dict = {k:v for k,v in zip(["win","lose","draw"], [6,0,3])}
# print(moves_dict)

p_score,op_score = 0,0

all_moves = fetch_input(2022,2).splitlines()


def win_loss_draw(op_move:str,p_move:str):
    op_move = moves_dict[op_move]
    p_move = moves_dict[p_move]
    if op_move==p_move:
        return 'draw',lose_win_dict['draw'],scores_dict[p_move]
    
    elif op_move == 'rock' and p_move=='paper' or op_move == 'paper' and p_move=='scissor' or op_move == 'scissor' and p_move=='rock':
        return 'win',lose_win_dict['win'],scores_dict[p_move]
    else:
        return 'lose',lose_win_dict['lose'],scores_dict[p_move]

for moves in all_moves:
    op_move = moves[0]
    p_move = moves[-1]
    result,win_lose_score,move_score = win_loss_draw(op_move,p_move)
    op_score += (win_lose_score+move_score)

print(op_score)









