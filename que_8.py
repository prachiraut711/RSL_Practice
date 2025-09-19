# 6.Provide multiple direction to robot from array and check robot is on same position or not at the end

def RobotMoves(moves):
    x = 0
    y = 0
    for move in moves:
        if move == "UP":
            y +=1
        elif move == "DOWN":
            y -= 1
        elif move == "LEFT":
            x -= 1
        elif move == "RIGHT":
            x += 1
        
    if x == 0 and y == 0:
        return True
    else:
        return False
        
moves1 = ["UP", "DOWN", "LEFT","RIGHT"]
moves2 = ["UP", "UP", "DOWN",  "RIGHT"]
print(RobotMoves(moves1))
print(RobotMoves(moves2))