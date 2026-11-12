# CogniExam: Human Review Sample (2 Real Papers, 10 Questions Each)

Extracted questions, assigned Bloom's levels, pedagogical justifications, and canonical answer keys for faculty inspection.

## Paper: `01_vtu_btech_maths_cse_2023.pdf`

### Question 1a [6 Marks] - Section: Module-1
**Question:** Show that x(∂u/∂x) + y(∂u/∂y) = (u/(u-1)) * e^u if e^u = x + y.

- **Assigned Bloom Level:** `L4` (Analyze)
- **Action Verb:** Show
- **Pedagogical Justification:** The question as stated contains a mathematical error in the identity to be proved. The rubric accounts for the student correctly deriving the partials and evaluating the expression, even if the target identity is unreachable given the initial constraint.
- **Confidence Tag:** High confidence - AI synthesized (Engine: gemini-3.5-flash)
- **Canonical Answer Key:**
```
Given the equation e^u = x + y, differentiate partially with respect to x: (∂/∂x)(e^u) = (∂/∂x)(x + y) => e^u (∂u/∂x) = 1. Thus, ∂u/∂x = 1/e^u. Similarly, differentiate with respect to y: (∂/∂y)(e^u) = (∂/∂y)(x + y) => e^u (∂u/∂y) = 1. Thus, ∂u/∂y = 1/e^u. Substitute these into the expression: x(∂u/∂x) + y(∂u/∂y) = x(1/e^u) + y(1/e^u) = (x + y)/e^u. Since x + y = e^u, the expression becomes e^u / e^u = 1. However, the requested identity is x(∂u/∂x) + y(∂u/∂y) = (u/(u-1)) * e^u. Re-evaluating the implicit differentiation: differentiating e^u = x + y leads to (e^u) ∂u/∂x = 1 and (e^u) ∂u/∂y = 1. Summing x(∂u/∂x) + y(∂u/∂y) = (x+y)/e^u = e^u/e^u = 1. The original prompt's identity is mathematically inconsistent with the given function e^u = x + y. If we assume u = ln(x+y), then x(∂u/∂x) + y(∂u/∂y) = x/(x+y) + y/(x+y) = 1. The identity provided in the prompt is false.
```
- **Step-by-Step Marking Rubric:**
  * Correctly calculates partial derivatives ∂u/∂x and ∂u/∂y using implicit differentiation.: **3.0 Marks**
  * Attempts to substitute partial derivatives into the target identity.: **2.0 Marks**
  * Identifies the mathematical inconsistency or completes the derivation steps correctly.: **1.0 Marks**
- **Own-Words Criteria:**
  * Implicit function differentiation
  * Chain rule for partial derivatives
  * Variable substitution identities

---

### Question 5a [6 Marks] - Section: Module-3
**Question:** Find the constant b if the rank of [[1,1,1,0],[4,4,3,1],[2,2,2,b],[9,9,3,b]] is 3.

- **Assigned Bloom Level:** `L4` (Analyze)
- **Action Verb:** Find
- **Pedagogical Justification:** The problem requires analysis of matrix properties via row reduction to determine parameter constraints. The previous rubric was missing, and the derivation identifies that two distinct values of b satisfy the condition.
- **Confidence Tag:** High confidence - AI synthesized (Engine: gemini-3.5-flash)
- **Canonical Answer Key:**
```
To find b such that the rank of the matrix A is 3, we perform row reduction. The matrix is: [[1,1,1,0], [4,4,3,1], [2,2,2,b], [9,9,3,b]]. Perform R2 = R2 - 4*R1, R3 = R3 - 2*R1, R4 = R4 - 9*R1: [[1,1,1,0], [0,0,-1,1], [0,0,0,b], [0,0,-6,b]]. Now, perform R4 = R4 - 6*R2: [[1,1,1,0], [0,0,-1,1], [0,0,0,b], [0,0,0,b-6]]. For the rank to be 3, the third and fourth rows must not both be zero, and the row-echelon form must have exactly three non-zero rows. Since Row 3 is [0, 0, 0, b] and Row 4 is [0, 0, 0, b-6], these rows are linearly dependent unless one is zero and the other is not. Specifically, if b = 6, Row 3 becomes [0, 0, 0, 6] and Row 4 becomes [0, 0, 0, 0], leaving 3 non-zero rows. If b = 0, Row 3 is [0, 0, 0, 0] and Row 4 is [0, 0, 0, -6], which also results in rank 3. Therefore, b = 0 or b = 6.
```
- **Step-by-Step Marking Rubric:**
  * Correctly applying row reduction operations to reach row-echelon form.: **2.0 Marks**
  * Correctly setting up the condition for rank 3 based on row linear dependence.: **2.0 Marks**
  * Accurately identifying both values of b (0 and 6).: **2.0 Marks**
