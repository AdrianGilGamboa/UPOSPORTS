# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
     _name = 'uposports.cliente'
     _description = 'uposports Cliente'

     dni = fields.Char(string="DNI",required=True, help="Documento identificativo")
     nombre = fields.Char(string="Nombre",required=True, help="Nombre del clente")
     apellidos = fields.Char(string="Apellidos",required=True, help="Apellidos del cliente")
     telefono = fields.Integer(("Telefono"), required=True, help="Número de teléfono móvil")
     codigoPostal = fields.Integer("Codigo Postal",required=True, help="Codigo Postal")

     abono_id=fields.Many2one('uposports.abono',string="Abono actual del cliente",required=True)
     reserva_id=fields.Many2one('uposports.reserva',string="Reservas del cliente")