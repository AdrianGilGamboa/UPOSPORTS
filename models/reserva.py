# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class Reserva(models.Model):
     _name = 'uposports.reserva'
     _description = 'Modelo para las reservas de instalaciones'
     _rec_name = 'instalacion_id'

     name = fields.Integer(string="ID Reserva")
     fechaHoraInicio = fields.Datetime(string='Fecha/Hora Inicio', required=True, autodate = True, store=True, default = lambda self: datetime.datetime.today())
     fechaHoraFin = fields.Datetime(string='Fecha/Hora Fin', required=True, autodate = True, store=True, default = lambda self: datetime.datetime.today())

     instalacion_id = fields.Many2one("uposports.instalacion",string="Instalacion",required=True )
     cliente_id = fields.Many2one("uposports.cliente",string="Cliente",required=True)

#Se comprueba que la fecha de inicio no sea inferior a la fecha actual, de lo contrario se informa del error y se establece la fecha actual.
#Además, la fecha de fin se establece 1 hora más tarde.
     @api.onchange('fechaHoraInicio')
     def onchange_fechaHoraInicio(self):
          resultadoFechaIni = {}
          ahora = datetime.datetime.today()
          if self.fechaHoraInicio < ahora:
               resultadoFechaIni = {'value': {'fechaHoraInicio': ahora, 'fechaHoraFin':ahora+datetime.timedelta(hours=1)},
               'warning': {'title': 'Fecha inicio incorrecta',
                          'message': 'La fecha de inicio no puede ser anterior a la fecha y hora actual'}}
               
          else:
               self.fechaHoraFin = self.fechaHoraInicio+datetime.timedelta(hours=1)
          return resultadoFechaIni
          
#Se comprueba que la fecha de fin sea mayor que la fecha de inicio, en caso contrario se informa del error y se establece 1 hora más tarde de la fecha de inicio.
     @api.onchange('fechaHoraFin')
     def onchange_fechaHoraFin(self):
          resultadoFechaFin = {}
          if self.fechaHoraFin <= self.fechaHoraInicio:
               resultadoFechaFin = {'value': {'fechaHoraFin': self.fechaHoraInicio+datetime.timedelta(hours=1)},
               'warning': {'title': 'Fecha fin incorrecta',
                          'message': 'La fecha de fin no puede ser anterior o igual a la fecha de inicio'}}
          return resultadoFechaFin