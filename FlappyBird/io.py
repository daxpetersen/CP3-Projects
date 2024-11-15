import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (230, 230, 230)
PLAYER_COLOR = (0, 100, 255)
FOOD_COLOR = (255, 0, 0)
ENEMY_COLOR = (255, 165, 0)
FPS = 60

# Player settings
PLAYER_RADIUS = 20
PLAYER_SPEED = 5
UPGRADE_COST = 5

# Food settings
FOOD_RADIUS = 10

# Enemy settings
ENEMY_RADIUS = 15
ENEMY_SPEED = 2

# List of abilities
ABILITIES = [
    "Circle Shield", "Circle Dash", "Circular Barrage", "Circle Pulse",
    "Circular Spin", "Circle Beam", "Circular Trap", "Circle Burst",
    "Circular Clone", "Circle Nova", "Circular Grasp", "Circle Surge",
    "Circular Storm", "Circle Wall", "Circular Vortex", "Circle Infusion",
    "Circular Blade", "Circle Eruption", "Circular Heal", "Circle Teleport",
    "Circular Amplification", "Circle Crush", "Circular Stun", "Circle Slice",
    "Circular Repel", "Circle Flash", "Circular Distortion", "Circle Resurgence",
    "Circular Annihilation", "Circle Sweep", "Circular Dominance", "Circle Ascension"
]

# List of weapons
WEAPONS = [
    "Arcane Staff", "Thunder Hammer", "Venomous Crossbow", "Spectral Blade",
    "Inferno Gauntlets", "Frostbite Bow", "Shadow Dagger", "Soul Reaver Scythe",
    "Gravity Hammer", "Phoenix Staff", "Void Cannon", "Aether Whip",
    "Tempest Blade", "Plasma Rifle", "Crystal Bow", "Time Warp Staff",
    "Celestial Chakrams", "Magma Axe", "Bladestorm Saber", "Thunderclap Mace",
    "Venom Fang Dagger", "Frostbite Cannon", "Shadow Bow", "Soulfire Staff",
    "Gravity Sphere", "Phoenix Blade", "Void Scythe", "Aether Shield",
    "Tempest Gloves", "Plasma Whip", "Crystal Hammer", "Timekeeper's Hourglass",
    "Celestial Lance", "Magma Bow", "Bladestorm Axe", "Thunderclap Hammer",
    "Venomous Whip", "Frostbite Staff", "Shadow Blade", "Soulfire Cannon",
    "Gravity Blade", "Phoenix Bow", "Void Staff", "Aether Blade",
    "Tempest Rifle", "Plasma Scythe", "Crystal Crossbow", "Time Warp Dagger",
    "Celestial Staff", "Magma Shield"
]

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enhanced IO Game")

# Function to draw players
def draw_player(position):
    pygame.draw.circle(screen, PLAYER_COLOR, position, PLAYER_RADIUS)

# Function to draw food
def draw_food(position):
    pygame.draw.circle(screen, FOOD_COLOR, position, FOOD_RADIUS)

# Function to draw enemies
def draw_enemy(position):
    pygame.draw.circle(screen, ENEMY_COLOR, position, ENEMY_RADIUS)

# Function to spawn an enemy off-screen
def spawn_enemy(player_pos):
    while True:
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            x = random.randint(0, WIDTH)
            y = -ENEMY_RADIUS
        elif side == 'bottom':
            x = random.randint(0, WIDTH)
            y = HEIGHT + ENEMY_RADIUS
        elif side == 'left':
            x = -ENEMY_RADIUS
            y = random.randint(0, HEIGHT)
        elif side == 'right':
            x = WIDTH + ENEMY_RADIUS
            y = random.randint(0, HEIGHT)
        
        dx = player_pos[0] - x
        dy = player_pos[1] - y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        
        if distance > PLAYER_RADIUS + ENEMY_RADIUS + 50:
            return [x, y]

# Function to show upgrade menu
def show_upgrade_menu():
    font = pygame.font.Font(None, 36)
    abilities = random.sample(ABILITIES, 3)  # Randomly select 3 abilities
    weapons = random.sample(WEAPONS, 3)      # Randomly select 3 weapons
    options = abilities + weapons
    return options

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True
    player_pos = [WIDTH // 2, HEIGHT // 2]
    food_pos = [random.randint(FOOD_RADIUS, WIDTH - FOOD_RADIUS), 
                 random.randint(FOOD_RADIUS, HEIGHT - FOOD_RADIUS)]
    score = 0
    enemies = []
    game_paused = False
    selected_upgrade = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if not game_paused:
            if keys[pygame.K_UP]:
                player_pos[1] -= PLAYER_SPEED
            if keys[pygame.K_DOWN]:
                player_pos[1] += PLAYER_SPEED
            if keys[pygame.K_LEFT]:
                player_pos[0] -= PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                player_pos[0] += PLAYER_SPEED

            # Keep player within screen bounds
            player_pos[0] = max(PLAYER_RADIUS, min(WIDTH - PLAYER_RADIUS, player_pos[0]))
            player_pos[1] = max(PLAYER_RADIUS, min(HEIGHT - PLAYER_RADIUS, player_pos[1]))

            # Check for collision with food
            dx = player_pos[0] - food_pos[0]
            dy = player_pos[1] - food_pos[1]
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance < PLAYER_RADIUS + FOOD_RADIUS:
                score += 1
                food_pos = [random.randint(FOOD_RADIUS, WIDTH - FOOD_RADIUS), 
                             random.randint(FOOD_RADIUS, HEIGHT - FOOD_RADIUS)]
                if score % UPGRADE_COST == 0:
                    game_paused = True
                    options = show_upgrade_menu()

            # Spawn enemies
            if random.random() < 0.02:
                enemies.append(spawn_enemy(player_pos))

            # Move enemies towards player
            for enemy in enemies:
                enemy_dx = player_pos[0] - enemy[0]
                enemy_dy = player_pos[1] - enemy[1]
                enemy_distance = (enemy_dx ** 2 + enemy_dy ** 2) ** 0.5
                if enemy_distance > 0:
                    enemy[0] += (enemy_dx / enemy_distance) * ENEMY_SPEED
                    enemy[1] += (enemy_dy / enemy_distance) * ENEMY_SPEED

            # Check for collision with enemies
            for enemy in enemies:
                enemy_dx = player_pos[0] - enemy[0]
                enemy_dy = player_pos[1] - enemy[1]
                enemy_distance = (enemy_dx ** 2 + enemy_dy ** 2) ** 0.5
                if enemy_distance < PLAYER_RADIUS + ENEMY_RADIUS:
                    print("Game Over!")
                    running = False

        else:
            # Display upgrade menu
            font = pygame.font.Font(None, 36)
            text = font.render("Choose an upgrade:", True, (0, 0, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 20))
            for i, option in enumerate(options):
                option_text = font.render(f"{i+1}. {option}", True, (0, 0, 0))
                screen.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, 
                                           HEIGHT // 2 + i * 30))

            # Handle selection
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                selected_upgrade = options[0]
                game_paused = False
            elif keys[pygame.K_2]:
                selected_upgrade = options[1]
                game_paused = False
            elif keys[pygame.K_3]:
                selected_upgrade = options[2]
                game_paused = False

            if selected_upgrade:
                print(f"You selected: {selected_upgrade}")
                selected_upgrade = None

        # Fill the background
        screen.fill(BACKGROUND_COLOR)

        # Draw everything
        draw_player(player_pos)
        draw_food(food_pos)
        for enemy in enemies:
            draw_enemy(enemy)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()