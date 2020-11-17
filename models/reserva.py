# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reserva(models.Model):
     _name = 'uposports.reserva'
     _description = 'uposports Reserva'

     id_reserva = fields.Integer("ID Reserva")
     freserva = fields.Datetime('Fecha de reserva', required=True, autodate = True)
     horaInicio= fields.Datetime('Hora de inicio', required=True, autodate = True)
     horaFin = fields.Datetime('Hora de fin', required=True, autodate = True)

     instalacion_id = fields.Many2one("uposports.instalacion",string="Instalacion")
     cliente_id = fields.One2many("uposports.cliente","reserva_id","Cliente")
     complejoDeportivo_id = fields.Many2one("uposports.complejoDeportivo",string="Hola")

