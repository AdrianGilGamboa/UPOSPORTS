# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api


class Pago(models.Model):
     _name = 'uposports.pago'
     _description = 'uposports Pago'
     _rec_name = 'cliente_id'

     fecha=fields.Datetime(string='Fecha y Hora',required=True, default = lambda self: datetime.today(),readonly=1)
     cantidad=fields.Float(string='Cantidad(€)',required=True)

     cliente_id = fields.Many2one("uposports.cliente",string="Cliente",required=True)
     abono_id = fields.Many2one("uposports.abono",string="Abono",required=True)

