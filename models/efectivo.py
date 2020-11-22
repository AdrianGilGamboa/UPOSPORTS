# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Efectivo(models.Model):
    _inherit = 'uposports.pago'
    _name = 'uposports.efectivo'



    importeAbonado = fields.Float(string="Dinero entregado(€)",required=True)
    importeDevuelto = fields.Float(string="Dinero devuelto(€)",readonly=1)
