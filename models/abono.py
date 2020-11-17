# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Abono(models.Model):
     _name = 'uposports.abono'
     _description = 'uposports Abono'

     precio = fields.Float(("Precio (€)"),required=True)
     tipo = fields.Char(string="Tipo", required=True, help="Nombre identificativo del abono")
     duracion = fields.Char(string="Duracion (meses)", required=True, help="Duración en meses del abono")
    

     empleado_id = fields.Many2one("uposports.empleado",string="Creado por el empleado")
     cliente_id =  fields.One2many("uposports.cliente","abono_id","Cliente")
     complejoDeportivo_id = fields.Many2one("uposports.complejoDeportivo",string="Hola")
    