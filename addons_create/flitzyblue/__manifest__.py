{
    'name': 'Testing Melody',
    'version': '16.0',
    'summary': 'Integration with Another Application',
    'description': 'This addon integrates Odoo with Another Application.',
    'category': 'Custom Development',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base'],
    "application": True,  # This line says the module is an App, and not a module
    "data": [
        "security/ir.model.access.csv",
        "views/rumah_views.xml",
        "views/flitzyblue_menu.xml"
    ],
    "installable": True,
}
