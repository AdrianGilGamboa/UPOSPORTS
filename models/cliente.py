# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
     _name = 'uposports.cliente'
     _description = 'Modelo para los clientes'

     name = fields.Char(string="DNI", required=True, size=9, help="Documento identificativo")
     nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del cliente")
     apellidos = fields.Char(string="Apellidos",required=True, size=50, help="Apellidos del cliente")
     telefono = fields.Integer(string="Telefono", required=True, size=9, help="Número de teléfono móvil")
     codigoPostal = fields.Integer(string="Codigo Postal",required=True, size=5, help="Codigo Postal")
 

     abono_id=fields.Many2one('uposports.abono',string="Abono del cliente",required=True)
     reserva_id=fields.One2many('uposports.reserva',"cliente_id","Reservas del cliente")
     pago_id=fields.One2many("uposports.pago","cliente_id","Pagos del cliente")
    	
     _sql_constraints = [('cliente_name_unique', 'UNIQUE (name)', 'Compruebe el DNI, debe ser único.')]
                 
                    

     def btn_pago_tarjeta(self):
          return {
                    "type": "ir.actions.act_window",
                    "res_model": "uposports.tarjeta",
                    "views": [[False, "form"]],
                    "target": "new",
                    "context":{
                              "default_entidadBancaria":self.name                           }
                    }    

     def btn_pago_efectivo(self):
          return {
                    "type": "ir.actions.act_window",
                    "res_model": "uposports.efectivo",
                    "views": [[False, "form"]],
                    "target": "new",
                    "context":{
                              "default_cliente_id":self.name                           }
                    }
