# 2×2 Matrix Chain Multiplication Calculator (SD Mode)

## Program Code
```
ClrStat: ?→A: ?→B: ?→C: ?→D: Lbl 1: ?→X: ?→Y: ?→M: X,Y;M DT: ?→X: AmaxX+Bn→Y◢ AmaxY+BX→M◢ Y→A: M→B: CmaxX+Dn→Y◢ CmaxY+DX→M◢ Y→C: M→D: ClrStat: Goto 1
```

## Important: Run in SD Mode
This program **must be run in SD (Single-variable statistics) mode** because:
1. Uses `DT` command to store data points
2. Uses `n` variable (number of data points in statistics memory)
3. Uses `max` as multiplication operator (alternative to `×`)
4. Uses statistics memory for intermediate calculations

**To switch to SD mode:** Press `MODE` → `4` (SD)

## How to Use

### **Step 1: Initialize First Matrix**
```
Input: A [EXE]  (a₁₁ of first matrix)
Input: B [EXE]  (a₁₂ of first matrix)
Input: C [EXE]  (a₂₁ of first matrix)
Input: D [EXE]  (a₂₂ of first matrix)
```

### **Step 2: Input Next Matrix**
For each additional matrix:
```
Input: X [EXE]  (b₁₁)
Input: Y [EXE]  (b₁₂)
Input: M [EXE]  (b₂₁)
Now press: X,Y;M DT  (Stores in statistics)
Input: X [EXE]  (b₂₂) - this overwrites previous X!
```

**Outputs after entering b₂₂:**
```
1: c₁₁ = a₁₁×b₁₁ + a₁₂×b₂₁
2: c₁₂ = a₁₁×b₁₂ + a₁₂×b₂₂
3: c₂₁ = a₂₁×b₁₁ + a₂₂×b₂₁  
4: c₂₂ = a₂₁×b₁₂ + a₂₂×b₂₂
```

**The result automatically becomes the new A,B,C,D for next multiplication.**

## Detailed Example

### **Example: Multiply [1 2; 3 4] × [5 6; 7 8]**

**Step 1: Initialize first matrix**
```
Input: 1 [EXE]  → A = 1
Input: 2 [EXE]  → B = 2
Input: 3 [EXE]  → C = 3  
Input: 4 [EXE]  → D = 4
```

**Step 2: Input second matrix**
```
Input: 5 [EXE]  → X = 5 (b₁₁)
Input: 6 [EXE]  → Y = 6 (b₁₂)
Input: 7 [EXE]  → M = 7 (b₂₁)

Now the calculator shows: 5,6;7

Press: DT  (stores 5,6;7 in statistics)

Input: 8 [EXE]  → X = 8 (b₂₂, overwrites previous X=5)

Outputs appear:
1: 1×5 + 2×7 = 19  (displays: 19)
2: 1×6 + 2×8 = 22  (displays: 22) 
3: 3×5 + 4×7 = 43  (displays: 43)
4: 3×6 + 4×8 = 50  (displays: 50)
```

**Result:** `[19 22; 43 50]`

**The program automatically:**
- Stores 19→A, 22→B, 43→C, 50→D
- Clears statistics memory (`ClrStat`)
- Returns to Lbl 1 for next multiplication

## Variables Explanation

### **Input Variables:**
- **A, B, C, D**: Current matrix `[A B; C D]`
- **X, Y, M**: Elements of next matrix being entered
- **n**: Statistics variable = number of data points (always 1 here)

### **Statistics Trick:**
`X,Y;M DT` stores a data point where:
- `X` = x-value (but gets overwritten!)
- `Y` = y-value (b₁₂)
- `M` = frequency (b₂₁)

After `DT`, `n=1` in statistics memory.

## Complete Walkthrough Example

### **Chain: [1 0; 0 1] × [2 0; 0 3] × [4 1; 1 4]**

```
Step 1: Initialize identity matrix
A=1, B=0, C=0, D=1

Step 2: Input [2 0; 0 3]
Input: 2 [EXE]  (X=b₁₁)
Input: 0 [EXE]  (Y=b₁₂)  
Input: 0 [EXE]  (M=b₂₁)
Press: DT
Input: 3 [EXE]  (X=b₂₂)

Outputs:
1: 2  (1×2 + 0×0 = 2)
2: 0  (1×0 + 0×3 = 0)
3: 0  (0×2 + 1×0 = 0)
4: 3  (0×0 + 1×3 = 3)

Now A=2, B=0, C=0, D=3

Step 3: Input [4 1; 1 4]
Input: 4 [EXE]  (X=b₁₁)
Input: 1 [EXE]  (Y=b₁₂)
Input: 1 [EXE]  (M=b₂₁)
Press: DT
Input: 4 [EXE]  (X=b₂₂)

Outputs:
1: 8  (2×4 + 0×1 = 8)
2: 2  (2×1 + 0×4 = 2)
3: 3  (0×4 + 3×1 = 3)
4: 12 (0×1 + 3×4 = 12)

Final: [8 2; 3 12]
```

## Key Features

### **1. Memory Efficient**
- Uses only 7 variables (A,B,C,D,X,Y,M)
- Reuses variables cleverly
- Statistics memory for temporary storage

### **2. Automatic Chain**
- Result becomes new matrix automatically
- No need to manually store results
- Continuous operation possible

### **3. SD Mode Benefits**
- `n` variable always available
- `DT` command for quick storage
- Statistics functions available if needed

## Special Notes

### **Important:**
- Must be in **SD mode** before running
- `max` means multiplication (Casio syntax)
- `n` is statistics counter (should be 1)
- `ClrStat` clears statistics after each multiplication

### **Sequence is Critical:**
1. Enter b₁₁, b₁₂, b₂₁
2. Press `DT` 
3. Enter b₂₂
4. Get all 4 outputs

### **If You Make a Mistake:**
Press `AC` to clear and restart from beginning.

## Applications

### **1. Transformation Chains**
- Computer graphics: rotate, scale, translate
- Physics: coordinate system transformations
- Engineering: stress/strain transformations

### **2. Quantum Mechanics**
- Spin operator combinations
- Quantum gate sequences
- State vector transformations

### **3. Linear Algebra**
- Matrix powers (M × M × M...)
- Similarity transformations
- Eigenvalue decompositions

## Matrix Math Reference

Given: `M1 = [A B; C D]` and `M2 = [X₁ Y; M X₂]` (note: X changes!)

Multiplication: `M1 × M2 = [P Q; R S]`

Where:
```
P = A×X₁ + B×M
Q = A×Y + B×X₂
R = C×X₁ + D×M  
S = C×Y + D×X₂
```

## Quick Test Example

**Test: Identity × Anything = Same**
```
Initialize: A=1, B=0, C=0, D=1
Input second: X=5, Y=6, M=7, DT, X=8
Outputs: 5, 6, 7, 8 ✓
```

This program is perfect for rapid 2×2 matrix chain calculations in physics, engineering, and computer graphics applications where multiple transformations are applied sequentially.