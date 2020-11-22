# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Efectivo(models.Model):
    _inherit = 'uposports.pago'
    _name = 'uposports.efectivo'



    importeAbonado = fields.Float(string="Dinero entregado (€)",required=True)
    importeDevuelto = fields.Float(string="Dinero a devolver (€)",readonly=1)

      

    @api.onchange('importeAbonado')
    def onchange_importeAbonadoCorrecto(self):
        if self.importeAbonado >= self.cantidad:
    	    self.importeDevuelto = self.importeAbonado-self.cantidad

    @api.onchange('importeAbonado')
    def onchange_importeAbonadoIncorrecto(self):
    	resultado = {}
    	if self.importeAbonado < self.cantidad:
    		resultado = {'value': {'importeAbonado': self.cantidad},
    		'warning': {'title': 'Importe abonado incorrecto',
    					'message': 'El importe abonado debe ser mayor o igual al precio del abono'}}
    	return resultado