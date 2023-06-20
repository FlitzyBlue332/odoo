from odoo import models

class InvoiceExport(models.Model):
    _name = 'invoice.export'
    _description = 'Invoice Export'

    def export_invoice_data(self):
        # Fetch invoice data using Odoo's ORM
        invoices = self.env['account.invoice'].search([])

        # Prepare CSV file
        import csv
        csv_data = []
        csv_fields = ['Invoice Number', 'Customer', 'Amount']

        for invoice in invoices:
            csv_row = [
                invoice.number,
                invoice.partner_id.name,
                invoice.amount_total,
            ]
            csv_data.append(csv_row)

        # Export data to CSV file
        with open('/path/to/exported_invoices.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_fields)
            writer.writerows(csv_data)

    def export_invoice_data_button(self):
        self.export_invoice_data()
        # Optional: Provide a feedback message or perform additional actions after exporting the data
        return True