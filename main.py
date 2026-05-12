import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# DOMÍNIO NUMÉRICO (fixo para todos os casos)
# =========================================================

L = 1.0
Nx = 200
dx = L / (Nx - 1)
x = np.linspace(0, L, Nx)

dt = 1e-4
Nt = 2500

# tempos para guardar solução
snap_times = np.linspace(0, Nt, 5, dtype=int)

# =========================================================
# PERFIL INICIAL (fixo)
# =========================================================

x0 = 0.3
sigma = 0.05
u0 = np.exp(-((x - x0)**2) / sigma**2)

# =========================================================
# SOLVER (upwind + difusão)
# =========================================================

def solve(v, D):

    u = u0.copy()
    snapshots = []

    for n in range(Nt + 1):

        if n in snap_times:
            snapshots.append(u.copy())

        u_new = u.copy()

        for i in range(1, Nx - 1):

            adv = -v * dt / dx * (u[i] - u[i - 1])

            diff = D * dt / dx**2 * (u[i + 1] - 2*u[i] + u[i - 1])

            u_new[i] = u[i] + adv + diff

        u = u_new

    return snapshots, u

cases = {
    "Advecção dominante": (2.0, 1e-5),
    "Difusão dominante": (0.1, 1e-3),
    "Equilibrado": (1.0, 5e-3)
}

results = {}

results = {}

for name, (v, D) in cases.items():

    # calcular números adimensionais
    C = v * dt / dx
    r = D * dt / dx**2

    print(f"\n{name}")
    print(f"C (Courant) = {C:.6f}")
    print(f"r (difusão) = {r:.6f}")

    snapshots, u_final = solve(v, D)
    results[name] = (snapshots, u_final)

    plt.figure(figsize=(8,5))

    for i, snap in enumerate(snapshots):
        plt.plot(x, snap, label=f"t={snap_times[i]*dt:.4f}")

    plt.title(name)
    plt.xlabel("x")
    plt.ylabel("u(x,t)")
    plt.legend()
    plt.grid()

    # 💾 guardar ficheiro
    filename = name.lower().replace(" ", "_") + ".png"
    plt.savefig(filename, dpi=300, bbox_inches="tight")

    plt.show()

plt.figure(figsize=(10,6))

for name, (_, u_final) in results.items():
    plt.plot(x, u_final, label=name)

plt.title("Comparação final entre regimes")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.legend()
plt.grid()

# 💾 guardar gráfico final
plt.savefig("comparacao_final.png", dpi=300, bbox_inches="tight")

plt.show()

print("run completed")