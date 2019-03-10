import numpy as np
import pyrodeo
# Extra source terms: planet gravity
def planet_source(t, dt, coords, state, planetParam):
    # Mass ratio planet/star
    mp = planetParam[0]
    # mp = 0.001
    # Softening length planet potential
    eps = planetParam[1]
    v_drift = planetParam[2]
    # Coordinates
    r = coords.x
    p = coords.y
    # Planet coordinates
    rp = 1.0
    pp = 0.0
    # Distance to the planet
    dist = np.sqrt(r*r + rp*rp - 2.0*r*rp*np.cos(p - pp) + eps*eps)
    # Potential gradient
    dpotdr = mp*(r - rp*np.cos(p - pp))/(dist*dist*dist)
    dpotdp = mp*r*rp*np.sin(p - pp)/(dist*dist*dist)
    # Indirect term
    dpotdr += mp*np.cos(p - pp)/(rp*rp)
    dpotdp -= mp*r*np.sin(p - pp)/(rp*rp)
    # Resulting source term
    source_velx = -dpotdr
    source_vely = -dpotdp/(r*r)
    source_vely += 0.5*(r**(-1.5))*v_drift


    # Damping boundary conditions
    # Rin = 100.0*(r - 0.5)*(r - 0.5)
    # Rin[np.where(r > 0.5)] = 0.0
    # Rout = (r - 2.1)*(r - 2.1)/(0.4*0.4)
    # Rout[np.where(r < 2.1)] = 0.0
    # R = (Rin + Rout)*np.power(r, -1.5)
    # Damp towards initial state
    # source_dens = -(state.dens - 1.0)*R
    # source_velx -= state.velx*R
    # source_vely -= state.vely*R

    # Integrate extra source terms
    # source_dens = state.dens
    # state.dens += dt*source_dens*state.no_ghost

    state.velx += dt*source_velx*state.no_ghost
    state.vely += dt*source_vely*state.no_ghost

    #Drift term
    # source_term = 0.5*(r**(-1.5))*v_drift
    # state.velx += dt*source_term*state.no_ghost


sim = pyrodeo.Simulation.from_geom('cyl', dimensions=[128, 384, 1],
                                    domain=([0.4, 2.5], [-np.pi, np.pi], []))

# Sound speed constant H/r = 0.05
# pp 1205, http://dx.doi.org/10.1051/0004-6361:20053761
sim.state.soundspeed = 0.05*sim.state.soundspeed/np.sqrt(sim.coords.x)
v_drift = 0.2*sim.state.soundspeed  # define Drift Velocity
sim.state.dens = 1.0/sim.coords.x  # define density

sim.state.velx = v_drift

sim.param.boundaries[0] = ['nonreflecting','nonreflecting']
sim.param.boundaries[1] = ['nonreflecting','nonreflecting']
# Simulate a Jupiter planet up to 100 orbits

sim.evolve(2.0*np.pi*np.array([100]),
                    planet_source, (0, 0.6*0.05, v_drift), new_file=True)
#20%---100 orbits--no planet