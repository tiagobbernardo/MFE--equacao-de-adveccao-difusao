# Equação de Advecção–Difusão

Projeto desenvolvido no âmbito da unidade curricular de Modelação em Física e Engenharia, com o objetivo de estudar numericamente a equação de advecção–difusão unidimensional através de métodos de diferenças finitas.

## Objetivos

- Simular numericamente a equação de advecção–difusão;
- Analisar diferentes regimes físicos:
  - Advecção dominante;
  - Difusão dominante;
  - Regime equilibrado;
- Comparar diferentes esquemas numéricos;
- Estudar estabilidade numérica e difusão numérica artificial.

---

## Equação estudada

A equação considerada é:

```math
\frac{\partial u}{\partial t}
+
v\frac{\partial u}{\partial x}
=
D\frac{\partial^2u}{\partial x^2}
```

onde:

- \(u(x,t)\) representa a quantidade transportada;
- \(v\) é a velocidade de advecção;
- \(D\) é o coeficiente de difusão.

---

## Métodos Numéricos

O projeto utiliza:

- Método de Euler explícito para discretização temporal;
- Diferenças centradas para o termo difusivo;
- Esquema de Lax–Wendroff para o termo advectivo.

Inicialmente foi utilizado o esquema upwind, mas este introduzia difusão numérica significativa em regimes dominados pela advecção. O método de Lax–Wendroff permitiu melhorar a preservação da amplitude e forma do perfil Gaussiano.

---

## Estrutura do Projeto

```text
.
├── main.py
├── README.md
├── Relatorio/
│   └── relatorio.tex
├── Graficos/
│   ├── adveccao_dominante.png
│   ├── difusao_dominante.png
│   ├── equilibrado.png
│   └── comparacao_final.png
```

---

## Resultados

As simulações permitem observar:

- Transporte do perfil Gaussiano em regimes advectivos;
- Espalhamento progressivo em regimes difusivos;
- Competição entre advecção e difusão em regimes equilibrados;
- Influência da difusão numérica nos diferentes métodos.

---

## Tecnologias Utilizadas

- Python
- NumPy
- Matplotlib

---

## Autores

- Tiago Bernardo
- Gabriel Marques