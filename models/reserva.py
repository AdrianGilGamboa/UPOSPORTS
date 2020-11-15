# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reserva(models.Model):
     _name = 'uposports.reserva'
     _description = 'uposports Reserva'

     id_reserva = fields.Integer("ID Reserva")
     freserva = fields.Datetime('Fecha de reserva', required=True, autodate = True)
     horaInicio= fields.Datetime('Hora de inicio', required=True, autodate = True)
     horaFin = fields.Datetime('Hora de fin', required=True, autodate = True)