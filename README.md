# Advection–Diffusion Equation Simulation

Este repositório contém a simulação numérica da equação de advecção–difusão unidimensional utilizando métodos de diferenças finitas.

O objetivo é estudar a evolução de um perfil Gaussiano em diferentes regimes físicos e comparar esquemas numéricos.

---

## Objetivos

- Resolver numericamente a equação de advecção–difusão 1D
- Analisar regimes físicos diferentes:
  - Advecção dominante
  - Difusão dominante
  - Regime equilibrado
- Estudar o número de Péclet
- Comparar esquemas:
  - Upwind
  - Lax–Wendroff
- Avaliar estabilidade e difusão numérica
- Gerar gráficos 1D, 2D, 3D e animações

---

## Equação governante

$$
\frac{\partial u}{\partial t} + v \frac{\partial u}{\partial x} = D \frac{\partial^2 u}{\partial x^2}
$$

Onde:
- $u(x,t)$ → variável transportada  
- $v$ → velocidade de advecção  
- $D$ → coeficiente de difusão  

---

## Parâmetros adimensionais

$$
C = \frac{v \Delta t}{\Delta x}
$$

$$
r = \frac{D \Delta t}{(\Delta x)^2}
$$

$$
Pe = \frac{vL}{D}
$$

---

## Estrutura do repositório
```
MFE--equacao-de-adveccao-difusao/
│
├── main.py  
├── README.md  
│
├── 1D graphics/
├── 2D graphics/
├── 3D graphics/
├── animations/
```


---

## Métodos numéricos

### 🔹 Upwind
Método robusto, mas introduz difusão numérica artificial.

### 🔹 Lax–Wendroff
Método de segunda ordem mais preciso, reduzindo a difusão numérica.

---

## Regimes estudados

| Regime | v | D | Pe |
|--------|---|---|----|
| Advecção dominante | 2.0 | 1e-5 | 200000 |
| Equilibrado | 1.0 | 5e-3 | 200 |
| Difusão dominante | 0.05 | 1e-2 | 5 |

---

## Animações

As animações da evolução temporal podem ser encontradas na pasta:
```
MFE--equacao-de-adveccao-difusao/
│
├── animations/
```

Exemplos:
- Advecção dominante
- Difusão dominante
- Regime equilibrado

---

## Resultados

O projeto permite observar:

- Transporte de perfis Gaussianos
- Espalhamento por difusão
- Dissipação numérica em esquemas discretos
- Influência direta do número de Péclet

---

## Conclusões

- O número de Péclet controla o regime físico dominante
- Upwind é estável mas difusivo
- Lax–Wendroff melhora significativamente a precisão
- A escolha do esquema numérico influencia fortemente a solução

---

## 👨‍💻 Autores

Tiago Bernardo - 53117  
Gabriel Marques - 53087
