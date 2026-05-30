import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# =========================================================
# DOMÍNIO NUMÉRICO
# =========================================================

L = 1.0
Nx = 200
dx = L / (Nx - 1)
x = np.linspace(0, L, Nx)

dt = 1e-4
Nt = 2500

snap_times = np.linspace(0, Nt, 5, dtype=int)

# =========================================================
# PERFIL INICIAL
# =========================================================

x0 = 0.3
sigma = 0.05
u0 = np.exp(-((x - x0)**2) / sigma**2)

# =========================================================
# SOLVER OTIMIZADO (VETORIZADO)
# =========================================================

def solve(v, D):

    u = u0.copy()
    snapshots = []

    C = v * dt / dx
    r = D * dt / dx**2

    for n in range(Nt + 1):

        if n in snap_times:
            snapshots.append(u.copy())

        u_new = u.copy()

        # vetorização (remove loop i)
        u_center = u[1:-1]
        u_left = u[:-2]
        u_right = u[2:]

        adv = (
            -0.5 * C * (u_right - u_left)
            + 0.5 * C**2 * (u_right - 2*u_center + u_left)
        )

        diff = r * (u_right - 2*u_center + u_left)

        u_new[1:-1] = u_center + adv + diff

        u = u_new

    return snapshots, u


# =========================================================
# CASOS
# =========================================================

cases = {
    "Advecção dominante": (2.0, 1e-5),
    "Difusão dominante": (0.05, 1e-2),
    "Equilibrado": (1.0, 5e-3)
}

results = {}

for name, (v, D) in cases.items():

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

    plt.savefig(name.lower().replace(" ", "_") + ".png",
                dpi=300, bbox_inches="tight")

    plt.show()


# =========================================================
# COMPARAÇÃO FINAL
# =========================================================

plt.figure(figsize=(10,6))

for name, (_, u_final) in results.items():
    plt.plot(x, u_final, label=name)

plt.title("Comparação final entre regimes")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.legend()
plt.grid()

plt.savefig("comparacao_final.png", dpi=300, bbox_inches="tight")
plt.show()

# =========================================================
# HISTÓRICO (OTIMIZADO PARA ANIMAÇÃO)
# =========================================================

def solve_history(v, D, skip=5):

    u = u0.copy()
    history = []

    C = v * dt / dx
    r = D * dt / dx**2

    for n in range(Nt):

        u_center = u[1:-1]
        u_left = u[:-2]
        u_right = u[2:]

        adv = (
            -0.5 * C * (u_right - u_left)
            + 0.5 * C**2 * (u_right - 2*u_center + u_left)
        )

        diff = r * (u_right - 2*u_center + u_left)

        u_new = u.copy()
        u_new[1:-1] = u_center + adv + diff
        u = u_new

        # guarda apenas alguns frames (CRÍTICO)
        if n % skip == 0:
            history.append(u.copy())

    return np.array(history)


history = solve_history(v=1.0, D=5e-3, skip=5)


# espaço 2D
plt.figure(figsize=(8,5))
plt.imshow(history, aspect='auto', extent=[0,1,0,len(history)*dt*5], origin='lower')
plt.colorbar(label="u(x,t)")
plt.xlabel("x")
plt.ylabel("t")
plt.title("Equilibrado")
plt.savefig("Equilibrado_espaço-tempo.png", dpi=300, bbox_inches="tight")
plt.show()

"""
# Mesh 3D
T = np.arange(len(history)) * dt * 5
X, Tgrid = np.meshgrid(x, T)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Tgrid, history, cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("t")
ax.set_zlabel("u")
plt.savefig("Mesh_3D.png", dpi=300, bbox_inches="tight")
plt.show()

# =========================================================
# ANIMAÇÃO LEVE
# =========================================================

fig, ax = plt.subplots(figsize=(8,5))

line, = ax.plot(x, history[0])

ax.set_xlim(0, 1)
ax.set_ylim(0, 1.1)

ax.set_xlabel("x")
ax.set_ylabel("u")

title = ax.set_title("")

def update(frame):
    line.set_ydata(history[frame])
    title.set_text(f"t = {frame * dt * 5:.4f} s")  # skip=5
    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=len(history),
    interval=15,
    blit=True
)

ani.save(
    "equilibrado_dominante.gif",
    writer="pillow",
    fps=30
)

plt.close()

print("GIF criado com sucesso!")

"""