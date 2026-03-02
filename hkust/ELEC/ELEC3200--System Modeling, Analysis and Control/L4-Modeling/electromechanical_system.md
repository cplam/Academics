# Electromechanical Systems: DC Motor Modeling

## 1. System Schematic and Variables

### DC Motor System Diagram
```
Electrical Side          Mechanical Side
     ↓                           ↓
   ┌───┐                       ┌───┐
   │ R │ Armature              │ J │ Load Inertia
Va ┼─/\/\/─┐                   ├───┤
   │      │ iₐ(t)              │   │ θ(t), ω(t)
   │ L    ├───→                │   │ (angular position/velocity)
   │      │                    │ Kf│ Friction
   └──────┘ Back EMF: Vb = Kω  └───┘ Torque: τ = Kiₐ
        ↑                           ↑
        └───────── Coupling ────────┘
               K = Kₜ = K_b
```

### Variables and Parameters
| Symbol | Meaning | Units |
|--------|---------|-------|
| \( v_a(t) \) | Armature voltage (input) | V |
| \( i_a(t) \) | Armature current | A |
| \( v_b(t) \) | Back EMF voltage | V |
| \( θ(t) \) | Angular position | rad |
| \( ω(t) \) | Angular velocity (ω = dθ/dt) | rad/s |
| \( τ_m(t) \) | Motor torque | N·m |
| \( R_a \) | Armature resistance | Ω |
| \( L_a \) | Armature inductance | H |
| \( J \) | Moment of inertia | kg·m² |
| \( K_f \) | Friction coefficient | N·m·s/rad |
| \( K \) | Motor constant (K_t = K_b) | N·m/A or V·s/rad |

---

## 2. Fundamental Physical Laws

### Electrical Side: Kirchhoff's Voltage Law (KVL)
\[
v_a(t) = R_a i_a(t) + L_a \frac{di_a(t)}{dt} + v_b(t)
\]

### Back EMF Relationship
\[
v_b(t) = K \omega(t) = K \frac{d\theta(t)}{dt}
\]

### Mechanical Side: Newton's Second Law (Rotational)
\[
J \frac{d\omega(t)}{dt} = τ_m(t) - τ_f(t)
\]
where:
- Motor torque: \( τ_m(t) = K i_a(t) \)
- Friction torque: \( τ_f(t) = K_f \omega(t) \)

---

## 3. Two Modeling Cases

### Case 1: Position Control
**Output**: Angular position \( θ(t) \)

#### Differential Equations:
\[
L_a \frac{di_a}{dt} + R_a i_a + K \frac{dθ}{dt} = v_a \quad \text{(Electrical)}
\]
\[
J \frac{d^2θ}{dt^2} + K_f \frac{dθ}{dt} = K i_a \quad \text{(Mechanical)}
\]

#### State-Space Representation (3 states):
States: \( x_1 = i_a \), \( x_2 = θ \), \( x_3 = ω = \dot{θ} \)

\[
\begin{bmatrix}
\dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3
\end{bmatrix}
=
\begin{bmatrix}
-R_a/L_a & 0 & -K/L_a \\
0 & 0 & 1 \\
K/J & 0 & -K_f/J
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix}
+
\begin{bmatrix}
1/L_a \\ 0 \\ 0
\end{bmatrix}
v_a
\]
\[
y = \begin{bmatrix} 0 & 1 & 0 \end{bmatrix} \mathbf{x}
\]

---

### Case 2: Speed Control
**Output**: Angular velocity \( ω(t) \)

#### Differential Equations:
\[
L_a \frac{di_a}{dt} + R_a i_a + K ω = v_a
\]
\[
J \frac{dω}{dt} + K_f ω = K i_a
\]

#### State-Space Representation (2 states):
States: \( x_1 = i_a \), \( x_2 = ω \)

\[
\begin{bmatrix}
\dot{x}_1 \\ \dot{x}_2
\end{bmatrix}
=
\begin{bmatrix}
-R_a/L_a & -K/L_a \\
K/J & -K_f/J
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2
\end{bmatrix}
+
\begin{bmatrix}
1/L_a \\ 0
\end{bmatrix}
v_a
\]
\[
y = \begin{bmatrix} 0 & 1 \end{bmatrix} \mathbf{x}
\]

