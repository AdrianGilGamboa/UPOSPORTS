# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Empleado(models.Model):
     _name = 'uposports.empleado'
     _description = 'Modelo para los empleados'

     name = fields.Char(string="DNI", required=True, size=9, help="DNI del empleado")
     nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del empleado")
     apellidos = fields.Char(string="Apellidos", required=True, size=50, help="Apellidos del empleado")
     telefono = fields.Integer(string="Telefono", size=9, required=True)

     abono_id = fields.One2many("uposports.abono","empleado_id","Abonos creado por el empleado")

     _sql_constraints = [('empleado_name_unique', 'UNIQUE (name)', 'Compruebe el DNI, debe ser único.')]
