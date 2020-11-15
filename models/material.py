# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
     _name = 'uposports.material'
     _description = 'uposports Material'

     nombre = fields.Char(string="Nombre Material", required=True, help="Nombre del material")
     descripcion = fields.Text()
     unidades = fields.Integer()