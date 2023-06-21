{
    'name': "abc",
    'author': 'vicky',
    'version': '0.1',
    'depends':['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/member_views.xml',
        'report/report_member_views.xml',
        'views/report_accounting.xml',
        # 'views/report_cusomer_views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}