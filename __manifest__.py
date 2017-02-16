{
	'name': "ML Quality",
	'summary': "General services",
	'description': """Quality Module""",
	'author': "Rodrigo de Castro",
	'license': "AGPL-3",
	'website': "http://www.megalaser.com.br",
	'category': 'Others',
	'version': '10.0.1.0.0',
	'depends': ['base', 'report'],
	'data': [
		'views/ml_quality.xml',
		'reports/ml_one_report.xml',
		'reports/ml_template_header.xml'
	],
	'demo': [],
	"active": True,
    "installable": True,
    'application': True,
}