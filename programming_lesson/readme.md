# Usage:
`python fintrack_invoice_generator.py`

# Requirements:
`pip install reportlab openpyxl`

# What the script does:
 - Creates ./invoices directory if missing
 - Generates invoice files for PDF, XLSX and HTML
 - Prints created file paths to stdout

# Extending:
 - Add new generator class inheriting InvoiceGenerator and implement generate_invoice()
 - Register it in generator_factory
 - Optionally apply TaxMixin if you want tax-aware generators

# Bonus suggestions (already possible):
 - Create TaxedPDFGenerator by subclassing TaxMixin and PDFInvoiceGenerator:
 class TaxedPDFGenerator(TaxMixin, PDFInvoiceGenerator):
 pass
 - Use dependency injection to select generators by config
