# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Empleado(models.Model):
     _name = 'uposports.empleado'
     _description = 'uposports Empleado'

     dni = fields.Char(string="DNI", required=True, help="DNI del empleado")
     nombre = fields.Char(string="Nombre", required=True, help="Nombre del empleado")
     apellidos = fields.Char(string="Apellidos", required=True, help="Apellidos del empleado")
     telefono = fields.Integer("Telefono", required=True)

     abono_id = fields.One2many("uposports.abono","empleado_id","Abono")

