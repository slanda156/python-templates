from logging import getLogger
import time

import pygame as pg


logger = getLogger(__name__)


class App:
    def __init__(self, fps: int, winSize: tuple[int, int], fullscreen: bool = False):
        pg.init()
        self.winSize = winSize
        self.fps = fps
        if fullscreen:
            self.screen = pg.display.set_mode(self.winSize, pg.FULLSCREEN)
        else:
            self.screen = pg.display.set_mode(self.winSize)
        pg.display.set_caption("Pygame App")
        self.clock = pg.time.Clock()
        self.debugFont = pg.font.SysFont("monospace", 15)
        self.running = True
        self.paused = True
        self.forceTick = False
        self.debug = True
        self.help = True
        self.ticks = -1
        self.debugTextLenght = 0
        self.helpTextLenght = 0
        self.updateTime = 0
        self.renderTime = 0

    def gameloop(self):
        self.screen.fill(pg.Color("grey"))
        while self.running:
            self.eventHandler()
            if not self.paused or self.forceTick:
                startTime = time.time()
                self.update()
                self.updateTime = (time.time() - startTime) * 1000
            startTime = time.time()
            self.render()
            self.renderTime = (time.time() - startTime) * 1000
            self.clock.tick(self.fps)
        pg.quit()

    def quit(self) -> None:
        self.running = False
        logger.info("Exiting...")

    def eventHandler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            # Check keyboard events
            elif event.type == pg.KEYDOWN:
                # Escape key to quit
                if event.key == pg.K_ESCAPE:
                    self.quit()
                # + key to increase fps
                elif event.key == pg.K_PLUS or event.key == pg.K_KP_PLUS:
                    self.fps += 5
                # - key to decrease fps
                elif event.key == pg.K_MINUS or event.key == pg.K_KP_MINUS:
                    self.fps -= 5
                    if self.fps < 1:
                        self.fps = 1
                # d key to toggle debug
                elif event.key == pg.K_d:
                    self.debug = not self.debug
                # h key to toggle help
                elif event.key == pg.K_h:
                    self.help = not self.help
                # p key to pause
                elif event.key == pg.K_p:
                    self.paused = not self.paused
                # s key to force tick
                elif event.key == pg.K_s and self.paused:
                    self.forceTick = True

    def update(self):
        pass
        self.ticks += 1
        self.forceTick = False

    def render(self):
        toUpdate = []
        # Render objects
        toUpdate.extend(self.renderObjects())
        # Render debug text
        if self.debug:
            toUpdate.extend(self.renderDebugText())
        # Render help text
        if self.help:
            toUpdate.extend(self.renderHelpText())
        # Remove None values
        while None in toUpdate:
            toUpdate.remove(None)
        # Update display
        if len(toUpdate) == 0 or (self.debug and len(toUpdate) == 1):
            pg.display.update()
        else:
            pg.display.update(toUpdate)

    def renderDebugText(self) -> list[pg.Rect]:
        color =  (255, 0, 0)
        fpsText = self.debugFont.render(f"FPS: {round(self.clock.get_fps(), 1)} / {self.fps}", True, color)
        timeText = self.debugFont.render(f"A: {round(self.clock.get_rawtime(), 3)}ms", True, color)
        updateText = self.debugFont.render(f"U: {round(self.updateTime, 3)}ms", True, color)
        renderText = self.debugFont.render(f"R: {round(self.renderTime, 3)}ms", True, color)
        tickText = self.debugFont.render(f"Tick: {self.ticks}", True, color)
        lenghts = [fpsText.get_width(), updateText.get_width(), renderText.get_width(), timeText.get_width(), tickText.get_width()]
        lenght = max(lenghts)
        if self.debugTextLenght < lenght:
            self.debugTextLenght = lenght
        debugFrame = pg.Surface((self.debugTextLenght + 10, 75))
        debugFrame.blit(fpsText, (0, 0))
        debugFrame.blit(timeText, (0, 15))
        debugFrame.blit(updateText, (0, 30))
        debugFrame.blit(renderText, (0, 45))
        debugFrame.blit(tickText, (0, 60))
        # Render debug frame
        self.screen.blit(debugFrame, (5, 5))
        return [pg.Rect(5, 5, debugFrame.get_width(), debugFrame.get_height()), ]

    def renderHelpText(self) -> list[pg.Rect]:
        color =  (255, 0, 0)
        pos = (self.winSize[0] - self.helpTextLenght - 5, 5)
        lines = []
        lines.append(self.debugFont.render("ESC - Close window", True, color))
        lines.append(self.debugFont.render("+   - Increase FPS", True, color))
        lines.append(self.debugFont.render("-   - Decrease FPS", True, color))
        lines.append(self.debugFont.render("D   - Toggle debug", True, color))
        lines.append(self.debugFont.render("H   - Toggle help", True, color))
        lines.append(self.debugFont.render("P   - Pause", True, color))
        lines.append(self.debugFont.render("S   - Force tick", True, color))
        lenghts = [line.get_width() for line in lines]
        lenght = max(lenghts)
        if self.helpTextLenght < lenght:
            self.helpTextLenght = lenght
        helpFrame = pg.Surface((self.helpTextLenght + 10, 15*len(lines)))
        for line in lines:
            helpFrame.blit(line, (0, 15*lines.index(line)))
        # Render help frame
        self.screen.blit(helpFrame, pos)
        return [pg.Rect(pos[0], pos[1], helpFrame.get_width(), helpFrame.get_height()), ]

    def renderObjects(self) -> list[pg.Rect]:
        toUpdate = []
        return toUpdate