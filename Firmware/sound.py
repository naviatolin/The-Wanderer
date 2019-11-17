import pygame

def talk(state):
    pygame.mixer.init()
    if state == "batt":
        pygame.mixer.music.load("batt.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    elif state == "hi":
        pygame.mixer.music.load("hi.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    elif state == "bye":
        pygame.mixer.music.load("bye.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    elif state == "help":
        pygame.mixer.music.load("help.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    else:
        pygame.mixer.music.load("confused.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    return 1