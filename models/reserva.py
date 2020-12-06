# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class Reserva(models.Model):
     _name = 'uposports.reserva'
     _description = 'Modelo para las reservas de instalaciones'
     _rec_name = 'instalacion_id'

     fechaHoraInicio = fields.Datetime(string='Fecha/Hora Inicio', required=True, autodate = True, store=True, default = lambda self: datetime.datetime.today().timedelta(seconds=5))
     fechaHoraFin = fields.Datetime(string='Fecha/Hora Fin', required=True, autodate = True, store=True, default = lambda self: datetime.datetime.today().timedelta(hours=1))
     state = fields.Selection([('completado','Completado'),
                                     ('pendiente','Pendiente'),
                                     ('cancelado','Cancelado'),],
                                     'Estado', default='pendiente')
     instalacion_id = fields.Many2one("uposports.instalacion",string="Instalacion",required=True )
     cliente_id = fields.Many2one("uposports.cliente",string="Cliente",required=True)


     def btn_submit_to_cancelado(self):
          if self.state=='pendiente':
               self.write({'state':'cancelado'})
          else:
               raise models.ValidationError('La reserva no puede ser cancelada porque ya ha sido completada.')


     def btn_submit_to_completado(self):
          if self.state=='pendiente':
               self.write({'state':'completado'})
          else:
               raise models.ValidationError('La reserva no puede ser completada porque ya ha sido cancelada.')


#Validamos antes de guardar los datos comprobamos:
# 1. Fecha de inicio no puede ser inferior a la fecha y hora actual.
# 2. Fecha de inicio no puede ser superior o igual a la fecha y hora de fin.
# 3. La duracion maxima de la reserva es de 3 horas.
     @api.constrains('fechaHoraInicio')
     def _check_fechaHoraInicio(self):
          if self.fechaHoraInicio < datetime.datetime.today():
               raise models.ValidationError('La fecha de inicio no puede ser anterior a la fecha y hora actual.')
          if self.fechaHoraInicio >= self.fechaHoraFin:
               raise models.ValidationError('La fecha de inicio no puede ser superior a la fecha y hora de fin.')
          if self.fechaHoraFin > self.fechaHoraInicio+datetime.timedelta(hours=3):
               raise models.ValidationError('Las reservas no pueden superar las 3 horas de duración.')
  

#Se comprueba que la fecha de fin sea mayor que la fecha de inicio, en caso contrario se informa del error y se establece 1 hora más tarde de la fecha de inicio.
     @api.onchange('fechaHoraFin')
     def onchange_fechaHoraFin(self):
          resultadoFechaFin = {}
          if self.fechaHoraFin <= self.fechaHoraInicio:
               resultadoFechaFin = {'value': {'fechaHoraFin': self.fechaHoraInicio+datetime.timedelta(hours=1)},
               'warning': {'title': 'Fecha fin incorrecta',
                          'message': 'La fecha de fin no puede ser anterior o igual a la fecha de inicio'}}
          return resultadoFechaFin