# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Instalacion(models.Model):
     _name = 'uposports.instalacion'
     _description = 'uposports Instalacion'

     nombre = fields.Char(string="Nombre", required=True, help="Nombre de la instalación")
     capacidad = fields.Integer("Capacidad máxima", required=True)
     descripcion = fields.Text()

     material_id = fields.One2many("uposports.material","instalacion_id","Material")
     reserva_id = fields.One2many("uposports.reserva","instalacion_id","Reserva")