
import glob
import re
import matplotlib.pyplot as plt

a = []
energy = []

for file in glob.glob("fe_bcc_a*.out"):
    match = re.search(r"a(\d+)\.out$", file)
    if not match:
        continue

    lattice = int(match.group(1)) / 100

    with open(file) as f:
        content = f.read()

    if "JOB DONE" not in content:
        print("Skipped incomplete:", file)
        continue

    values = re.findall(
        r"!\s+total energy\s+=\s+([-\d.]+)",
        content
    )

    if values:
        a.append(lattice)
        energy.append(float(values[-1]))

data = sorted(zip(a, energy))

if not data:
    raise ValueError("No completed energy calculations found")

a, energy = zip(*data)

for x, y in data:
    print(f"a = {x:.2f} Angstrom, E = {y:.8f} Ry")

plt.plot(a, energy, "o-", color="blue")
plt.xlabel("Lattice Parameter (Angstrom)")
plt.ylabel("Total Energy (Ry)")
plt.title("DFT Study of BCC Iron")
plt.grid(True)
plt.tight_layout()
plt.savefig("fe_energy_vs_lattice.png", dpi=300)

print("Updated graph saved successfully!")
