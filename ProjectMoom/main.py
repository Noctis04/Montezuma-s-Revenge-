import sdl2.ext
import sdl2.sdlgfx
import windowCreate
from block import Block
import softwareRenderer
from game_object import Character


sdl2.ext.init()
window = windowCreate.window
world = sdl2.ext.World()
sprite_renderer = softwareRenderer.SoftwareRenderer(window)
world.add_system(sprite_renderer)


level_dict = {
    'BackGround': Block(world, "MainBackGround.png", 0, 0,),

    'blockGround1': Block(world, "block.png", 0, 650, ),
    'blockGround2': Block(world, "block.png", 240, 650, ),
    'blockGround3': Block(world, "block.png",480,650,),
    'blockGround4': Block(world, "block.png",720,650,),
    'blockGround5': Block(world, "block.png",960,650,),

    'blockPlatform1':Block(world, "block.png",200,360,),
    'blockPlatform2':Block(world, "block.png",520,200,),
    'blockPlatform3':Block(world, "block.png",900,300,),

}

character = Character(world,  "Character2.png", 0, 470,)

running = True
while running:
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break
        if event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.sym == sdl2.SDLK_LEFT:
                character.sprite.x -= 10
            elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
               character.sprite.x += 10
            elif event.key.keysym.sym == sdl2.SDLK_UP:
               character.sprite.y -= 10
            elif event.key.keysym.sym == sdl2.SDLK_DOWN:
               character.sprite.y += 10


    world.process()

sdl2.ext.quit()
