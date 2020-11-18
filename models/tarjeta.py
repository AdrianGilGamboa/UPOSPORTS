# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Tarjeta(models.Model):
     _inherit = 'uposports.pago'
     _name = 'uposports.tarjeta'


     entidadBancaria=fields.Char(string="Entidad Bancaria",size=30,required=True)


