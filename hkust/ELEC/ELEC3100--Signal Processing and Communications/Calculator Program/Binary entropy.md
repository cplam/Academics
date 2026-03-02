# Binary Entropy Calculator - Usage Guide

## Program Code
Program size: 59 bytes
```
MM-: 1→X: Lbl 1: ?→A: A = 0 => Goto 1: If A < 0: Then Abs(X) > 1E-5 => 0⁻¹: M◢ IfEnd: X-A→X: -Alog(2,A M+: Goto 1
```

## How to Use

### **Step-by-Step Instructions:**

1. **Run the program**
2. **Enter probabilities one by one** (0 to 1)
3. **End with any negative number** (e.g., -1)
4. **Valid input → displays entropy**
5. **Invalid input → shows Math ERROR**

---

## **Examples**

### **Example 1: Fair Coin** (p=0.5, 0.5)
```
INPUT          OUTPUT
Run program
0.5 [EXE]
0.5 [EXE]
-1 [EXE]       1
```
**Result:** Entropy = 1 bit

---

### **Example 2: Biased Coin** (p=0.9, 0.1)
```
INPUT          OUTPUT
Run program
0.9 [EXE]
0.1 [EXE]
-1 [EXE]       0.4689955936
```
**Result:** Entropy ≈ 0.469 bits

---

### **Example 3: 4-Sided Die** (p=0.25 each)
```
INPUT          OUTPUT
Run program
0.25 [EXE]
0.25 [EXE]
0.25 [EXE]
0.25 [EXE]
-1 [EXE]       2
```
**Result:** Entropy = 2 bits

---

### **Example 4: With Zero Probability**
```
INPUT          OUTPUT
Run program
0.6 [EXE]
0.4 [EXE]
0.0 [EXE]      (automatically skipped)
-1 [EXE]       0.9709505945
```
**Result:** Entropy ≈ 0.971 bits

---

### **Example 5: ERROR - Invalid Sum**
```
INPUT          OUTPUT
Run program
0.3 [EXE]
0.3 [EXE]
0.3 [EXE]
-1 [EXE]       Math ERROR
```
**Reason:** 0.3+0.3+0.3=0.9 ≠ 1

---

### **Example 6: Single Outcome** (p=1)
```
INPUT          OUTPUT
Run program
1 [EXE]
-1 [EXE]       0
```
**Result:** Entropy = 0 bits (no uncertainty)

---

### **Example 7: Three Outcomes** (p=0.2, 0.3, 0.5)
```
INPUT          OUTPUT
Run program
0.2 [EXE]
0.3 [EXE]
0.5 [EXE]
-1 [EXE]       1.485475297
```
**Result:** Entropy ≈ 1.485 bits

---

## **Important Notes**

### **What Works:**
- ✅ Probabilities between 0 and 1
- ✅ Any number of probabilities
- ✅ Zero probabilities (skipped automatically)
- ✅ Must sum exactly to 1, but can allow tolarance precision error due to decimial numbers

### **What Doesn't Work:**
- ❌ Probabilities that don't sum to 1 (causes ERROR)
- ❌ Negative probabilities (undefined log)
- ❌ Probabilities > 1 (causes X to go negative)

### **Termination:**
- Use **any negative number** to end input
- Common choices: -1, -99, -999
- The specific value doesn't matter

### **Error Messages:**
- **"Math ERROR"** = Probabilities don't sum very close to 1
- **No other error checking** (be careful with inputs)

## **Quick Reference**

| Input Pattern | Expected Output |
|---------------|-----------------|
| 0.5, 0.5, -1 | 1 |
| 0.9, 0.1, -1 | 0.469 |
| 0.25×4, -1 | 2 |
| 1, -1 | 0 |
| Invalid sum, -1 | ERROR |

This program calculates **Shannon Entropy**:  
`H(X) = -Σ pᵢ log₂(pᵢ)` measured in **bits**