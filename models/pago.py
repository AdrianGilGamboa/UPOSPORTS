# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api

#Modelo del cual se hereda el modelo tarjeta y efectivo.

class Pago(models.Model):
     _name = 'uposports.pago'
     _description = 'Modelo de pago que servirá de modelo padre para tarjeta y efectivo'
     _rec_name = 'cliente_id'

     fecha=fields.Datetime(string='Fecha y Hora',required=True, default = lambda self: datetime.today(),readonly=1)
     cantidad=fields.Float(string='Precio (€)')

     cliente_id = fields.Many2one("uposports.cliente",string="Cliente",required=True)
     abono_id = fields.Many2one("uposports.abono",string="Abono",required=True)

#El precio del abono se inserta automaticamente, obtenienndolo del modelo abono, mediante el atributo abono_id
     @api.onchange('abono_id')
     def onchange_abono(self):
        self.cantidad = self.abono_id.precio

