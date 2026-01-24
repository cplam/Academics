# Routh Table Algorithm - High-Level Idea

## **Core Concept**
Test polynomial stability **without solving for roots** by constructing a triangular table from coefficients and checking signs in the first column.

If noticed that any cofficients are non-positive, which is 0 or negative, the system is indeed unstable.
---

## **Step-by-Step Idea**

### 1. **Setup First Two Rows**
- **Row 0 (sⁿ):** Take coefficients of even powers: \(a_0, a_2, a_4, \dots\)
- **Row 1 (sⁿ⁻¹):** Take coefficients of odd powers: \(a_1, a_3, a_5, \dots\)

### 2. **Compute Subsequent Rows**
For each new row \(i\) (starting from row 2):
- Each element \(r_{i,j}\) is computed from the **two rows above it**:
\[
\begin{bmatrix} r_{i-2,0} & r_{i-2,j+1} \\ r_{i-1,0} & r_{i-1,j+1} \end{bmatrix}
\]
- Basically: cross-multiply elements from previous two rows, divide by pivot element above.

### 3. **Stop When** 
- You reach row \(s^0\) (last row has only one element).

### 4. **Check Stability**
- **Stable if:** All elements in **first column** are **positive** (\(> 0\)).
- **Unstable if:** Any element in first column is **negative or zero** (sign changes indicate right-half-plane roots).

---

## **Key Insight**
- The **first column signs** reveal how many roots are in the right-half plane.
- No need to factor polynomial or find actual roots.
- Special cases (zero in first column, entire row zero) require modified procedures but same principle.

---

## **Example Pattern**
For \(a(s) = s^4 + 10s^3 + 35s^2 + 50s + 24\):

| Power | Col 0 | Col 1 |
|-------|-------|-------|
| \(s^4\) | 1 | 35 |
| \(s^3\) | 10 | 50 |
| \(s^2\) | 30 | 24 |
| \(s^1\) | 42 | – |
| \(s^0\) | 24 | – |

✅ All first column positive → **STABLE**

❌ Otherwise → **UNSTABLE**

---

## **Why It Works (Out of scope)**
- Routh table is a **recursive factorization** that preserves root location information.
- Sign changes in first column = number of roots with positive real parts.
- Mathematically derived from Sturm's theorem and Cauchy index.