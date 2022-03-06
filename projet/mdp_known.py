import main
import numpy as np 


def reward(state, n_moves,strat): 
    """_summary_

    Args:
        state (_type_): _description_
        n_moves (_type_): _description_
        strat (_type_): _description_

    Returns:
        _type_: _description_
    """
    possibilities = possible_states(state)
    reward_list,actions = [],[]
    for e in possibilities : 
        reward_list.append(get_strat(e,strat))
    for key in possibilities.keys(): 
        actions.append(int(key))
    return reward_list,actions

def get_strat(state,strat):
    """_summary_

    Args:
        state (_type_): _description_
        strat (_type_): _description_
    """
    val = state[0][0]
    

def possible_states(state, colors, last_value):
    """_summary_

    Args:
        state (_type_): _description_
        colors (_type_): _description_
        last_value (_type_): _description_

    Returns:
        _type_: _description_
    """
    colors = [e for e in colors if e!= last_value]
    states = {}
    for e in colors : 
        state_bis = np.copy(state)
        main.MajCell(state_bis,e, last_value,0,0,len(state)) 
        states[str(e)] = state_bis
    return states

def generate_all_states(start,colors,n_moves,liste,max_moves): 
    """_summary_

    Args:
        start (_type_): _description_
        colors (_type_): _description_
        n_moves (_type_): _description_
        liste (_type_): _description_
        max_moves (_type_): _description_

    Returns:
        _type_: _description_
    """
    if main.AssertEnd(start) or n_moves == max_moves:
        return start
    else : 
        start_val = start[0][0]
        new_colors= [e for e in colors if e!= start_val]
        n_moves+=1
        for e in new_colors : 
            state_bis = np.copy(start)
            main.MajCell(state_bis,e, start_val,0,0,len(start))
            liste.append( generate_all_states(state_bis,colors,n_moves,liste,max_moves))
        return liste


width = 5
nbr_color = 4
grill = main.GenerateGrille(width,nbr_color)
max_moves = np.round((25*(2*width)*nbr_color)/((14+14)*6))
print(max_moves)
colors = [i for i in range(nbr_color)]
L = generate_all_states(grill,colors,0,[],max_moves)
print(len(L))

