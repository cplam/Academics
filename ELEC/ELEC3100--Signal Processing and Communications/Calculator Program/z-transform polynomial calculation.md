# Polynomial and Z-Transform Calculator Program

## Program Code
```
?→M: ?→A: ?→B: ?→C: ?→D: ?→X: ?→Y: 
M=3=> Goto 1: 
M=-2=> Goto 2: 
M=-1=> Goto 3: 
AD◢ 
AX+BD◢ 
If M=1: Then 
  BX◢ 
  AY+CD◢ 
Else 
  AY+BX+CD◢ 
IfEnd: 
BY+CX◢ 
CY◢ 
0-1: 
Lbl 1: 
ACX◢ 
ACY+ADX+BCX◢ 
ADY+BCY+BDX◢ 
BDY◢ 
0-1: 
Lbl 2: 
?→M: 
AX-1→A◢ 
X-1(B-AY→B◢ 
C-AM-BY→C◢ 
D-MB◢ 
0-1: 
Lbl 3: 
?→M: 
AY-1→A◢ 
Y-1(B-MA→B◢ 
Y-1(C-MB→C◢ 
Y-1(D-MC→D◢ 
X-MD
```

## Overview
This Casio calculator program performs various polynomial operations and can be adapted for Z-transform calculations by substituting x = z⁻¹. The operation type is selected by the initial value of `M`.

## Operations

### 1. **M = 1: Multiply Two Bivariate Linear Polynomials**
**Format:** `(Ax + By + C)(Dx + Xy + Y)`

**Input Variables:**
- A = x coefficient in first factor
- B = y coefficient in first factor
- C = constant in first factor
- D = x coefficient in second factor
- X = y coefficient in second factor
- Y = constant in second factor

**Output Order:**
1. x² coefficient: AD
2. xy coefficient: AX + BD
3. y² coefficient: BX
4. x coefficient: AY + CD
5. y coefficient: BY + CX
6. constant: CY

**Example:** `(3x + 2y + 5)(2x + 3y + 1)`
```
Input: M=1, A=3, B=2, C=5, D=2, X=3, Y=1
Output: 6, 13, 6, 13, 17, 5
Result: 6x² + 13xy + 6y² + 13x + 17y + 5
```

### 2. **M = 2: Multiply Two Quadratic Polynomials**
**Format:** `(Ax² + Bx + C)(Dx² + Xx + Y)`

**Input Variables:**
- A = x² coefficient in first factor
- B = x coefficient in first factor
- C = constant in first factor
- D = x² coefficient in second factor
- X = x coefficient in second factor
- Y = constant in second factor

**Output Order:**
1. x⁴ coefficient: AD
2. x³ coefficient: AX + BD
3. x² coefficient: AY + BX + CD
4. x coefficient: BY + CX
5. constant: CY

**Example:** `(4x² + 5x + 6)(7x² + 9x + 10)`
```
Input: M=2, A=4, B=5, C=6, D=7, X=9, Y=10
Output: 28, 71, 127, 104, 60
Result: 28x⁴ + 71x³ + 127x² + 104x + 60
```

### 3. **M = 3: Multiply Three Linear Polynomials**
**Format:** `(Ax + B)(Cx + D)(Xx + Y)`

**Input Variables:**
- A = x coefficient in first factor
- B = constant in first factor
- C = x coefficient in second factor
- D = constant in second factor
- X = x coefficient in third factor
- Y = constant in third factor

**Output Order:**
1. x³ coefficient: ACX
2. x² coefficient: ACY + ADX + BCX
3. x coefficient: ADY + BCY + BDX
4. constant: BDY

**Example:** `(2x + 1)(3x + 1)(100x + 4)`
```
Input: M=3, A=2, B=1, C=3, D=1, X=100, Y=4
Output: 600, 524, 120, 4
Result: 600x³ + 524x² + 120x + 4
```

### 4. **M = -1: Polynomial Division (Degree 4 ÷ Degree 1)**
**Format:** `(Ax⁴ + Bx³ + Cx² + Dx + X) ÷ (Yx + M)`

**Input Variables:**
- A = x⁴ coefficient
- B = x³ coefficient
- C = x² coefficient
- D = x coefficient
- X = constant term
- Y = divisor x coefficient
- Program prompts for new M = divisor constant term

**Output Order:**
1. Quotient x³ coefficient: AY⁻¹
2. Quotient x² coefficient: Y⁻¹(B - MA)
3. Quotient x coefficient: Y⁻¹(C - MB)
4. Quotient constant: Y⁻¹(D - MC)
5. Remainder: X - M×(4th output)