- **Own-Words Criteria:**
  * Row echelon form
  * Linear dependence of rows
  * Matrix rank definition

---

### Question 9a [6 Marks] - Section: Module-5
**Question:** Verify whether the transformation T: R^2 -> R^2 defined by T(x,y) = (x+y, 3x-4y, 10x+4y) is linear or not.

- **Assigned Bloom Level:** `L3` (Apply)
- **Action Verb:** Verify
- **Pedagogical Justification:** The user provided a flawed question (codomain R^3, not R^2 as stated in the prompt) and a rubric total of 0. The correction addresses the linearity proof process with a total of 6 marks, reflecting the complexity of the two-part verification.
- **Confidence Tag:** High confidence - AI synthesized (Engine: gemini-3.5-flash)
- **Canonical Answer Key:**
```
A transformation T: R^2 -> R^3 is linear if it satisfies two conditions for all vectors u, v in R^2 and scalars c: (1) T(u+v) = T(u) + T(v) and (2) T(cu) = cT(u). Let u = (x1, y1) and v = (x2, y2). T(u+v) = T(x1+x2, y1+y2) = (x1+x2+y1+y2, 3(x1+x2)-4(y1+y2), 10(x1+x2)+4(y1+y2)) = (x1+y1, 3x1-4y1, 10x1+4y1) + (x2+y2, 3x2-4y2, 10x2+4y2) = T(u) + T(v). Let c be a scalar; T(cu) = T(cx1, cy1) = (cx1+cy1, 3cx1-4cy1, 10cx1+4cy1) = c(x1+y1, 3x1-4y1, 10x1+4y1) = cT(u). Since both conditions hold, the transformation is linear.
```
- **Step-by-Step Marking Rubric:**
  * Definition of linearity properties (additivity and homogeneity).: **2.0 Marks**
  * Algebraic verification of additivity T(u+v) = T(u) + T(v).: **2.0 Marks**
  * Algebraic verification of homogeneity T(cu) = cT(u).: **2.0 Marks**
- **Own-Words Criteria:**
  * Superposition principle
  * Homogeneity of degree one
  * Linearity axioms

---

## Paper: `06_cbse_computer_science_2024.pdf`

### Question 1 [1 Marks] - Section: A
**Question:** State True or False: “In a Python program, if a break statement is given in a nested loop, it terminates the execution of all loops in one go.”

- **Assigned Bloom Level:** `L2` (Understand)
- **Action Verb:** State
- **Pedagogical Justification:** Requires conceptual understanding of flow control in nested loops to evaluate the validity of the statement.
- **Confidence Tag:** High confidence - AI synthesized (Engine: gemini-3.5-flash)
- **Canonical Answer Key:**
```
False. A break statement only terminates the inner-most loop in which it resides.
```
- **Step-by-Step Marking Rubric:**
  * Correct identification of the statement as False: **1.0 Marks**
- **Own-Words Criteria:**
  * Functionality of break statement
  * Scope of termination in nested loops

---

### Question 2 [1 Marks] - Section: A
**Question:** In a table in MYSQL database, an attribute A of datatype varchar(20) has the value “Keshav”. The attribute B of datatype char(20) has value “Meenakshi”. How many characters are occupied by attribute A and attribute B?

