import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my first game screen")


GREY = (58, 58, 58)

IMAGE_PATH = "my_image.png"
IMAGE_SIZE = (300, 300)

try:
    if not pygame.path.isfile(IMAGE_PATH):
        raise FileNotFoundError(f"Image file '{IMAGE_PATH}' not found.")
    
    image = pygame.image.load(IMAGE_PATH)
    image = pygame.transform.scale(image, IMAGE_SIZE)
except Exception as e:
    print(f"Error loading image: {e}")
    pygame.quit()


image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(GREY)
    window.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()