**Example:** `(3x⁴ + 5x³ + 2x² - 10x + 5) ÷ (2x - 7)`
```
Input: M=-1, A=3, B=5, C=2, D=-10, X=5, Y=2
When prompted for M: -7 (since 2x - 7)
Output: 1.5, 13, ? (Note: Results may need verification)
```

### 5. **M = -2: Polynomial Division (Degree 3 ÷ Degree 2)**
**Format:** `(Ax³ + Bx² + Cx + D) ÷ (Xx² + Yx + M)`

**Input Variables:**
- A = x³ coefficient
- B = x² coefficient
- C = x coefficient
- D = constant term
- X = divisor x² coefficient
- Y = divisor x coefficient
- Program prompts for new M = divisor constant term

**Output Order:**
1. Quotient x coefficient: AX⁻¹
2. Quotient constant: X⁻¹(B - AY)
3. Remainder x coefficient: C - AM - BY
4. Remainder constant: D - MB

**Example:** `(5x³ + 2x² - 10x + 5) ÷ (2x² - 12x - 7)`
```
Input: M=-2, A=5, B=2, C=-10, D=5, X=2, Y=-12
When prompted for M: -7
Output: 2.5, 31, ? (Note: Results may need verification)
```

## Z-Transform Example

### **Z-Transform Calculation:**
Given: `(2z⁻¹ - 2z⁻²)/(1 - z⁻¹ - 2z⁻²)`

Let `x = z⁻¹`, then the expression becomes:
```
(2x - 2x²)/(1 - x - 2x²)
```

This is a rational function that can be analyzed using polynomial division. Rewrite as:
```
Numerator: -2x² + 2x + 0
Denominator: -2x² - x + 1
```

Since we have degree 2 ÷ degree 2, we can use the division feature by considering it as a degree 3 polynomial with leading coefficient 0.

**Step 1: Perform polynomial division**
We want to divide `-2x² + 2x + 0` by `-2x² - x + 1`

Using M=-2 format (degree 3 ÷ degree 2), we can pad with zero:
```
Let: Ax³ + Bx² + Cx + D = 0x³ + (-2)x² + 2x + 0
Divisor: Xx² + Yx + M = -2x² + (-1)x + 1
```

**Calculator Input:**
```
M = -2
A = 0  (x³ coefficient)
B = -2 (x² coefficient)
C = 2  (x coefficient)
D = 0  (constant)
X = -2 (divisor x² coefficient)
Y = -1 (divisor x coefficient)
When prompted for M: 1 (divisor constant)
```

**Expected Output:**
1. Quotient x coefficient: 0
2. Quotient constant: 1
3. Remainder x coefficient: 3
4. Remainder constant: -1

**Result:** Quotient = 1, Remainder = 3x - 1

Therefore: `(2x - 2x²)/(1 - x - 2x²) = 1 + (3x - 1)/(1 - x - 2x²)`

**Final Z-transform:**
```
(2z⁻¹ - 2z⁻²)/(1 - z⁻¹ - 2z⁻²) = 1 + (3z⁻¹ - 1)/(1 - z⁻¹ - 2z⁻²)
```

## Program Notes

### Important:
1. **Variable Reuse:** The variables X and Y have different meanings depending on the operation mode
2. **Division Algorithms:** The division operations use synthetic division-like algorithms and may require careful interpretation
3. **Input Order:** Pay close attention to the input order for each operation mode
4. **Negative Coefficients:** Handle negative coefficients correctly, especially in division operations

### Limitations:
1. Integer coefficients work best for clear results
2. Division results may need manual verification
3. The program doesn't handle improper fractions directly for Z-transforms
4. For Z-transforms with higher powers, additional manipulation may be needed

### Tips for Z-Transform Calculations:
1. Substitute x = z⁻¹ to convert to polynomial form
2. Ensure both numerator and denominator are written in standard polynomial form
3. Use polynomial division to separate proper and improper fractions
4. For partial fraction decomposition, additional manual steps are needed

## Program Size and Compatibility
- **Approximate size:** 250-300 bytes
- **Compatible with:** Casio fx-991EX, fx-991ES Plus, and similar models
- **Memory usage:** Uses variables M, A, B, C, D, X, Y
- **Labels used:** Lbl 1, Lbl 2, Lbl 3

This program provides a quick way to perform common polynomial operations and can be adapted for basic Z-transform calculations in digital signal processing problems.