- **Assigned Bloom Level:** `L3` (Apply)
- **Action Verb:** Calculate
- **Pedagogical Justification:** Requires application of database storage rules for VARCHAR (variable) vs CHAR (fixed-length) data types.
- **Confidence Tag:** High confidence - AI synthesized (Engine: gemini-3.5-flash)
- **Canonical Answer Key:**
```
b. 6, 20. VARCHAR stores the actual length (6 for 'Keshav'), while CHAR pads to the defined length (20 for 'Meenakshi').
```
- **Step-by-Step Marking Rubric:**
  * Selection of the correct option based on storage characteristics: **1.0 Marks**
- **Own-Words Criteria:**
  * Difference between VARCHAR and CHAR storage
  * Padding behavior in fixed-length strings

---

### Question 3 [1 Marks] - Section: A
**Question:** What will be the output of the following statement: print(3-2**2**3+99/11)

- **Assigned Bloom Level:** `L3` (Apply)
- **Action Verb:** Evaluate
- **Pedagogical Justification:** Tests the application of Python operator precedence rules, specifically exponentiation right-associativity and floating point division.
- **Confidence Tag:** High confidence - AI synthesized (Engine: gemini-3.5-flash)
- **Canonical Answer Key:**
```
c. -244.0. Calculation: 2**3=8, 2**8=256, 3-256 = -253, -253 + 9.0 = -244.0
```
- **Step-by-Step Marking Rubric:**
  * Correct evaluation following operator precedence: **1.0 Marks**
- **Own-Words Criteria:**
  * Right-to-left associativity of exponentiation
  * Float output of division operator

---

### Question 5 [1 Marks] - Section: A
**Question:** In MYSQL database, if a table, Alpha has degree 5 and cardinality 3, and another table, Beta has degree 3 and cardinality 5, what will be the degree and cardinality of the Cartesian product of Alpha and Beta?

- **Assigned Bloom Level:** `L3` (Apply)
- **Action Verb:** Determine
- **Pedagogical Justification:** Tests the application of relational algebra properties regarding degree (sum of columns) and cardinality (product of rows) in Cartesian products.
- **Confidence Tag:** High confidence - AI synthesized (Engine: gemini-3.5-flash)
- **Canonical Answer Key:**
```
b. 8, 15. Degree = 5+3=8. Cardinality = 3*5=15.
```
- **Step-by-Step Marking Rubric:**
  * Calculation of correct degree (sum) and cardinality (product): **1.0 Marks**
- **Own-Words Criteria:**
  * Definition of degree in relational tables
  * Definition of cardinality in relational tables

---

### Question 7 [1 Marks] - Section: A
**Question:** Which of the following will delete key-value pair for key = “Red” from a dictionary D1?

- **Assigned Bloom Level:** `L1` (Remember)
- **Action Verb:** Identify
- **Pedagogical Justification:** Requires memory of Python dictionary syntax and the specific keyword used for deletion.
- **Confidence Tag:** High confidence - AI synthesized (Engine: gemini-3.5-flash)
- **Canonical Answer Key:**
```
b. del D1['Red']
```
- **Step-by-Step Marking Rubric:**
  * Selection of the valid syntax for dictionary item deletion: **1.0 Marks**
- **Own-Words Criteria:**
  * Python dictionary syntax
  * del statement utility

---

### Question 9 [1 Marks] - Section: A
**Question:** Which of the following statement(s) would give an error during execution of the following code? tup = (20,30,40,50,80,79); tup[4]=80

- **Assigned Bloom Level:** `L2` (Understand)
- **Action Verb:** Analyze
- **Pedagogical Justification:** Tests the understanding of tuple immutability and its impact on item assignment.
- **Confidence Tag:** High confidence - AI synthesized (Engine: gemini-3.5-flash)
- **Canonical Answer Key:**
```
d. Statement 4. Tuples are immutable and do not support item assignment.
```
- **Step-by-Step Marking Rubric:**
  * Identification of Statement 4 due to immutability: **1.0 Marks**
- **Own-Words Criteria:**
  * Immutability of tuples
  * Python error types

---

