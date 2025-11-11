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


---
