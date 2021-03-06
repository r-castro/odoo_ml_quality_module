from odoo import fields, models


class QualityDimensions(models.Model):
	""" docstring for ProcessLine
		Class model for process for dimensions per line  
	"""
	_name = 'quality.dimensions'

	dimensions_check = fields.Char('Tag', required=True)
	dim_especified = fields.Char('Dim. Especificada')
	quality_dimensions_id = fields.Many2one('process.line', string='Dimensions id')

