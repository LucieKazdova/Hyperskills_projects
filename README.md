# Loan Calculator (Hyperskill)

Small command‑line tool that computes loan parameters for *annuity* and *differentiated* payments.

> **Why:** This is my study project finished in PyCharm. The script accepts CLI arguments via `argparse` and prints the requested result (monthly payment / number of months / principal) including *overpayment*.

---

## Features
- Annuity and differentiated payments
- Compute exactly **one** of:
  - monthly payment (`--payment`),
  - number of periods in months (`--periods`),
  - principal amount (`--principal`).
- Always requires annual **interest** (`--interest`).
- Prints **overpayment** for annuity and diff cases.

---

## CLI arguments

| Argument | Type | Required | Notes |
|---|---|---|---|
| `--type` | `str` | yes | `annuity` or `diff` |
| `--principal` | `int` | one of principal/payment/periods | loan principal |
| `--payment` | `float` | one of principal/payment/periods | monthly payment |
| `--periods` | `int` | one of principal/payment/periods | number of months |
| `--interest` | `float` | yes | annual interest rate in percent (e.g., `10` for 10%) |

Validation rules (as in Hyperskill task):
- `--type` must be `annuity` or `diff`.
- `--interest` must be provided.
- All numeric values must be **positive**.
- Exactly **3** of the 4 parameters among principal/payment/periods/interest must be provided.
- For `diff` you cannot provide `--payment`.

- ## Usage examples

```bash
# 1) How many months will it take?
python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=10

# 2) What is the monthly payment (annuity)?
python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=8

# 3) What is the principal (annuity)?
python creditcalc.py --type=annuity --payment=8722.0 --periods=120 --interest=7.5

# 4) Differentiated payments (prints one line per month) + overpayment:
python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
```

> Tip: keep a few commands in a text file *run_examples.txt* and copy–paste to quickly check the app.

---

## Project structure (suggested)

```
loan-calculator/
├─ creditcalc.py        # your final PyCharm version (single file is OK)
├─ README.md            # (this file)
└─ .gitignore
```

- Keep **imports once at the top** (`import argparse`, `import math`).  
- If you still have three partial versions from the stages, consider merging them into functions inside one file:

```python
if __name__ == "__main__":
    # parse args and call the correct function
    main()
```

## How to run (PyCharm)
1. Open the project folder in PyCharm.
2. Make sure the file is named `creditcalc.py` and set as the run configuration (green triangle ▶).
3. For CLI arguments, set **Run → Edit Configurations → Parameters** e.g.:  
   `--type=annuity --principal=1000000 --periods=60 --interest=8`

---

## How to publish to GitHub (two quick ways)

### A) Web UI (no Git on your PC)
1. Create a repository (e.g. `Hyperskills_projects`) or open an existing one.
2. Click **Add file → Create new file** and type `loan-calculator/README.md`.
3. Paste the content of this README and **Commit**.
4. Click **Add file → Upload files**, drag `creditcalc.py` (from Explorer) into `loan-calculator/` and commit.
5. (Optional) Create `.gitignore` with Python defaults (see below).

### B) Directly from PyCharm
1. In PyCharm: **VCS → Enable Version Control Integration… → Git**.
2. **Git → Commit…** select `creditcalc.py` & README, write a message (e.g. `Add loan calculator`) and **Commit**.
3. **Git → Push…** → set the remote to your GitHub repo URL and **Push**.

---

## .gitignore (Python)
```
__pycache__/
*.py[cod]
*.env
.venv/
venv/
.idea/
.DS_Store
```

---
