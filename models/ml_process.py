from odoo import fields, models


class MlProcess(models.Model):
	"""docstring for MlProcess"""
	
	_name = 'ml.process'
	_rec_name = 'process_cod'

	_sql_constraints = [
			('process_cod', 'unique(process_cod)', 'Please enter unique Process Code'),
    ]

	process_cod = fields.Char("Process code", size=2, required=True)
	process_description = fields.Char('Process description')
	process_process_line = fields.One2many('process.line', 'process_id', string='Process Line')
