# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class Reserva(models.Model):
     _name = 'uposports.reserva'
     _description = 'uposports Reserva'
     _rec_name = 'instalacion_id'

     name = fields.Integer(string="ID Reserva")
     fechaHoraInicio= fields.Datetime('Fecha/Hora Inicio', required=True, autodate = True, store=True)
     fechaHoraFin = fields.Datetime('Fecha/Hora Fin', required=True, autodate = True, store=True)

     instalacion_id = fields.Many2one("uposports.instalacion",string="Instalacion",required=True )
     cliente_id = fields.Many2one("uposports.cliente",string="Cliente",required=True)  