from odoo import fields, models

class rumah(models.Model):
    _name = "rumah"
    _description = "Rumah milik fletz"
    _order = "sequence"

    # bisa di edit jadi nanti ya gitu e faktur buatnya isi aja
    name = fields.Char('Nama Rumah', required=True, translate=True)
    number_of_months = fields.Integer('# Months', required=True)
    active = fields.Boolean('Ditinggali', default=True)
    sequence = fields.Integer('Sequence', default=10)

    _sql_constraints = [
        ('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
    ]