# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Instalacion(models.Model):
     _name = 'uposports.instalacion'
     _description = 'uposports Instalacion'

     name = fields.Char(string="Nombre", required=True, size=30, help="Nombre de la instalación")
     capacidad = fields.Integer(string="Capacidad máxima", required=True)
     descripcion = fields.Text(size=300)

     material_id = fields.One2many("uposports.material","instalacion_id","Material")
     reserva_id = fields.One2many("uposports.reserva","instalacion_id","Reserva")