# 🔢 NumericalMethods-SolverPack

This repository contains a set of Python implementations for commonly used numerical methods in computational mathematics. These are ideal for solving linear and nonlinear equations using iterative and direct techniques.

## 📘 Included Methods

### 🧮 Linear System Solvers
- **Jacobi Method** (`jacobi.py`)
- **Gauss LU Decomposition** (`LU gauss.py`)
- **Gauss-Seidel + Jacobi Comparison** (`seidel + jacobi.py`)
- **Relaxation Method** (`Relaxation method.py`)

### 🔍 Root-Finding Techniques
- **Newton-Raphson Method** (`Newton method.py`)
- **Bisection Method (Dichotomy)** (`Метод дихотомії.py`)

## 🧪 Usage

Each file is a standalone script. To run a method, use:

```bash
python jacobi.py
```

Or substitute jacobi.py with any other file name listed above. Some scripts may require initial user input (e.g., matrices, functions, or tolerance levels), usually provided via the console or coded into the file.

## 💡 Example: Newton's Method

  def f(x):
      return x**3 - 4*x + 1
  
  def df(x):
      return 3*x**2 - 4
      
You can define the function and its derivative directly inside Newton method.py and run it to find the root.

## 📂 Project Structure

  ├── jacobi.py
  ├── LU gauss.py
  ├── Newton method.py
  ├── Relaxation method.py
  ├── seidel + jacobi.py
  ├── Метод дихотомії.py (Bisection Method)
  └── README.md
  
## 🧠 Learning Objectives

    Understand the logic and convergence of iterative solvers
    Apply decomposition techniques like LU
    Experiment with tolerance and iteration limits
    Compare the performance and stability of solvers
    
## 📎 Notes

  Scripts are written in plain Python (no external dependencies beyond standard libraries like math or numpy)
  The Bisection script is named in Ukrainian (Метод дихотомії.py) but the logic is universal
