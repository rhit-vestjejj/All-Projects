from vpython import sphere, vector, rate, color, mag, norm

# --- Define simulation constants in normalized units ---
# We work in astronomical units (AU) and years.
# In these units, for a circular orbit around the Sun,
# the gravitational constant is G = 4*pi^2.
G = 4 * 3.14159**2

# Create the Sun at the origin. Its mass is 1 (in solar mass units).
sun = sphere(pos=vector(0, 0, 0), radius=0.1, color=color.yellow, emissive=True)
sun.mass = 1

# Data for the eight planets (distance in AU, approximate colors, and visualization radii)
planet_data = [
    {"name": "Mercury", "distance": 0.39, "color": color.gray(0.5), "radius": 0.02},
    {"name": "Venus",   "distance": 0.72, "color": color.orange,   "radius": 0.04},
    {"name": "Earth",   "distance": 1.00, "color": color.blue,     "radius": 0.04},
    {"name": "Mars",    "distance": 1.52, "color": color.red,      "radius": 0.03},
    {"name": "Jupiter", "distance": 5.20, "color": color.orange,   "radius": 0.1},
    {"name": "Saturn",  "distance": 9.58, "color": color.yellow,   "radius": 0.09},
    {"name": "Uranus",  "distance": 19.2, "color": color.cyan,     "radius": 0.08},
    {"name": "Neptune", "distance": 30.05, "color": color.blue,     "radius": 0.08}
]

# Create a list to hold planet objects
planets = []
for pdata in planet_data:
    # Place each planet along the x-axis at its orbital distance (in AU)
    pos = vector(pdata["distance"], 0, 0)
    planet = sphere(pos=pos,
                    radius=pdata["radius"],
                    color=pdata["color"],
                    make_trail=True,   # leave a trail to visualize the orbit
                    retain=150)        # keep up to 150 trail points
    # (Here we assign an arbitrary small mass to each planet;
    # since only the Sun's gravity is used, the planet masses don't affect the orbit.)
    planet.mass = 1e-6

    # Compute the orbital speed for a circular orbit: v = sqrt(G*M_sun / r)
    speed = (G * sun.mass / pdata["distance"])**0.5  # in AU/year
    # Set the initial velocity perpendicular to the radius (along +y)
    planet.velocity = vector(0, speed, 0)
    
    planets.append(planet)

# Choose a time step (in years). Smaller dt gives a smoother simulation.
dt = 0.001

# --- Simulation loop ---
while True:
    rate(1000)  # control the simulation speed (1000 iterations per second)
    for planet in planets:
        # Compute the vector from the planet to the Sun
        r_vec = planet.pos - sun.pos
        r_mag = mag(r_vec)
        # Compute gravitational acceleration from the Sun:
        # a = -G * M_sun / r^2 * (r_vec normalized)
        a = -G * sun.mass / (r_mag**2) * norm(r_vec)
        # Update the planet's velocity and position using a simple Euler method
        planet.velocity = planet.velocity + a * dt
        planet.pos = planet.pos + planet.velocity * dt
