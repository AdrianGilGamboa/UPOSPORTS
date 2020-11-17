# -*- coding: utf-8 -*-
{
    'name': "uposports",

    'summary': """
        Complejo Deportivo UpoSports""",

    'description': """
        Descripcion del modulo UPOSPORTS
    """,

    'author': "TSI - UPO",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/abono_view.xml',
        'views/cliente_view.xml',
        'views/empleado_view.xml',
        'views/instalacion_view.xml',
        'views/material_view.xml',
        'views/pago_view.xml',
        'views/reserva_view.xml',
        'views/complejoDeportivo_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
