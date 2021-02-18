import math

length = float(input('Length: ')) 
if (length < 0):
    print('Length must be >= 0. Please try again.')
    quit()

square_area = length**2
cube_vol = length**3
area_circle = math.pi*(length)**2
sphere_vol = (4/3)*math.pi*(length)**3
cyl_vol = length*area_circle

