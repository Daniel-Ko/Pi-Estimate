from math import modf, pi

def est_pi(dp):
    estimation = 1
    denom = 3
    num_terms = 1
    swing = False
    
    terms_per_dp = []

    i = 0
    while i < dp:
        
        if swing:
            estimation += 1/denom
        else:
            estimation -= 1/denom
        
        num_terms += 1
        swing = not swing


        pi_est = 4 * estimation
        if dp <= len(str(pi_est)):
            print("{}, {}".format(str(modf(pi)[0])[i+2],str(modf(pi_est)[0])[i+2]))
            if str(modf(pi)[0])[i+2] == str(modf(pi_est)[0])[i+2]: # Skip 3, skip .
                terms_per_dp.append(num_terms)
                i += 1
        
        denom += 2
        
        # print(pi_est)
    return terms_per_dp


print("It took {} terms to get the correct digit at {} decimal place.".format(est_pi(2), 'first'))