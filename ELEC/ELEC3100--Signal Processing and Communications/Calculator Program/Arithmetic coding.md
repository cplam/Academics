# Arithmetic Coding Binary Converter Program

## Overview
This Casio calculator program converts a decimal number between 0 and 1 into its binary (base-2) representation using arithmetic coding principles. The program generates an infinite stream of binary digits.

## Program Code
```
?→A: While 1: 2A→A: If A≥1: Then 1◢ A-1→A: Else 0◢ IfEnd: WhileEnd
```

## How It Works
The program implements the arithmetic coding binarization algorithm:

1. **Initialization**: Input a decimal number A (0 ≤ A < 1)
2. **Infinite Loop**: 
   - Multiply A by 2 (shift left in binary)
   - If result ≥ 1: Output 1, subtract 1
   - If result < 1: Output 0
   - Repeat indefinitely

## Mathematical Basis
Given a decimal number `x` between 0 and 1, its binary representation is:
```
x = b₁ × 2⁻¹ + b₂ × 2⁻² + b₃ × 2⁻³ + ...
```
Where each `bᵢ` is either 0 or 1.

The algorithm extracts each bit by:
- Multiplying by 2: `2x = b₁ + (b₂ × 2⁻¹ + b₃ × 2⁻² + ...)`
- If `2x ≥ 1` → `b₁ = 1`, subtract 1 to get fractional part
- If `2x < 1` → `b₁ = 0`
- Repeat for next bits

## Example Usage

### Example 1: 0.375
```
Input: 0.375
Process:
0.375 × 2 = 0.75 → Output: 0
0.75 × 2 = 1.5 → Output: 1, subtract 1 → 0.5
0.5 × 2 = 1.0 → Output: 1, subtract 1 → 0
0 × 2 = 0 → Output: 0
... continues with all zeros

Output sequence: 0, 1, 1, 0, 0, 0, ...
Binary: 0.011000...
```

### Example 2: 0.625
```
Input: 0.625
Process:
0.625 × 2 = 1.25 → Output: 1, subtract 1 → 0.25
0.25 × 2 = 0.5 → Output: 0
0.5 × 2 = 1.0 → Output: 1, subtract 1 → 0
0 × 2 = 0 → Output: 0
... continues with all zeros

Output sequence: 1, 0, 1, 0, 0, 0, ...
Binary: 0.101000...
```

### Example 3: 0.2 (Non-terminating)
```
Input: 0.2
Process:
0.2 × 2 = 0.4 → Output: 0
0.4 × 2 = 0.8 → Output: 0
0.8 × 2 = 1.6 → Output: 1, subtract 1 → 0.6
0.6 × 2 = 1.2 → Output: 1, subtract 1 → 0.2
... repeats the pattern 0011...

Output sequence: 0, 0, 1, 1, 0, 0, 1, 1, ...
Binary: 0.001100110011... (repeating)
```

## Program Execution

### Step-by-Step:
1. **Run the program**
2. **Input**: Enter a decimal number between 0 and 1
3. **Output**: The calculator will display binary digits one by one indefinitely
4. **To stop**: Press the `AC` (All Clear) button

### Sample Run:
```
? 0.375  [Enter]
0        [Display]
1        [Display]
1        [Display]
0        [Display]
0        [Display]
... continues ...
```

## Special Cases

### Input = 0
```
Input: 0
Output: 0, 0, 0, 0, ... (all zeros)
Binary: 0.000000...
```

### Input = 0.5
```
Input: 0.5
Output: 1, 0, 0, 0, ... 
Binary: 0.100000...
```

### Input ≥ 1 or < 0
The algorithm assumes 0 ≤ A < 1. For A ≥ 1:
- The first output will be 1
- A-1 will be processed for subsequent bits
This effectively handles numbers ≥ 1 but produces unexpected results.

## Applications

### 1. Data Compression (Arithmetic Coding)
- Converts probability intervals to binary stream
- Used in lossless compression algorithms

### 2. Computer Science Education
- Demonstrates binary representation of fractions
- Shows how floating-point numbers are stored

### 3. Number Theory
- Illustrates the concept of binary expansions
- Shows periodic vs. terminating expansions

## Limitations

1. **Infinite Loop**: Program runs forever until manually stopped
2. **No Termination Detection**: Even for terminating binaries, it continues outputting zeros
3. **Precision Limits**: Calculator rounding may affect accuracy after many iterations
4. **Input Range**: Designed for 0 ≤ A < 1

## Extended Version (With Counter)

If you want to limit output to N bits:

```
?→A: ?→N: 1→C
While C≤N: 2A→A: If A≥1: Then 1◢ A-1→A: Else 0◢ IfEnd: C+1→C: WhileEnd
```

This version:
1. Takes number A
2. Takes number of bits N to display
3. Outputs exactly N binary digits

## Related Concepts

### Binary Fractions Table
| Decimal | Binary | Pattern |
|---------|--------|---------|
| 0.5 | 0.1 | Terminating |
| 0.25 | 0.01 | Terminating |
| 0.75 | 0.11 | Terminating |
| 0.1 | 0.000110011... | Repeating |
| 0.2 | 0.00110011... | Repeating |
| 0.3 | 0.0100110011... | Repeating |

### Algorithm Complexity
- Time: O(n) for n bits
- Space: O(1) - only stores current value
- Precision: Limited by calculator's floating-point accuracy

## Educational Value
This simple program demonstrates several important concepts:
- Binary number representation
- Infinite vs. finite representations
- Arithmetic coding fundamentals
- Shift-and-subtract algorithms

The program elegantly shows how continuous values can be converted to discrete binary sequences, which is fundamental to digital signal processing and data compression.