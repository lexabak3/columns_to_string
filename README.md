# columns_to_string

A lightweight Python tool that converts clipboard content into a clean, comma-separated string.  
Perfect for transforming column values (e.g., copied from Excel or Google Sheets) into a single line for SQL queries, logs, or data processing.

---

## 🚀 Features
- Reads data directly from your clipboard.
- Handles tabular data (e.g., Excel, Google Sheets, CSV).
- Outputs values as a single string separated by commas.
- Simple, fast, and dependency-light.

---

## 📦 Installation
Clone the repository:

```bash
git clone https://github.com/your-username/columns_to_string.git
cd columns_to_string
```

Install the required dependency:

```bash
pip install clipboard
```

---

## 🔧 Usage

1. Copy some column values from Excel / Google Sheets / CSV file.  
2. Run the script:

```bash
python columns_to_string.py
```

3. The program will output the values as a string, for example:

**Clipboard input:**
```
A123
B456
C789
```

**Output:**
```
'A123','B456','C789'
```

---

## 🛠 Example Use Case
Useful for generating:
- SQL `IN` clauses
- Logging IDs
- Quick copy-paste transformations


