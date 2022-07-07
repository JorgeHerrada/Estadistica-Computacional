import random
from calculate_statistics import desviacion_estandar, media 

def throw_needle(needle_num):
    # Counter for needles inside of the circle
    needles_inside = 0

    # Generate random X,Y coordinate
    for _ in range(needle_num):
        x = random.random() * random.choice([1,-1])
        y = random.random() * random.choice([1,-1])

        distance_from_center = (x**2 + y**2)**0.5

        if distance_from_center <= 1:
            needles_inside += 1
    
    return ( 4 * needles_inside ) / needle_num


def estimation(needle_num, iterations):
    estimate = []

    for _ in range (iterations):
        PI_estimation = throw_needle(needle_num)
        estimate.append(PI_estimation)

    mean_estimation = media(estimate)
    sigma = desviacion_estandar(estimate)

    print(f"Estimate= {round(mean_estimation,5)}, Sigma= {round(sigma,5)} Needles= {needle_num}")

    return (mean_estimation, sigma)


def estimate_PI(precision, iterations):
    needle_num = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        mean, sigma = estimation(needle_num,iterations)
        needle_num *= 2
    
    return mean


if __name__ == '__main__':
    estimate_PI(0.01,1000)