from odoo import fields, models


class ProcessLine(models.Model):
	"""docstring for ProcessLine"""
	_name = 'process.line'
	_rec_name = 'process_id'

	process_line = fields.One2many('quality.dimensions', 'quality_dimensions_id', string='Dimensions check')
	product_code_id = fields.Many2one('ml.quality', string='Product Line')
	process_id = fields.Many2one('ml.process', string='Process Code')
