import pygame
import math
import random
from constants import (
    Color, Display, PLAYER_SIZE,
    PLAYER_MAX_RTSPD, SMALL_SAUCER_ACCURACY
)
from asteroid import Asteroid
from saucer import Saucer
from player import Player
from bullet import Bullet
from game_object import GameObject
from utilities import draw_text


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(
            (Display.width, Display.height))
        pygame.display.set_caption("Asteroids")
        self.timer = pygame.time.Clock()
        self.is_running = False

    def quit(self):
        self.is_running = False

    def gameLoop(self):
        self.is_running = True
        gameState = "Menu"
        player_state = "Alive"
        player_blink = 0
        player_pieces = []
        player_dying_delay = 0
        player_invi_dur = 0
        hyperspace = 0
        next_level_delay = 0
        bullet_capacity = 4
        bullets = []
        asteroids = []
        stage = 3
        score = 0
        live = 2
        oneUp_multiplier = 1
        playOneUpSFX = 0
        intensity = 0
        player = Player(Display.width / 2, Display.height / 2, self)
        saucer = Saucer(self)

        while gameState != "Exit":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameState = "Exit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.thrust = True
                    if event.key == pygame.K_LEFT:
                        player.rtspd = -PLAYER_MAX_RTSPD
                    if event.key == pygame.K_RIGHT:
                        player.rtspd = PLAYER_MAX_RTSPD
                    if event.key == pygame.K_SPACE and player_dying_delay == 0 and len(bullets) < bullet_capacity:
                        bullets.append(Bullet(player.x, player.y, player.dir))
                        pygame.mixer.Sound.play(snd_fire)
                    if gameState == "Game Over":
                        if event.key == pygame.K_r:
                            gameState = "Exit"
                            gameLoop("Playing")
                    if event.key == pygame.K_LSHIFT:
                        hyperspace = 30
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        player.thrust = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player.rtspd = 0

            player.updatePlayer()

            if player_invi_dur != 0:
                player_invi_dur -= 1
            elif hyperspace == 0:
                player_state = "Alive"

            gameDisplay.fill(Color.black)

            if hyperspace != 0:
                player_state = "Died"
                hyperspace -= 1
                if hyperspace == 1:
                    player.x = random.randrange(0, Display.width)
                    player.y = random.randrange(0, Display.height)

            for a in asteroids:
                a.updateAsteroid()
                if player_state != "Died":
                    if isColliding(player.x, player.y, a.x, a.y, a.size):
                        # Create ship fragments
                        player_pieces.append(PlayerDeathPiece(
                            player.x, player.y, 5 * PLAYER_SIZE / (2 * math.cos(math.atan(1 / 3)))))
                        player_pieces.append(PlayerDeathPiece(
                            player.x, player.y, 5 * PLAYER_SIZE / (2 * math.cos(math.atan(1 / 3)))))
                        player_pieces.append(PlayerDeathPiece(
                            player.x, player.y, PLAYER_SIZE))

                        player_state = "Died"
                        player_dying_delay = 30
                        player_invi_dur = 120
                        player.killPlayer()

                        if live != 0:
                            live -= 1
                        else:
                            gameState = "Game Over"

                        if a.t == "Large":
                            asteroids.append(Asteroid(a.x, a.y, "Normal"))
                            asteroids.append(Asteroid(a.x, a.y, "Normal"))
                            score += 20
                            pygame.mixer.Sound.play(snd_bangL)
                        elif a.t == "Normal":
                            asteroids.append(Asteroid(a.x, a.y, "Small"))
                            asteroids.append(Asteroid(a.x, a.y, "Small"))
                            score += 50
                            pygame.mixer.Sound.play(snd_bangM)
                        else:
                            score += 100
                            pygame.mixer.Sound.play(snd_bangS)
                        asteroids.remove(a)

            for f in player_pieces:
                f.updateDeadPlayer()
                if f.x > Display.width or f.x < 0 or f.y > Display.height or f.y < 0:
                    player_pieces.remove(f)

            if len(asteroids) == 0 and saucer.state == "Dead":
                if next_level_delay < 30:
                    next_level_delay += 1
                else:
                    stage += 1
                    intensity = 0
                    for i in range(stage):
                        xTo = Display.width / 2
                        yTo = Display.height / 2
                        while xTo - Display.width / 2 < Display.width / 4 and yTo - Display.height / 2 < Display.height / 4:
                            xTo = random.randrange(0, Display.width)
                            yTo = random.randrange(0, Display.height)
                        asteroids.append(Asteroid(xTo, yTo, "Large"))
                    next_level_delay = 0

            if intensity < stage * 450:
                intensity += 1

            if saucer.state == "Dead":
                if (
                    random.randint(0, 6000) <= (intensity * 2) / (stage * 9) and
                    next_level_delay == 0
                ):
                    saucer.reset()
                    if score >= 40000:
                        saucer.type = "Small"
            else:
                acc = SMALL_SAUCER_ACCURACY * 4 / stage
                saucer.bdir = math.degrees(
                    math.atan2(-saucer.y + player.y, -saucer.x + player.x) + math.radians(random.uniform(acc, -acc)))

                saucer.update()
                saucer.draw()

                for a in asteroids:
                    if isColliding(saucer.x, saucer.y, a.x, a.y, a.size + saucer.size):
                        saucer.state = "Dead"

                        if a.t == "Large":
                            asteroids.append(Asteroid(a.x, a.y, "Normal"))
                            asteroids.append(Asteroid(a.x, a.y, "Normal"))
                            pygame.mixer.Sound.play(snd_bangL)
                        elif a.t == "Normal":
                            asteroids.append(Asteroid(a.x, a.y, "Small"))
                            asteroids.append(Asteroid(a.x, a.y, "Small"))
                            pygame.mixer.Sound.play(snd_bangM)
                        else:
                            pygame.mixer.Sound.play(snd_bangS)
                        asteroids.remove(a)

                for b in bullets:
                    if isColliding(b.x, b.y, saucer.x, saucer.y, saucer.size):
                        if saucer.type == "Large":
                            score += 200
                        else:
                            score += 1000

                        saucer.state = "Dead"

                        pygame.mixer.Sound.play(snd_bangL)

                        bullets.remove(b)

                if isColliding(saucer.x, saucer.y, player.x, player.y, saucer.size):
                    if player_state != "Died":
                        player_pieces.append(PlayerDeathPiece(
                            player.x, player.y, 5 * PLAYER_SIZE / (2 * math.cos(math.atan(1 / 3)))))
                        player_pieces.append(PlayerDeathPiece(
                            player.x, player.y, 5 * PLAYER_SIZE / (2 * math.cos(math.atan(1 / 3)))))
                        player_pieces.append(PlayerDeathPiece(
                            player.x, player.y, PLAYER_SIZE))

                        player_state = "Died"
                        player_dying_delay = 30
                        player_invi_dur = 120
                        player.killPlayer()

                        if live != 0:
                            live -= 1
                        else:
                            gameState = "Game Over"

                        pygame.mixer.Sound.play(snd_bangL)

                for b in saucer.bullets:
                    b.updateBullet()

                    for a in asteroids:
                        if isColliding(b.x, b.y, a.x, a.y, a.size):
                            if a.t == "Large":
                                asteroids.append(Asteroid(a.x, a.y, "Normal"))
                                asteroids.append(Asteroid(a.x, a.y, "Normal"))
                                pygame.mixer.Sound.play(snd_bangL)
                            elif a.t == "Normal":
                                asteroids.append(Asteroid(a.x, a.y, "Small"))
                                asteroids.append(Asteroid(a.x, a.y, "Small"))
                                pygame.mixer.Sound.play(snd_bangL)
                            else:
                                pygame.mixer.Sound.play(snd_bangL)

                            asteroids.remove(a)
                            saucer.bullets.remove(b)

                            break

                    if isColliding(player.x, player.y, b.x, b.y, 5):
                        if player_state != "Died":
                            player_pieces.append(PlayerDeathPiece(
                                player.x, player.y, 5 * PLAYER_SIZE / (2 * math.cos(math.atan(1 / 3)))))
                            player_pieces.append(PlayerDeathPiece(
                                player.x, player.y, 5 * PLAYER_SIZE / (2 * math.cos(math.atan(1 / 3)))))
                            player_pieces.append(PlayerDeathPiece(
                                player.x, player.y, PLAYER_SIZE))

                            player_state = "Died"
                            player_dying_delay = 30
                            player_invi_dur = 120
                            player.killPlayer()

                            if live != 0:
                                live -= 1
                            else:
                                gameState = "Game Over"

                            # Play SFX
                            pygame.mixer.Sound.play(snd_bangL)

                            # Remove bullet
                            saucer.bullets.remove(b)

                    if b.life <= 0:
                        try:
                            saucer.bullets.remove(b)
                        except ValueError:
                            continue

            # Bullets
            for b in bullets:
                # Update bullets
                b.updateBullet()

                # Check for bullets collide w/ asteroid
                for a in asteroids:
                    if b.x > a.x - a.size and b.x < a.x + a.size and b.y > a.y - a.size and b.y < a.y + a.size:
                        # Split asteroid
                        if a.t == "Large":
                            asteroids.append(Asteroid(a.x, a.y, "Normal"))
                            asteroids.append(Asteroid(a.x, a.y, "Normal"))
                            score += 20
                            # Play SFX
                            pygame.mixer.Sound.play(snd_bangL)
                        elif a.t == "Normal":
                            asteroids.append(Asteroid(a.x, a.y, "Small"))
                            asteroids.append(Asteroid(a.x, a.y, "Small"))
                            score += 50
                            # Play SFX
                            pygame.mixer.Sound.play(snd_bangM)
                        else:
                            score += 100
                            # Play SFX
                            pygame.mixer.Sound.play(snd_bangS)
                        asteroids.remove(a)
                        bullets.remove(b)

                        break

                # Destroying bullets
                if b.life <= 0:
                    try:
                        bullets.remove(b)
                    except ValueError:
                        continue

            # Extra live
            if score > oneUp_multiplier * 10000:
                oneUp_multiplier += 1
                live += 1
                playOneUpSFX = 60
            # Play sfx
            if playOneUpSFX > 0:
                playOneUpSFX -= 1
                pygame.mixer.Sound.play(snd_extra, 60)

            # Draw player
            if gameState != "Game Over":
                if player_state == "Died":
                    if hyperspace == 0:
                        if player_dying_delay == 0:
                            if player_blink < 5:
                                if player_blink == 0:
                                    player_blink = 10
                                else:
                                    player.drawPlayer()
                            player_blink -= 1
                        else:
                            player_dying_delay -= 1
                else:
                    player.drawPlayer()
            else:
                draw_text(self.display, "Game Over", Color.white, Display.width /
                          2, Display.height / 2, 100)
                draw_text(self.display, "Press \"R\" to restart!", Color.white,
                          Display.width / 2, Display.height / 2 + 100, 50)
                live = -1

            # Draw score
            draw_text(self.display, str(score), Color.white, 60, 20, 40, False)

            # Draw Lives
            for l in range(live + 1):
                Player(75 + l * 25, 75).drawPlayer()

            # Update screen
            pygame.display.update()

            # Tick fps
            self.timer.tick(30)
        pygame.quit()
