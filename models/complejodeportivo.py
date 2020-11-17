# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ComplejoDeportivo(models.Model):
     _name = 'uposports.complejodeportivo'
     _description = 'uposports ComplejoDeportivo'

     abono_id=fields.One2many('uposports.abono',"complejoDeportivo_id","Abonos")
     reserva_id=fields.One2many('uposports.reserva',"complejoDeportivo_id","Reservas del cliente")