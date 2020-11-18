# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
     _name = 'uposports.material'
     _description = 'uposports Material'

     name = fields.Char(string="Nombre", required=True, size=30, help="Nombre del material")
     descripcion = fields.Text(size=300)
     unidades = fields.Integer()

     instalacion_id = fields.Many2one("uposports.instalacion",string="Instalacion")