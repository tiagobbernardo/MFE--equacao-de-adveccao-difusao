# 🌊 Advection–Diffusion Equation Simulation

Este repositório contém a simulação numérica da equação de advecção–difusão unidimensional utilizando métodos de diferenças finitas.

O objetivo principal é estudar a evolução de um perfil inicial Gaussiano sob diferentes regimes físicos, caracterizados pelo número de Péclet, e comparar diferentes esquemas numéricos.

---

## 📌 Objetivos do projeto

- Resolver numericamente a equação de advecção–difusão 1D
- Analisar três regimes físicos:
  - Advecção dominante
  - Difusão dominante
  - Regime equilibrado
- Estudar o efeito do número de Péclet
- Comparar esquemas numéricos:
  - Upwind
  - Lax–Wendroff
- Avaliar estabilidade e difusão numérica
- Gerar gráficos 1D, 2D, 3D e animações (GIF)

---

## 🧮 Equação governante

\[
\frac{\partial u}{\partial t}
+
v \frac{\partial u}{\partial x}
=
D \frac{\partial^2 u}{\partial x^2}
\]

Onde:
- \(u(x,t)\): variável transportada  
- \(v\): velocidade de advecção  
- \(D\): coeficiente de difusão  

---

## 📊 Parâmetros adimensionais

- Número de Courant:
\[
C = \frac{v \Delta t}{\Delta x}
\]

- Parâmetro difusivo:
\[
r = \frac{D \Delta t}{(\Delta x)^2}
\]

- Número de Péclet:
\[
Pe = \frac{vL}{D}
\]

---

## 📁 Estrutura do repositório
'''
adadadadad
adadadadasdfe
'''


---

## ⚙️ Métodos numéricos

### 🔹 Upwind
Método robusto, mas introduz difusão numérica artificial.

### 🔹 Lax–Wendroff
Método de segunda ordem mais preciso, reduzindo a difusão numérica.

---

## 📌 Regimes estudados

| Regime | v | D | Pe |
|--------|---|---|----|
| Advecção dominante | 2.0 | 1e-5 | 200000 |
| Equilibrado | 1.0 | 5e-3 | 200 |
| Difusão dominante | 0.05 | 1e-2 | 5 |

---

## 🎞️ Animações

As animações da evolução temporal podem ser encontradas na pasta:
'''
/animations
'''

Exemplos:
- Advecção dominante
- Difusão dominante
- Regime equilibrado

---

## 📈 Resultados

O projeto permite observar:

- Transporte de perfis Gaussianos
- Espalhamento por difusão
- Dissipação numérica em esquemas discretos
- Influência direta do número de Péclet

---

## 🧠 Conclusões

- O número de Péclet controla o regime físico dominante
- Upwind é estável mas difusivo
- Lax–Wendroff melhora significativamente a precisão
- A escolha do esquema numérico influencia fortemente a solução

---

## 🚀 Possíveis melhorias futuras

- Extensão para 2D/3D completo
- Implementação de esquemas implícitos
- Análise de erro quantitativo
- Implementação de condições de fronteira não homogéneas

---

## 👨‍💻 Autor

Tiago Bernardo  
Gabriel Marques  

Projeto académico – Equação de Advecção–Difusão (Física/Engenharia)