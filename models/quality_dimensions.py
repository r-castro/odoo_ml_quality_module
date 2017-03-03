from odoo import fields, models


class QualityDimensions(models.Model):
	"""docstring for ProcessLine"""
	_name = 'quality.dimensions'

	dimensions_check = fields.Char('Dimension Tag', required=True)
	quality_dimensions_id = fields.Many2one('process.line', string='Dimensions id')
