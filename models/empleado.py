# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Empleado(models.Model):
     _name = 'uposports.empleado'
     _description = 'Modelo para los empleados'

     name = fields.Char(string="DNI", required=True, size=9, help="DNI del empleado")
     nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del empleado")
     apellidos = fields.Char(string="Apellidos", required=True, size=50, help="Apellidos del empleado")
     telefono = fields.Integer(string="Telefono", size=9, required=True)

     abono_id = fields.One2many("uposports.abono","empleado_id","Abonos creado por el empleado")

     _sql_constraints = [('empleado_name_unique', 'UNIQUE (name)', 'Compruebe el DNI, debe ser único.')]

#Validamos los campos de telefono y DNI. Si alguno es erroneo se muestra el mensaje correspondiente al querer guardar.
     @api.constrains('telefono','name')
     def _check_cliente(self):
          error=""
          hayerror=False
          letras='TRWAGMYFPDXBNJZSQVHLCKE'
          numeroDni=self.name[0:8]
          if len(str(self.telefono)) < 9:
               error=error + "El telefono debe tener 9 digitos\n"
               hayerror=True
          if str(self.telefono)[0:1]!='6' and str(self.telefono)[0:1]!='7':
               error=error + "El telefono debe empezar por 6 o 7\n"
               hayerror=True
          if(self.name[-1]!=letras[int(numeroDni)%23]):
               error=error + "El DNI es incorrecto\n"
               hayerror=True
          if(hayerror==True):
               raise models.ValidationError(error)
