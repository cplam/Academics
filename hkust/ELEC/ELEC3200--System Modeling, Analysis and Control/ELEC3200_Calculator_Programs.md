# ELEC3200 Calculator Programs (Rough Table)

This document provides the calculator program codes for **ELEC3200**, along with detailed instructions on how to input the program into standard scientific calculators (e.g., Casio fx-50FH / fx-50FH II) and simple verification examples.

---

## Overview

- **Course**: ELEC3200
- **Topic**: Rough Table Computation
- **Program Versions**:
  - **Version 1**: $\deg(ap+bq) = \{2, 3\}$ (54 bytes)
  - **Version 2**: $\deg(ap+bq) = \{4, 5\}$ (168 bytes)

---

## Version 1: $\deg(ap+bq) = \{2, 3\}$ (54 Bytes)

### 1. Program Code
```text
?→A: ?→B: ?→C: ?→D: A◢ C◢ B◢ D◢ B≠0 => B⁻¹(BC-AD→B◢ 0◢ B=0 => 0→D: D◢ 0
```

> **Note on Symbols:**
> - `?` : Input prompt (`SHIFT` + `3` [PROG] $\rightarrow$ `?`)
> - `→` : Memory assignment / Arrow (`→` key)
> - `◢` : Display symbol / Output pause (`SHIFT` + `3` [PROG] $\rightarrow$ `◢`)
> - `=>` : Jump conditional (`SHIFT` + `3` [PROG] $\rightarrow$ `=>`)
> - `≠` : Relational operator (`SHIFT` + `3` [PROG] $\rightarrow$ `≠`)
> - `=` : Relational operator (`SHIFT` + `3` [PROG] $\rightarrow$ `=`)

---

### 2. How to Input (Key Sequence Guide)

1. **Enter Program Edit Mode**:
   - Press `MODE` $\rightarrow$ `PROG` (or `MODE 6` depending on your model).
   - Select an available program slot (e.g., `P1`).
2. **Type the Code**:
   - Use `ALPHA` + key to type variables `A`, `B`, `C`, `D`.
   - Use `SHIFT` + `PROG` (or `PRGM`) to access special control commands (`?`, `→`, `◢`, `=>`, `≠`, `=`).
3. **Save and Exit**:
   - Press `EXIT` or `AC` once complete.

---

### 3. Execution & Input Instructions

To run the program:
1. Press `MODE 1` (COMP Mode).
2. Press `EXE` or select the program slot (e.g., `Prog 1`).
3. The calculator will prompt for parameters step-by-step:
   - `A?` $\rightarrow$ Enter value of $A$, press `EXE`
   - `B?` $\rightarrow$ Enter value of $B$, press `EXE`
   - `C?` $\rightarrow$ Enter value of $C$, press `EXE`
   - `D?` $\rightarrow$ Enter value of $D$, press `EXE`
4. Press `EXE` to cycle through the output displays (indicated by `◢`).

---

### 4. Simple Example & Verification

#### Verification Example
Given initial values:
- $A = 2$
- $B = 4$
- $C = 6$
- $D = 10$

**Expected Step-by-Step Outputs**:
1. **Initial Displays**:
   - Outputs $A = 2$
   - Outputs $C = 6$
   - Outputs $B = 4$
   - Outputs $D = 10$
2. **Calculated Rough Table Value**:
   - Since $B \neq 0$ ($4 \neq 0$):
     $$\text{New } B = B^{-1}(BC - AD) = \frac{1}{4}(4 \times 6 - 2 \times 10) = \frac{1}{4}(24 - 20) = 1$$
   - Output display: `1`
   - Followed by output display: `0`

---

## Version 2: $\deg(ap+bq) = \{4, 5\}$ (168 Bytes)

### 1. Mode Setup
- **Required Mode**: Linear Regression Mode (`Mode 5 1` or `STAT` $\rightarrow$ `A+BX` / `Line`)

---

### 2. Program Code
```text
ClrStat: ?→A: ?→B: ?→C: A, B; C DT: ?→A: ?→B: ?→C: maxX◢ n◢ B◢ maxY◢ A◢ C◢ maxY→D: D≠0 => D⁻¹(n maxY - A maxX → D: D◢ maxY→X: X≠0 => X⁻¹(B maxY - C maxX → X: X◢ 0◢ D→Y: Y≠0 => Y⁻¹(AD - X maxY → Y: Y◢ D→M: M≠0 => C→M: M◢ 0◢ Y→A: A≠0 => A⁻¹(XY - DM → A: A◢ 0◢ 0◢ A→B: A≠0 => M→B: B◢ 0◢ 0
```

---

### 3. How to Input

1. Ensure the program is saved while in **Linear Regression Mode** (`Mode 5 1`).
2. Use STAT commands:
   - `ClrStat`: Clears statistical memory (`SHIFT` + `STAT` $\rightarrow$ `Clear`).
   - `DT`: Data input key (`,` and `DT`).
   - `maxX`, `maxY`, `n`: Statistical summary variables found in `SHIFT` + `STAT` (or `S-SUM` / `S-VAR`).
3. Enter operators (`=>`, `≠`, `→`, `◢`) via the `PROG` menu.

---

### 4. Input Procedure

When executing the program:
1. **First Dataset Entry**:
   - Prompt `A?` $\rightarrow$ Enter $A_1$, press `EXE`
   - Prompt `B?` $\rightarrow$ Enter $B_1$, press `EXE`
   - Prompt `C?` $\rightarrow$ Enter $C_1$, press `EXE`
   - (The program stores $A_1, B_1$ and registers $C_1$ as data point via `DT`)
2. **Second Dataset Entry**:
   - Prompt `A?` $\rightarrow$ Enter $A_2$, press `EXE`
   - Prompt `B?` $\rightarrow$ Enter $B_2$, press `EXE`
   - Prompt `C?` $\rightarrow$ Enter $C_2$, press `EXE`
3. Press `EXE` repeatedly to view all intermediate outputs and calculated elements of the Rough Table.

---

### 5. Verification Table (Rough Table Structure)

The program computes and steps through the array elements for higher degree system stability analysis:

| Degree / Row | Column 1 | Column 2 | Column 3 |
| :--- | :--- | :--- | :--- |
| **Row 1** | $A_1$ | $B_1$ | $C_1$ |
| **Row 2** | $A_2$ | $B_2$ | $C_2$ |
| **Row 3 (Computed)** | $\text{maxX}$, $n$, $B$ | $\text{maxY}$, $A$, $C$ | $D = D^{-1}(n \cdot \text{maxY} - A \cdot \text{maxX})$ |
| **Row 4 (Computed)** | $X = X^{-1}(B \cdot \text{maxY} - C \cdot \text{maxX})$ | $Y = Y^{-1}(AD - X \cdot \text{maxY})$ | $M = C \text{ (if } M \neq 0\text{)}$ |
| **Row 5 (Computed)** | $A = A^{-1}(XY - DM)$ | $B = M \text{ (if } A \neq 0\text{)}$ | $0$ |

---

## Quick Reference Summary

| Feature | Version 1 | Version 2 |
| :--- | :--- | :--- |
| **Degree Range** | $\deg(ap+bq) = \{2, 3\}$ | $\deg(ap+bq) = \{4, 5\}$ |
| **Memory Size** | 54 Bytes | 168 Bytes |
| **Calculator Mode** | `MODE 1` (COMP) | `MODE 5 1` (Linear Regression) |
| **Primary Output** | $B^{-1}(BC - AD)$ | Full multi-row Routh/Rough table coefficients |
