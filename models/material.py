# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
     _name = 'uposports.material'
     _description = 'Modulo para los materiales asociados a las instalaciones'

     name = fields.Char(string="Nombre", required=True, size=30, help="Nombre del material")
     descripcion = fields.Text(size=300)
     unidades = fields.Integer(required=True)

     instalacion_id = fields.Many2one("uposports.instalacion",string="Instalacion")

     _sql_constraints = [('material_name_unique', 'UNIQUE (name)', 'Compruebe el nombre del material, debe ser único.')]


#Se comprueba que las unidades sean mayor que 0, de lo contrario se informa del error y se establece a 0.
     @api.onchange('unidades')
     def onchange_unidades(self):
          resultadoUnidades = {}
          if self.unidades < 0:
               resultadoUnidades = {'value': {'unidades': 0},
               'warning': {'title': 'Unidades de material incorrecta',
                              'message': 'El número de unidades no puede ser negativo'}}
          return resultadoUnidades