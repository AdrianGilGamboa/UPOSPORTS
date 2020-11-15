# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pago(models.Model):
     _name = 'uposports.pago'
     _description = 'uposports Pago'

     fecha=fields.Datetime('Fecha y Hora')
     cantidad=fields.Float('Cantidad')
