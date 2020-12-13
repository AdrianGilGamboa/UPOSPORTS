# -*- coding: utf-8 -*-
{
    'name': "UPOSports",

    'summary': """
        Complejo Deportivo UPOSports""",

    'description': """
        Nuestro sistema tiene como fin gestionar un complejo deportivo, que será manipulado por los empleados del propio complejo deportivo, para ello desarrollaremos un Módulo personalizado en un sistema ERP que permita realizar su cometido. Nos hemos decidido por Odoo por ser un ERP de código abierto y disponer de una interfaz web muy clara e intuitiva tanto para desarrolladores como usuarios del sistema.
    """,

    'author': "Adrián Gil Gamboa, Javier Giménez Figueroa, Manuel Molina Fuentes, Daniel Emilio López Luque",
    'website': "https://github.com/AdrianGilGamboa/uposports",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'deporte',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/tarjeta_report.xml', 
        'reports/efectivo_report.xml',
        'views/reserva_view.xml',
        'views/abono_view.xml',
        'views/cliente_view.xml',
        'views/empleado_view.xml',
        'views/instalacion_view.xml',
        'views/material_view.xml',
        'views/pago_view.xml',
        'views/efectivo_view.xml',
        'views/tarjeta_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
