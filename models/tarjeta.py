# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Modelo heredado de pago mediante herencia por prototipo.
#Este modelo tiene su propia base de datos con sus datos independientes del modelo padre.

class Tarjeta(models.Model):
     _inherit = 'uposports.pago'
     _name = 'uposports.tarjeta'
     _description = 'Modelo heredado por prototipo de pago para los pagos con tarjeta.'

     entidadBancaria=fields.Char(string="Entidad Bancaria",size=30,required=True)


     def btn_report_tarjeta_graph(self):
          return self.env.ref('uposports.tarjeta_report_graph').report_action(self)

     def btn_report_tarjeta_text(self):
          return self.env.ref('uposports.tarjeta_report_text').report_action(self)
     