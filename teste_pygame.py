import pygame
pygame.init()


screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tela Inicial")

white = (255, 255, 255)
black = (0, 0, 0)
green = (50, 100, 0)


class Button:
    def __init__(self, x, y, width, height, color, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.SysFont(None, 40)
        text = font.render(self.text, True, white)
        surface.blit(text, (self.rect.centerx - text.get_width() / 2, self.rect.centery - text.get_height() / 2))


menu_options = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]

def draw_menu():
    menu_font = pygame.font.SysFont(None, 30)
    menu_items = []
    for option in menu_options:
        text = menu_font.render(option, True, white)
        menu_items.append(text)
    
    x = 20
    y = 20
    for item in menu_items:
        screen.blit(item, (x, y))
        x += item.get_width() + 20
        
play_button = Button(screen_width / 2 - 100, screen_height / 2 - 50, 200, 50, white, "Jogar")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.rect.collidepoint(event.pos):
                # Código para iniciar o jogo
                pass

    screen.fill(green)
    draw_menu()
    play_button.draw(screen)
    pygame.display.flip()

pygame.quit()
        