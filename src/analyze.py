import json
import ast
from pathlib import Path

BASE = Path("../../erpnext/erpnext/accounts/doctype/sales_invoice")

json_path = BASE / "sales_invoice.json"
py_path = BASE / "sales_invoice.py"

# ---------- Extract schema from JSON ----------
schema = json.loads(json_path.read_text())

fields = []
relationships = []

for f in schema.get("fields", []):
    fields.append({
        "name": f.get("fieldname"),
        "type": f.get("fieldtype")
    })

    if f.get("fieldtype") in ("Link", "Table"):
        relationships.append({
            "from": "Sales Invoice",
            "to": f.get("options"),
            "type": f.get("fieldtype")
        })

# ---------- Extract classes & functions from Python ----------
tree = ast.parse(py_path.read_text())

classes = []
functions = []

for node in ast.walk(tree):
    if isinstance(node, ast.ClassDef):
        classes.append(node.name)
    elif isinstance(node, ast.FunctionDef):
        functions.append(node.name)

output = {
    "entity": "Sales Invoice",
    "fields": fields,
    "classes": sorted(set(classes)),
    "functions": sorted(set(functions)),
    "relationships": relationships
}

Path("../output").mkdir(exist_ok=True)
Path("../output/entities.json").write_text(json.dumps(output, indent=2))

print("entities.json generated successfully")
# ---------- Generate Mermaid diagram ----------
lines = ["graph TD"]

for rel in relationships:
    if rel["to"]:
        target = rel["to"].replace(" ", "")
        lines.append(f"SalesInvoice --> {target}")

Path("../output/relationships.mermaid").write_text("\n".join(lines))

print("relationships.mermaid generated")

