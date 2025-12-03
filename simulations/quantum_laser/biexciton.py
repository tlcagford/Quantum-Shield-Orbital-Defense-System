import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

# Define the states
# We have four levels: |0>, |H>, |V>, |B>
# We will use the basis: [|0>, |H>, |V>, |B>]
# So the ground state is:
g = qt.basis(4, 0)
# The exciton state with H polarization:
H = qt.basis(4, 1)
# The exciton state with V polarization:
V = qt.basis(4, 2)
# The biexciton state:
B = qt.basis(4, 3)

# Define the operators
# We will define the lowering operators for the decays
# From B to H: emits an H photon, leaving the dot in H state
sigma_B_H = B * H.dag()
# From B to V: emits a V photon, leaving the dot in V state
sigma_B_V = B * V.dag()
# From H to g: emits an H photon? Actually, when the exciton decays, it emits a photon of the same polarization.
# So from H to g, we emit an H photon.
sigma_H_g = H * g.dag()
# From V to g, we emit a V photon.
sigma_V_g = V * g.dag()

# We assume the biexciton is pumped from the ground state at a rate P
# The Hamiltonian for the pumping: H_pump = P (|B><0| + |0><B|)
# But note: the pumping might be via a laser, so we can model it as a coherent drive.
# However, for simplicity, we will model the pumping as a Lindblad operator (incoherent pumping).
# Alternatively, we can model it as a Hamiltonian term. Let's do both and see.

# Parameters
gamma = 1.0  # decay rate for the exciton (assumed same for H and V)
gamma_B = 0.5  # decay rate for the biexciton (could be different)
P = 0.1  # pumping rate from ground to biexciton

# Hamiltonian: We assume no coherent drive for now, so only the energy levels.
# We set the energy of the ground state to 0.
# Let the exciton states have energy E_X and the biexciton have energy E_B.
E_X = 2.0  # arbitrary units
E_B = 4.0  # biexciton energy (should be less than 2*E_X due to binding energy)

H0 = E_X * (H * H.dag() + V * V.dag()) + E_B * B * B.dag()

# For the pumping, we add a Hamiltonian term: H_pump = P * (|B><0| + |0><B|)  (coherent pumping)
# But note: coherent pumping would create a superposition, but we want to model an incoherent pump.
# We can model the pump as a Lindblad operator that takes the dot from |0> to |B> at rate P.
# Let's do that.

# Collapse operators for decays and pumping
c_ops = []
# Decay from biexciton to exciton (with either polarization)
c_ops.append(np.sqrt(gamma_B/2) * sigma_B_H)  # decay B -> H, emitting an H photon? Actually, the photon emitted in this step is H? Yes, in the model we defined.
c_ops.append(np.sqrt(gamma_B/2) * sigma_B_V)  # decay B -> V, emitting a V photon
# Decay from exciton to ground
c_ops.append(np.sqrt(gamma) * sigma_H_g)  # decay H -> g, emitting an H photon
c_ops.append(np.sqrt(gamma) * sigma_V_g)  # decay V -> g, emitting a V photon
# Incoherent pumping from ground to biexciton
c_ops.append(np.sqrt(P) * g * B.dag())  # note: this operator takes |B> to |0>, but we want pumping from |0> to |B>? Actually, the Lindblad operator for pumping is usually written as sqrt(P) * |B><0|, which does exactly that.

# Initial state: let's start in the ground state
psi0 = g

# Times for evolution
tlist = np.linspace(0, 50, 501)

# Solve the master equation
result = qt.mesolve(H0, psi0, tlist, c_ops, [])

# We can calculate the population of each state
populations = qt.expect([g*g.dag(), H*H.dag(), V*V.dag(), B*B.dag()], result.states)

# Plot the populations
plt.figure()
plt.plot(tlist, populations[0], label='Ground')
plt.plot(tlist, populations[1], label='H exciton')
plt.plot(tlist, populations[2], label='V exciton')
plt.plot(tlist, populations[3], label='Biexciton')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Biexciton decay dynamics with incoherent pumping')
plt.show()

