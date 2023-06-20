{
    'name': 'Invoice Export',
    'version': '1.0',
    'author': 'Fletz and Ryu',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/invoice_export_views.xml',
    ],
    'application' : True,
    'installable': True,
    'auto_install': False,
}