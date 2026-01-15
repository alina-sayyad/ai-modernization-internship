# Sales Invoice – Code Summary

## What is Sales Invoice?
Sales Invoice represents a finalized sales transaction in ERPNext.
It records customer details, sold items, taxes, totals, and accounting impact.

## Files Analyzed
- `sales_invoice.json` – Entity schema and field definitions
- `sales_invoice.py` – Business logic and validation rules

## Extracted Structure
- **Entity:** Sales Invoice
- **Primary Class:** `SalesInvoice`
- **Key Hooks Identified:**
  - `validate`
  - `on_submit`
  - `before_save`

## Field Insights
Examples of important fields extracted from the schema:
- `customer` (Link → Customer)
- `items` (Table → Sales Invoice Item)
- `posting_date` (Date)
- `grand_total` (Currency)

## Relationships
Sales Invoice has strong relationships with:
- Customer
- Item (via child table)
- Account (for accounting entries)

## Key Observations
- The `SalesInvoice` class acts as the main orchestrator
- Business rules are enforced through lifecycle hooks
- Schema and logic are cleanly separated across JSON and Python

## Why This Matters
This separation of schema and logic allows ERPNext to scale across
multiple business domains while remaining maintainable.
