from math import modf, pi
import argparse
from inflect import engine

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
            if str(pi)[i+2] == str(pi_est)[i+2]: # Skip 3, skip .
                terms_per_dp.append(num_terms)
                i += 1
        
        denom += 2
        
        # print(pi_est)
    return terms_per_dp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dp', type=int, help='How many places of accuracy?')
    args = parser.parse_args()

    accum_terms = est_pi(args.dp)

    eng = engine()
    for place, terms in enumerate(accum_terms):
        print("It took {} terms to get the correct digit at {} decimal place.".format(terms, eng.ordinal(1+place)))

if __name__ == '__main__':
    main()