# Now, we want to study the entanglement between the emitted photons.
# We need to look at the two-photon state. We can calculate the joint polarization state of the two emitted photons.
# However, in this model, we are not keeping track of the photons. We are only looking at the dot.
# To study the entanglement of the emitted photons, we need to include the photon states in our Hilbert space.
# This would make the system much larger. Alternatively, we can use the method of quantum trajectories and record the jumps (photon emissions).
# We will do a quantum trajectory simulation and post-select on trajectories where two photons are emitted, and then analyze the polarization of the two photons.

# Let's do a quantum trajectory simulation and look at the two-photon emission events.

# We define the collapse operators that correspond to photon emissions:
# We have four collapse operators that lead to photon emissions:
# 1. sigma_B_H: emits an H photon (when decaying from B to H)
# 2. sigma_B_V: emits a V photon (when decaying from B to V)
# 3. sigma_H_g: emits an H photon (when decaying from H to g)
# 4. sigma_V_g: emits a V photon (when decaying from V to g)

# We will run a single trajectory and record the jumps.

# We use the same Hamiltonian and collapse operators, but now we use the Monte Carlo solver.
# We want to record which jumps occur at what times.

# Let's run a few trajectories and collect the two-photon events.

# We set the random seed for reproducibility
np.random.seed(0)

# We run one trajectory
mcsolve_result = qt.mcsolve(H0, psi0, tlist, c_ops, [], ntraj=1, options=qt.Options(store_states=True))

# The mcsolve_result does not directly give the jumps, but we can get the states at each time.
# Alternatively, we can use the `mc_fluctuate` function to get the jumps? Actually, QuTiP's mcsolve does not return the jumps by default.
# We can use the `ntraj=1` and `options=qt.Options(store_states=True)` to get the states, but not the jumps.
# To get the jumps, we need to use the `mc_fluctuate` function or handle the trajectory differently.

# Instead, let's use the `photocurrent` method in QuTiP, which is designed for counting photons.

# We define the collapse operators and their corresponding detection efficiencies (here 1.0 for all).
# We use the `mcsolve` with the `photocurrent` method.

# Actually, the `mcsolve` function in QuTiP 4.7 and above has a `options` argument that can specify the method.
# We can set the method to 'photocurrent' and then we get the jumps.

# Let's do:

mcsolve_result = qt.mcsolve(H0, psi0, tlist, c_ops, [], ntraj=1, options=qt.Options(method='photocurrent'))

# Now, mcsolve_result.photocurrent is a list of lists, one for each collapse operator, containing the times of the jumps.

# We have four collapse operators, in the order we defined them in c_ops:
# 0: sigma_B_H (emits an H photon from biexciton decay)
# 1: sigma_B_V (emits a V photon from biexciton decay)
# 2: sigma_H_g (emits an H photon from exciton decay)
# 3: sigma_V_g (emits a V photon from exciton decay)

# Let's extract the jumps for a single trajectory.
jumps = mcsolve_result.photocurrent[0]  # This is a list of lists, one for each trajectory? Actually, for ntraj=1, it's a list of 4 lists.

# We can print the jump times for each operator.
print("Jumps for operator 0 (H from B):", jumps[0])
print("Jumps for operator 1 (V from B):", jumps[1])
print("Jumps for operator 2 (H from H):", jumps[2])
print("Jumps for operator 3 (V from V):", jumps[3])

# Now, we want to look at two-photon events. We note that the biexciton decays in two steps.
# So we look for a jump from operator 0 or 1, followed by a jump from operator 2 or 3, within a short time window.
# The time window is determined by the exciton lifetime (1/gamma).

# We will set a time window of, say, 5/gamma.
window = 5.0 / gamma

# We will loop over the jumps from operator 0 and 1, and then look for a jump from operator 2 or 3 within the window.
# We collect the two-photon events and record the polarizations.

two_photon_events = []

# First, collect all the jumps from the biexciton decay (operator 0 and 1) and sort them by time.
biexciton_jumps = []
for t in jumps[0]:
    biexciton_jumps.append(('H', t))
