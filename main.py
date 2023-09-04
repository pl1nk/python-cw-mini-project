# write your code here
def padle_court_cost(court_type):
    if court_type == 'indoor':
        return 30
    elif court_type == 'outdoor':
        return 20

def rackets_cost(racket_brand):
    if racket_brand == 'bullpadle' :
        return 100
    elif racket_brand == 'nox':
        return 140
    elif racket_brand == 'siux':
        return 200
    
def padle_ball_cost(ball_boxes):
    if ball_boxes == 'box':
        return 2
    elif ball_boxes == 'two boxes':
        return 3.5
    elif ball_boxes == 'three boxes':
        return 5

def padle_game_cost():
    court_type = input('the cort type: ')
    racket_brand = input('racket brand: ')
    ball_boxes = input('number of ball boxes: ')

    total_cost = (padle_court_cost(court_type)) + (rackets_cost(racket_brand)) + (padle_ball_cost(ball_boxes))

    return total_cost

total_cost = padle_game_cost()
print(f"""


toatal is {total_cost}

""")




    


    