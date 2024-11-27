import math
from PIL import Image


def get_mode_correction(image: Image):
    if image.mode not in ['RGB', 'RGBA']:
        return 'RGB'
    return image.mode


def sqrt_algorithm(image: Image):
    mode = get_mode_correction(image)
    if mode != image.mode:
        image = image.convert('RGB')

    red_total = 0
    green_total = 0
    blue_total = 0
    alpha_total = 0
    count = 0

    pixel = image.load()

    for i in range(image.width):
        for j in range(image.height):
            color = pixel[i, j]
            if len(color) == 4:
                red, green, blue, alpha = color
            else:
                [red, green, blue], alpha = color, 255

            red_total += red * red * alpha
            green_total += green * green * alpha
            blue_total += blue * blue * alpha
            alpha_total += alpha

            count += 1

    return (
        round(math.sqrt(red_total / alpha_total)),
        round(math.sqrt(green_total / alpha_total)),
        round(math.sqrt(blue_total / alpha_total))
    )
