# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Modelo heredado de pago mediante herencia por prototipo.
#Este modelo tiene su propia base de datos con sus datos independientes del modelo padre.

class Efectivo(models.Model):
    _inherit = 'uposports.pago'
    _name = 'uposports.efectivo'
    _description = 'Modelo heredado por prototipo de pago para los pagos en efectivo.'


    importeAbonado = fields.Float(string="Dinero entregado (€)",required=True)
    importeDevuelto = fields.Float(string="Cambio (€)*")

#Se comprueba que el importe abonado sea mayor o igual que el importe a pagar y se calcula el cambio.
    @api.onchange('importeAbonado')
    def onchange_importeAbonadoCorrecto(self):
        if self.importeAbonado >= self.cantidad:
    	    self.importeDevuelto = self.importeAbonado-self.cantidad

#En el caso de que el importe abonado sea menor que el importe a pagar, se informa del error y se establece al mismo valor del precio del abono.
    @api.onchange('importeAbonado')
    def onchange_importeAbonadoIncorrecto(self):
    	resultado = {}
    	if self.importeAbonado < self.cantidad:
    		resultado = {'value': {'importeAbonado': self.cantidad},
    		'warning': {'title': 'Importe abonado incorrecto',
    					'message': 'El importe abonado debe ser mayor o igual al precio del abono'}}
    	return resultado

    def btn_report_efectivo_graph(self):
        return self.env.ref('uposports.efectivo_report_graph').report_action(self)

    def btn_report_efectivo_text(self):
        return self.env.ref('uposports.efectivo_report_text').report_action(self)