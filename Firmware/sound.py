import pygame

def talk(state):
    pygame.mixer.init()
    if state == "batt":
        pygame.mixer.music.load("/home/pi/The-Wanderer/Firmware/sounds/batt.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    elif state == "hi":
        pygame.mixer.music.load("/home/pi/The-Wanderer/Firmware/sounds/hi.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    elif state == "bye":
        pygame.mixer.music.load("/home/pi/The-Wanderer/Firmware/sounds/bye.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    elif state == "help":
        pygame.mixer.music.load("/home/pi/The-Wanderer/Firmware/sounds/help.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    else:
        pygame.mixer.music.load("confused.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    return 1