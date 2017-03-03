from odoo import fields, models


class MlRoutes(models.Model):
	"""docstring for MlProcess"""
	
	_name = 'ml.routes'

	process_cod = fields.Char("Process code", size=2, required=True)
	process_description = fields.Char('Process description')