# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api


class Reserva(models.Model):
     _name = 'uposports.reserva'
     _description = 'uposports Reserva'
     _rec_name = 'instalacion_id'

     name = fields.Integer(string="ID Reserva")
     fechaHoraInicio = fields.Datetime(string='Fecha/Hora Inicio', required=True, autodate = True, store=True, default = lambda self: datetime.today())
     fechaHoraFin = fields.Datetime(string='Fecha/Hora Fin', required=True, autodate = True, store=True, default = lambda self: datetime.today())

     instalacion_id = fields.Many2one("uposports.instalacion",string="Instalacion",required=True )
     cliente_id = fields.Many2one("uposports.cliente",string="Cliente",required=True)


#     @api.onchange('fechaHoraInicio')
#     def onchange_fechaHoraInicio(self):
#          resultadoFechaInicio = {}
#          if self.fechaHoraInicio < datetime.today():
#               resultadoFechaInicio = {'value': {'fechaHoraInicio': datetime.today()},
#               'warning': {'title': 'Fecha inicio incorrecta',
#                              'message': 'La fecha de inicio no puede ser anterior a la fecha y hora actual'}}
#          return resultadoFechaInicio

#    @api.onchange('fechaHoraFin')
#     def onchange_fechaHoraFin(self):
#          resultadoFechaFin = {}
#          if self.fechaHoraFin <= self.fechaHoraInicio:
#               resultadoFechaFin = {'value': {'fechaHoraFin': (datetime.today()+datetime.timedelta(days=1))},
#               'warning': {'title': 'Fecha fin incorrecta',
#                              'message': 'La fecha de fin no puede ser anterior o igual a la fecha de inicio'}}
#          return resultadoFechaFin"""