for t in jumps[1]:
    biexciton_jumps.append(('V', t))

biexciton_jumps.sort(key=lambda x: x[1])

# Now, collect the exciton jumps (operator 2 and 3) and sort them.
exciton_jumps = []
for t in jumps[2]:
    exciton_jumps.append(('H', t))
for t in jumps[3]:
    exciton_jumps.append(('V', t))

exciton_jumps.sort(key=lambda x: x[1])

# Now, for each biexciton jump, look for the next exciton jump within the window.
# We assume that the biexciton jump is the first photon and the exciton jump is the second.
# We also assume that the two jumps are correlated if they come from the same quantum dot. In our simulation, we only have one dot, so any biexciton jump is followed by an exciton jump from the same dot.

# We will match the biexciton jumps to the exciton jumps in order.
# We use two pointers.

i = 0  # pointer for biexciton jumps
j = 0  # pointer for exciton jumps

while i < len(biexciton_jumps) and j < len(exciton_jumps):
    t_b, pol_b = biexciton_jumps[i][1], biexciton_jumps[i][0]
    # Find the next exciton jump after t_b
    while j < len(exciton_jumps) and exciton_jumps[j][1] < t_b:
        j += 1
    if j >= len(exciton_jumps):
        break
    t_e, pol_e = exciton_jumps[j][1], exciton_jumps[j][0]
    if t_e - t_b <= window:
        # Found a two-photon event
        two_photon_events.append((pol_b, pol_e, t_b, t_e))
        i += 1
        j += 1
    else:
        # The biexciton jump does not have a matching exciton jump within the window, so we skip it.
        i += 1

print("Number of two-photon events:", len(two_photon_events))

# Now, we analyze the polarization of the two-photon events.
# We expect that the two photons are entangled in the Bell state |Psi+> = (|HV> + |VH>)/sqrt(2)
# So we should see that the two photons have opposite polarizations.

# Count the combinations:
counts = {'HH':0, 'HV':0, 'VH':0, 'VV':0}
for event in two_photon_events:
    pol_b, pol_e, _, _ = event
    counts[pol_b+pol_e] += 1

print("Two-photon polarization counts:", counts)

# We can also compute the entanglement fidelity relative to the expected Bell state.
# The expected Bell state is (|HV> + |VH>)/sqrt(2).
# We can compute the density matrix of the two-photon state from the events.
# But note: we are only looking at two-photon events, so we are post-selecting.

# We can compute the density matrix by assuming that each two-photon event is a pure state |pol_b, pol_e>.
# Then the density matrix is the average of these states.

# Define the two-photon basis: |HH>, |HV>, |VH>, |VV>
# We create a density matrix of size 4x4.

rho = np.zeros((4,4), dtype=complex)
for event in two_photon_events:
    pol_b, pol_e, _, _ = event
    # Map the polarization to the basis index:
    # 0: HH, 1: HV, 2: VH, 3: VV
    if pol_b == 'H' and pol_e == 'H':
        idx = 0
    elif pol_b == 'H' and pol_e == 'V':
        idx = 1
    elif pol_b == 'V' and pol_e == 'H':
        idx = 2
    else:
        idx = 3
    psi = np.zeros(4)
    psi[idx] = 1.0
    rho += np.outer(psi, psi.conj())

rho /= len(two_photon_events)

# The ideal density matrix for the Bell state |Psi+>
psi_ideal = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
rho_ideal = np.outer(psi_ideal, psi_ideal.conj())

# Compute the fidelity
fidelity = np.trace(np.dot(rho_ideal, rho)).real  # because rho and rho_ideal are real

print("Fidelity to the Bell state |Psi+>:", fidelity)

# We expect the fidelity to be high if the two-photon events are indeed in the entangled state.

# This is a very simple model and simulation. In reality, there are many factors that can reduce the entanglement, such as timing jitter, different decay rates, and spectral distinguishability.

# We will continue to develop more advanced models in subsequent steps.

# Save the results
np.save('two_photon_events.npy', two_photon_events)
np.save('rho.npy', rho)

print("Simulation completed.")