---

## 4. Energy Conversion Relationships

### Key Relationships:
1. **Electrical → Mechanical Power**:
   \[
   P_{\text{electrical}} = v_b i_a = K ω i_a
   \]
   \[
   P_{\text{mechanical}} = τ_m ω = K i_a ω
   \]
   ∴ \( K_t = K_b = K \) (from energy conservation)

2. **Torque Production**:
   \[
   τ_m(t) = K i_a(t)
   \]

3. **Back EMF Generation**:
   \[
   v_b(t) = K ω(t)
   \]

---

## 5. Transfer Functions

### Position Control Transfer Function:
\[
\frac{Θ(s)}{V_a(s)} = \frac{K}{s[(L_a s + R_a)(J s + K_f) + K^2]}
\]

### Speed Control Transfer Function:
\[
\frac{Ω(s)}{V_a(s)} = \frac{K}{(L_a s + R_a)(J s + K_f) + K^2}
\]

### Simplified (if \( L_a ≈ 0 \), common approximation):
\[
\frac{Ω(s)}{V_a(s)} = \frac{K/R_a}{J s + (K_f + K^2/R_a)}
\]

---

## 6. Block Diagram Representation

### Speed Control Block Diagram:
```
V_a(s) → [1/(L_a s + R_a)] → I_a(s) → [K] → τ_m(s)
                                           ↓
        v_b(s) ← [K] ← ω(s) ← [1/(J s + K_f)] ←
```

### Signal Flow:
1. Voltage \( v_a \) drives current \( i_a \) through armature impedance
2. Current produces torque \( τ_m = K i_a \)
3. Torque accelerates load: \( J\dot{ω} = τ_m - K_f ω \)
4. Rotation generates back EMF: \( v_b = K ω \)
5. Back EMF opposes applied voltage: \( v_a = R_a i_a + L_a di_a/dt + v_b \)

---

## 7. Important Notes for Problem Solving

### 1. **Sign Convention**
- Motor torque: positive when accelerating in positive direction
- Back EMF: always opposes applied voltage
- Friction: always opposes motion

### 2. **Common Simplifications**
- Often neglect inductance: \( L_a ≈ 0 \) (electrical dynamics faster than mechanical)
- Sometimes neglect friction: \( K_f ≈ 0 \)

### 3. **DC Gain (Steady-State)**
For speed control:
\[
ω_{ss} = \frac{K}{R_a K_f + K^2} v_a
\]
For position control (with integral action):
\[
θ_{ss} = ∞ \quad \text{(integrator behavior)}
\]

### 4. **Time Constants**
Electrical time constant: \( τ_e = L_a/R_a \)
Mechanical time constant: \( τ_m = J/(K_f + K^2/R_a) \)

---

## 8. Memory Aids

### 1. **KVL for Armature Circuit**:
```
v_a = iR + L di/dt + back_emf
```

### 2. **Torque Equation**:
```
J dω/dt = motor_torque - friction_torque
       = K·i - K_f·ω
```

### 3. **Coupling Relationships**:
```
Electrical ←[K]→ Mechanical
i →[K]→ torque
ω →[K]→ back_emf
```

### 4. **Energy Conservation**:
```
Electrical power = Mechanical power
v_b·i = τ·ω
Kω·i = Ki·ω  ⇒ K_t = K_b
```

---

## 9. Typical Exam Questions

### Type 1: Derive equations from schematic
1. Write KVL for electrical loop
2. Write Newton's law for mechanical side
3. Substitute coupling equations
4. Convert to state-space form

### Type 2: Find transfer function
1. Take Laplace transform of equations
2. Eliminate intermediate variables (i_a)
3. Find ratio Y(s)/U(s)

### Type 3: Design controller
1. Determine system type (position = type 1, speed = type 0)
2. Use pole placement or other methods
3. Consider back EMF effects

---

**Core Concept**: DC motor is a **two-domain system** where electrical and mechanical domains couple through:
1. **Motor action**: current → torque (\( τ = K i \))
2. **Generator action**: speed → back EMF (\( v_b = K ω \))

This bidirectional coupling is what makes electromechanical systems interesting and challenging to control.