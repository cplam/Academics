# Disk Scheduling Algorithm Calculator (Casio)

## Overview
This program calculates the **total seek distance** for the **any** disk scheduling algorithm on a Casio calculator.

## Program Code
```
?→B: While 1: ?→A: A= -1 => M◢ Abs(A-B) M+: A→B: WhileEnd
```

## How It Works
The program simulates disk scheduling by:
1. Accepting the starting disk head position
2. Processing each request in the order they arrive
3. Calculating the absolute distance between consecutive positions
4. Summing all distances to get the total seek distance

## Input Format
1. **First input:** Starting cylinder position (e.g., `50`)
2. **Subsequent inputs:** Sequence of cylinder requests in order
3. **Termination:** Enter `-1` to calculate and display the result

## Example Usage

### Problem Statement
Suppose a disk drive has 200 cylinders (0-199). The drive is currently at cylinder 50. The queue of pending requests is: 100, 80, 10, 60, 20, 120, 30, 180.

### Step-by-Step Execution
```
Run Program:
? 50        ← Starting position
? 100       ← First request
? 80        ← Second request
? 10        ← Third request
? 60        ← Fourth request
? 20        ← Fifth request
? 120       ← Sixth request
? 30        ← Seventh request
? 180       ← Eighth request
? -1        ← Termination signal

Output: 570 ← Total seek distance
```

### Calculation Details
```
From 50 to 100: |100-50| = 50
From 100 to 80: |80-100| = 20
From 80 to 10:  |10-80|  = 70
From 10 to 60:  |60-10|  = 50
From 60 to 20:  |20-60|  = 40
From 20 to 120: |120-20| = 100
From 120 to 30: |30-120| = 90
From 30 to 180: |180-30| = 150
                          ────
                          Total: 570
```

## Important Notes
1. **No Optimization:** Requests are processed in the exact order entered
2. **No Direction Consideration:** The program doesn't consider arm movement direction
3. **Negative Termination:** Always use `-1` to end input and get results

## Common Disk Scheduling Algorithms
For comparison, here are other common algorithms (not implemented in this program):

| Algorithm | Description | Usually Better When |
|-----------|-------------|---------------------|
| **SSTF** | Shortest Seek Time First | Requests are clustered |
| **SCAN** | Elevator algorithm | Load is evenly distributed |
| **C-SCAN** | Circular SCAN | Uniform wait times needed |
| **LOOK** | SCAN without going to ends | More efficient than SCAN |
| **C-LOOK** | C-SCAN without going to ends | Most practical |

## Tips for Use
1. **Accuracy:** Double-check your input sequence before running
2. **Verification:** Manually calculate the first few steps to ensure correct operation
3. **Memory:** The calculator stores intermediate values in variables B (current position) and M (total distance)
4. **Reset:** To run a new calculation, you must restart the program

## Sample Problems for Practice
Try these with the program:

### Problem 1
- Starting position: 100
- Request queue: 50, 150, 30, 170, 10, 190
- Expected output: 500

### Problem 2
- Starting position: 0
- Request queue: 199, 1, 198, 2, 197, 3
- Expected output: 794

---

**Note:** This program is specifically for educational purposes and exam calculations. Real-world disk schedulers use more complex algorithms to optimize performance.