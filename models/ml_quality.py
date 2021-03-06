import fdb
from odoo import models, fields, api, exceptions


class MlQuality(models.Model):
	"""docstring for MlQuality"""

	_name = 'ml.quality'
	_description = 'Quality Module'
	_rec_name = 'product_code'


	_sql_constraints = [
			('product_code', 'unique(product_code)', 'Please enter unique Product Code'),
    ]

	product_code = fields.Integer('Product Code', required=True)
	product_refcli = fields.Char('Product Ref. Client')
	product_process_line = fields.One2many('process.line', 'product_code_id', string='Process Line')
	product_cli_name = fields.Char('Client', readonly=True)

	@api.model
	def create(self, vals):
		gestor_values = self.search_product(vals.get('product_code'))
		product_values = self.return_process_as_list(gestor_values['process_ids'])
		process_list = []
		new_vals = vals

		for a in product_values:
			process_list.append((0,0,{'product_code_id': vals.get(id), 'process_id': int(a)}))

		if len(gestor_values) != 0:
			new_vals['product_code'] = gestor_values['product_code']
			new_vals['product_refcli'] = gestor_values['product_refcli']
			new_vals['product_process_line'] = process_list
			new_vals['product_cli_name'] = gestor_values['product_cli_name']
			return super(MlQuality, self).create(new_vals)
		else:
			raise exceptions.UserError('Product code not found!')

		
	# @api.multi
	# def write(self, vals):
	# 	res = vals
	# 	product = self.get_product()
	# 	gestor_values = self.search_product(str(product))
	# 	product_values = self.return_process_as_list(gestor_values['process_ids'])
	# 	process_list = []

	# 	for a in product_values:
	# 		process_list.append((0,0,{'product_code_id': vals.get(id), 'process_id': int(a)}))
	
	# 	if len(gestor_values) != 0:
	# 		res['product_code'] = gestor_values['product_code']
	# 		res['product_refcli'] = gestor_values['product_refcli']	
	# 		res['product_process_line'] = process_list	
	# 		res['product_cli_name'] = gestor_values['product_cli_name']				
	# 	else:
	# 		raise exceptions.UserError('Product code not found!')
		
	# 	return super(MlQuality, self).write(res)


	@api.multi
	def get_product(self):
		for res in self:
			product = res.product_code
		return product


	def search_product(self, product):
		"""
		function get values from database "Gestor"
		Args:
			product (str): value from user insertion.
		Returns:
			product_values (dic): return dictionary {product_code: (int), product_refcli: (str), process_ids: (str)}
		"""

		product_values = {}

		con = fdb.connect(
        	host='192.168.23.2',
        	database='/Datos/gdb/gestor.gdb',
        	user='SYSDBA',
        	password='masterkey',
        	charset='iso8859_1'
		)

		cur = con.cursor()

		cur.execute("""
               SELECT a.REF_N, a.REF_C, a.RUTA_A_SEGUIR, b.NOM FROM PIEZAS AS a
               INNER JOIN CLIENTES AS b
               ON a.CODCLIENTE = b.CODIGO
               WHERE a.REF_N = """ + str(product)
        )

		for value in cur:
			product_values = {
				'product_code': value[0],
				'product_refcli': value[1],
				'process_ids': value[2],
				'product_cli_name': value[3]
			}

		return product_values


	def return_process_as_list(self, process):
		"""
		function get process values is returns process id 
		Args:
			process (str): value from database search.
		Returns:
			process_id_list (list): return a ids list (int)
		"""
		process_list = []
		process_id_list = []

		for value in range(0, len(process), 2):
			process_list.append(process[value:value+2])

		for process_id in process_list:
			id_process = self.env['ml.process'].search([('process_cod', '=', process_id)])
			for ids in id_process:
				process_id_list.append(int(ids.id))

		return process_id_list