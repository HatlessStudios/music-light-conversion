import unicornhat as uh

def wavelength_to_RGB(wavelength, gamma = 0.8):

    '''
    A function which converts a given wavelength to an RGB triple.

    :param wavelength: The wavelength to be converted
    :param gamma: The gamma (defaulted to 0.8 because I don't understand gamma)
    :return: An RGB triple
    '''

    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))

def unicorn_hat_output(R, G, B):

    '''
    A function which takes RGB values and outputs it to the Pi's hat

    :param R:
    :param G:
    :param B:
    '''

    uh.set_layout(uh.HAT)
    uh.brightness(0.5)
    for x in range(9):
        for y in range(9):
            uh.set_pixel(x, y, R, G, B)
    uh.show()

def find_light_wavelength(note_frequency):

    '''
    A function which converts a sound frequency to its corresponding light frequency

    :param note_frequency: The frequency of the note played.
    :return: The wavelength of the corresponding light in nm
    '''

    light_frequency = note_frequency

    while light_frequency < 4e+14:
        light_frequency *= 2

    light_wavelength = 3e+8 / light_frequency
    light_wavelength *= 10**9

    return light_wavelength



