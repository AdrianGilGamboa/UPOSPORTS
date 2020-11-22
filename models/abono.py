# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Abono(models.Model):
     _name = 'uposports.abono'
     _description = 'uposports Abono'

     precio = fields.Float(string="Precio (€)",required=True)
     name = fields.Char(string="Tipo", required=True, size=30,help="Nombre identificativo del abono")
     duracion = fields.Integer(string="Duracion (meses)", required=True, help="Duración en meses del abono",default=1)
    

     empleado_id = fields.Many2one("uposports.empleado",string="Creado por el empleado(DNI)", required=True)
     cliente_id =  fields.One2many("uposports.cliente","abono_id","Cliente")
     pago_id=fields.One2many("uposports.pago","abono_id","Pagos del abono")

     @api.onchange('precio')
     def onchange_precio(self):
          resultadoPrecio = {}
          if self.precio < 0:
               resultadoPrecio = {'value': {'precio': 0.00},
               'warning': {'title': 'Precio abono incorrecto',
                              'message': 'El precio del abono no puede ser negativo'}}
          return resultadoPrecio

     @api.onchange('duracion')
     def onchange_duracion(self):
          resultadoDuracion = {}
          if self.duracion < 1:
               resultadoDuracion = {'value': {'duracion': 1},
               'warning': {'title': 'Duración abono incorrecto',
                              'message': 'La duración del abono no puede ser menor a 1 mes'}}
          return resultadoDuracion
