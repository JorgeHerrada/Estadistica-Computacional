import random
from calculate_statistics import desviacion_estandar, media 

def throw_needle(needle_num):
    # Counter for needles inside of the circle
    needles_inside = 0

    for _ in range(needle_num):
        # Generate random X,Y coordinate
        x = random.random() * random.choice([1,-1])
        y = random.random() * random.choice([1,-1])

        # Calcularte distance from center to needle coordinate
        distance_from_center = (x**2 + y**2)**0.5

        # Check if needle is inside of the circle
        if distance_from_center <= 1:
            needles_inside += 1
    
    # Calculate and return estimation
    return ( 4 * needles_inside ) / needle_num


def estimation(needle_num, iterations):
    # list of different estimations based on each iteration
    estimate = []

    # Calcular an estimate for each iteration and store it on "estimate" list
    for _ in range (iterations):
        PI_estimation = throw_needle(needle_num)
        estimate.append(PI_estimation)

    # Calculate mean and standard deviation
    mean_estimation = media(estimate)
    sigma = desviacion_estandar(estimate)

    # Show results
    print(f"Estimate= {round(mean_estimation,5)}, Sigma= {round(sigma,5)} Needles= {needle_num}")

    # return mean and standard deviation
    return (mean_estimation, sigma)


def estimate_PI(precision, iterations):
    # Get number of needles to throw per iteration
    # needle = int(input("Ingresa el numero de agujas: "))
    needle_num = 1000

    sigma = precision

    # estate until we reach target precision 
    # Double the needle number each time to intrease precision
    while sigma >= precision / 1.96:
        mean, sigma = estimation(needle_num,iterations)
        needle_num *= 2
    
    return mean


if __name__ == '__main__':
    estimate_PI(0.01,1000)