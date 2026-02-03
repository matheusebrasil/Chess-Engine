import pygame as p
from ChessEngine import GameState, Move  # Importação essencial

# Configurações do Pygame
WIDTH = HEIGHT = 512 
DIMENSION = 8 
SQ_SIZE = HEIGHT // DIMENSION # Tamanho de cada quadrado (64px)
MAX_FPS = 15 
IMAGES = {}

def loadImages():
    # A lista deve usar os nomes EXATOS que estão na matriz do GameState ("wP", não "wp")
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        # Nota: O arquivo na pasta images deve se chamar ex: "wP.png"
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def drawGameState(screen, gs):
    drawBoard(screen) # Desenha os quadrados
    drawPieces(screen, gs.board) # Desenha as peças por cima

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": # Se não for uma casa vazia
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    
    gs = GameState()
    
    # Tenta carregar as imagens
    try:
        loadImages() 
    except Exception as e:
        print(f"ERRO: Verifique a pasta images. {e}")
        return

    # --- VARIÁVEIS DE CONTROLE DO MOUSE ---
    sqSelected = () # Mantém o registro do último clique do usuário (tupla: (linha, col))
    playerClicks = [] # Mantém o registro dos cliques (duas tuplas: [(6, 4), (4, 4)])

    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            
            # --- LÓGICA DE MOVIMENTO DO MOUSE ---
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) posição do mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                
                # Se o usuário clicou no mesmo quadrado duas vezes (deselecionar)
                if sqSelected == (row, col):
                    sqSelected = () # limpa seleção
                    playerClicks = [] # limpa cliques
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # adiciona o 1º ou 2º clique
                
                # Se for o segundo clique (temos origem e destino)
                if len(playerClicks) == 2:
                    move = Move(playerClicks[0], playerClicks[1], gs.board)
                    print(f"Tentando mover de {playerClicks[0]} para {playerClicks[1]}")
                    
                    # Executa o movimento
                    gs.makeMove(move)
                    
                    # Reseta para o próximo turno
                    sqSelected = () 
                    playerClicks = [] 

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

if __name__ == "__main__":
    main()