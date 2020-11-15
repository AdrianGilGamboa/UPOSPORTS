# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Abono(models.Model):
     _name = 'uposports.abono'
     _description = 'uposports Abono'

     precio = fields.Float(("Precio"),required=True)
     tipo = fields.Char(string="Tipo", required=True, help="tipo de abono")
     duracion = fields.Char(string="Duracion", required=True, help="tiempo que dura el abono")
    

    