import pygame
pygame.init()

x = 640

y = 360

velocidade = 10

fundo = pygame.image.load('Slide1.jpg')

moto = pygame.image.load('imagem moto pequena.jpg')

janela = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('GP RANCING')

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandoos = pygame.key.get_pressed()
    if comandoos[pygame.K_UP]:
        y -= velocidade
    if comandoos[pygame.K_DOWN]:
        y += velocidade
    if comandoos[pygame.K_RIGHT]:
        x += velocidade
    if comandoos[pygame.K_LEFT]:
         x -= velocidade

    janela.blit(fundo, (0, 0))
    janela.blit(moto, (x, y))
    pygame.display.update()

pygame.quit()