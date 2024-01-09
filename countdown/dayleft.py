import pygame
import sys
from datetime import datetime, timedelta

# Function to update countdown
def update_countdown(target_datetime):
    current_datetime = datetime.now()
    time_diff = target_datetime - current_datetime

    if time_diff.total_seconds() < 0:
        return "Countdown completed!"
    else:
        days_left = int(time_diff.days)
        hours_left, remainder = divmod(time_diff.seconds, 3600)
        minutes_left, seconds_left = divmod(remainder, 60)

        return f"{days_left}d {hours_left:02d}h {minutes_left:02d}m {seconds_left:02d}s"

# Main function
def main():
    # Input format: YYYY-MM-DD HH:MM:SS
    # initial_date_time 2024-03-02 00:00:00
    target_date_time = "2024-03-02 00:00:00"
    event_name = "InterSpeech 2024 Deadline"
    target_datetime = datetime.strptime(target_date_time, "%Y-%m-%d %H:%M:%S")

    pygame.init()

    # Set up the window
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Countdown Wallpaper")
    
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # show the event name
        
        countdown_text = update_countdown(target_datetime)
        text_surface = font.render(countdown_text, True, (255, 255, 255))
        event_name_surface = font.render(event_name, True, (255, 255, 255))
        
        screen.fill((0, 0, 0))
        # center the text
        screen.blit(text_surface, (300 - text_surface.get_width() // 2, 300 - text_surface.get_height() // 2))
        screen.blit(event_name_surface, (300 - event_name_surface.get_width() // 2, 400 - event_name_surface.get_height() // 2))

        pygame.display.flip()

        clock.tick(1)  # Update every second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


