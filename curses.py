import random,time,curses
print("Hello")
map_height = 10  
map_width = 15   
player_health = 100
player_pos = [5, 7]  
key_found = False
weapon_damage = 5  
player_coins = 0
monster_pos = [random.randint(0, map_height-1), random.randint(0, map_width-1)]  
monster_health = random.randint(25, 50)
monster_damage = random.randint(1, 5)
monster_coins = random.randint(1, 5)

def generate_weapon_damage(previous_damage):
    return random.randint(previous_damage - 2, previous_damage + 8)
def init_grid():
    grid = [['U' for _ in range(map_width)] for _ in range(map_height)]
    grid[player_pos[0]][player_pos[1]] = 'O'  
    grid[5][14] = 'L'     
    key_pos = [random.randint(0, map_height-1), random.randint(0, map_width-1)]
    weapon_pos = [random.randint(0, map_height-1), random.randint(0, map_width-1)]
    coin_pos = [[random.randint(0, map_height-1), random.randint(0, map_width-1)] for _ in range(3)]
   
    grid[key_pos[0]][key_pos[1]] = 'K'
    grid[weapon_pos[0]][weapon_pos[1]] = 'W'
    for pos in coin_pos:
        grid[pos[0]][pos[1]] = 'C'
   
    return grid

def move_player(grid, direction):
    global player_pos
    old_pos = player_pos[:]  
    new_pos = player_pos[:]
   
    if direction == 'up' and player_pos[0] > 0:
        new_pos[0] -= 1
    elif direction == 'down' and player_pos[0] < map_height - 1:
        new_pos[0] += 1
    elif direction == 'left' and player_pos[1] > 0:
        new_pos[1] -= 1
    elif direction == 'right' and player_pos[1] < map_width - 1:
        new_pos[1] += 1
   
    if grid[new_pos[0]][new_pos[1]] != 'L' or key_found:
        grid[old_pos[0]][old_pos[1]] = 'X'
        player_pos = new_pos

def move_monster():
    global monster_pos
    if monster_pos[0] < player_pos[0]:
        monster_pos[0] += 1
    elif monster_pos[0] > player_pos[0]:
        monster_pos[0] -= 1
    if monster_pos[1] < player_pos[1]:
        monster_pos[1] += 1
    elif monster_pos[1] > player_pos[1]:
        monster_pos[1] -= 1

def player_attack(stdscr):
    global monster_health
    if abs(player_pos[0] - monster_pos[0]) <= 1 and abs(player_pos[1] - monster_pos[1]) <= 1:
        monster_health -= weapon_damage
        stdscr.addstr(map_height + 2, 0, f"Player attacks! Monster health: {monster_health}")
        stdscr.refresh()
        time.sleep(0.5)
        if monster_health <= 0:
            stdscr.addstr(map_height + 2, 0, "You defeated the monster!")
            stdscr.refresh()
            time.sleep(0.5)
            monster_pos[:] = [-1, -1]  
def monster_attack(stdscr):
    global player_health
    if abs(player_pos[0] - monster_pos[0]) <= 1 and abs(player_pos[1] - monster_pos[1]) <= 1:
        player_health -= monster_damage
        stdscr.addstr(map_height + 2, 0, f"Monster attacks! Player health: {player_health}")
        stdscr.refresh()
        time.sleep(0.5)
        if player_health <= 0:
            stdscr.addstr(map_height + 2, 0, "You were defeated by the monster!")
            stdscr.refresh()
            time.sleep(1)
            quit() 
def show_grid(grid, stdscr):
    stdscr.clear()
    visible_radius = 1  
    for i in range(map_height):
        for j in range(map_width):
            if abs(i - player_pos[0]) <= visible_radius and abs(j - player_pos[1]) <= visible_radius:
                if grid[i][j] == 'U':  
                    grid[i][j] = 'X'  
            if [i, j] == player_pos:
                stdscr.addch(i, j, 'O')  
            elif [i, j] == monster_pos:
                stdscr.addch(i, j, 'M')  
            elif grid[i][j] in ['K', 'W', 'C', 'L', 'D']:
                stdscr.addch(i, j, grid[i][j])  
            else:
                stdscr.addch(i, j, grid[i][j])
    stdscr.refresh()
def main(stdscr):
    global key_found, weapon_damage, player_health, player_coins, monster_health    
    grid = init_grid()    
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(200)    
    while True:
        show_grid(grid, stdscr)        
        stdscr.addstr(map_height + 1, 0, f"Health: {player_health}, Coins: {player_coins}, Weapon Damage: {weapon_damage}, Monster Health: {monster_health}")        
        key = stdscr.getch()
        if key == curses.KEY_UP:
            move_player(grid, 'up')
        elif key == curses.KEY_DOWN:
            move_player(grid, 'down')
        elif key == curses.KEY_LEFT:
            move_player(grid, 'left')
        elif key == curses.KEY_RIGHT:
            move_player(grid, 'right')
        elif key == ord(' '):  
            player_attack(stdscr)        
        current_tile = grid[player_pos[0]][player_pos[1]]
        if current_tile == 'K':
            key_found = True
            stdscr.addstr(map_height + 2, 0, "You found the key!")
            grid[player_pos[0]][player_pos[1]] = 'O'
            grid[5][14] = 'D'  
            stdscr.refresh()
            time.sleep(0.5)
        elif current_tile == 'W':
            new_weapon_damage = generate_weapon_damage(weapon_damage)
            weapon_damage = new_weapon_damage
            stdscr.addstr(map_height + 2, 0, f"New weapon found! Damage: {new_weapon_damage}")
            grid[player_pos[0]][player_pos[1]] = 'O'
            stdscr.refresh()
            time.sleep(0.5)
        elif current_tile == 'C':
            player_coins += random.randint(1, 5)
            grid[player_pos[0]][player_pos[1]] = 'O'        
        move_monster()
        monster_attack(stdscr)        
        if current_tile == 'D':
            stdscr.addstr(map_height + 2, 0, "You win!")
            stdscr.refresh()
            time.sleep(1)
            break
curses.wrapper(main)
