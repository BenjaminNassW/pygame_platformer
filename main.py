import pygame
import sys
import mario_sprite

pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario-like Game")

# Load the sprite sheet
mario_spritesheet = pygame.image.load(
    "C:/Users/benja/OneDrive/Desktop/pygame/mario.png").convert_alpha()

# Initial player position
player_x, player_y = screen_width // 2, screen_height // 2

# Scale factor for the sprite
scale_factor = 5  # Adjust this value to control the scale

# Player speed
player_speed = 5

# Create sprite sheets
sprite_sheet = mario_sprite.SpriteSheet(mario_spritesheet)
sprite_sheet_walk = mario_sprite.SpriteSheet(mario_spritesheet)

# Load frames
frame_idle = sprite_sheet.get_image(209, 14, 20, scale_factor)
frame_walk = sprite_sheet_walk.get_image(328, 15, 20, scale_factor)

# Initial state
current_frame = frame_idle
walking_frames = [frame_walk, frame_idle]
walk_frame_index = 0
walk_frame_timer = 0
walk_frame_delay = 5  # Adjust this value to control the walking animation speed


# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
        # Switch to walking frame when moving left
        current_frame = walking_frames[walk_frame_index]
    elif keys[pygame.K_RIGHT] and player_x < screen_width - sprite_sheet.width * scale_factor:
        player_x += player_speed
        # Switch to walking frame when moving right
        current_frame = walking_frames[walk_frame_index]
    else:
        current_frame = frame_idle  # Switch back to idle frame when not moving

    # Update walking frame index and timer
    walk_frame_timer += 1
    if walk_frame_timer >= walk_frame_delay:
        walk_frame_timer = 0
        walk_frame_index = (walk_frame_index + 1) % len(walking_frames)
 
    # Draw the sprite onto the screen
    screen.fill((255, 255, 255))  # Fill the screen with a white background
    screen.blit(current_frame, (player_x, player_y))
    pygame.display.flip()

    clock.tick(60)  # Adjust the frame rate to control animation speed
