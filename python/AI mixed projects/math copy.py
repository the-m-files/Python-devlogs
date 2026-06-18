import random

def generate_real_quadratic():
    # Random coefficients a, b, c between -20 and 20 (excluding a = 0)
    a = random.choice([x for x in range(-20, 21) if x != 0])
    b = random.randint(-20, 20)
    c = random.randint(-20, 20)
    
    # Calculate Discriminant
    discriminant = (b**2) - (4*a*c)
    
    if discriminant >= 0:
        # Check if the roots will be rational or irrational
        perfect_square = (discriminant**0.5).is_integer()
        
        print(f"Equation: {a}x² + {b}x + {c} = 0")
        print(f"Discriminant (Δ): {discriminant}")
        print("Type: Real Roots")
        print("Nature: " + ("Rational" if perfect_square else "Irrational"))
        global con
        global dis
        con = -1*b/(2*a)
        dis = (b*b)-(4*a*c)
        dis = dis **0.5
        dis = dis/(2*a)
    else:
        # Recursively call function until a real root equation is generated
        generate_real_quadratic()

generate_real_quadratic()





print(f"Your roots are ({con-dis}, {con+dis})")