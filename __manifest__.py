{
    'name': 'Módulo de Registro de Huellas',
    'version': '1.0',
    'summary': 'Módulo para el registro de huellas biométricas',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/fingerprint_view.xml',
        'views/mi_modelo_views.xml',
        'views/registration.xml',
    ],
}
