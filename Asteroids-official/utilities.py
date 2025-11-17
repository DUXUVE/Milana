import pygame


def drawText(gameDisplay: pygame.Surface, msg, color, x, y, s, center=True):
    screen_text = pygame.font.SysFont("Calibri", s).render(msg, True, color)
    if center:
        rect = screen_text.get_rect()
        rect.center = (x, y)
    else:
        rect = pygame.Rect(x, y, s, s)
    gameDisplay.blit(screen_text, rect)


def is_colliding(centerX: int, centerY: int, centerXTo: int, centerYTo: int, radius: int):
    is_horizontal_collided = centerX > centerXTo - radius and centerX < centerXTo + radius
    is_vertical_collided = centerY > centerYTo - radius and centerY < centerYTo + radius
    return is_horizontal_collided and is_vertical_collided