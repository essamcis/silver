# -*- coding: utf-8 -*-
{
    'name': "Cheques managment ",

    'summary': """ Check Management Express """,

    'description': """
        This Module is used for check \n
        It includes creation of check receipt ,check cycle ,Holding ....... \n

    """,

    'author': "Mohamed abd elrhman 01128218762",
    'website': "",

    
    'category': 'native',
    'version': '12.0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],#' 'account_accountant', 'sale'

    # always loaded
    'data': [
        
        'security/ir.model.access.csv',
        'views/account_journal_view.xml',
        'views/checks_fields_view.xml',
        'views/check_payment.xml',
        'views/check_menus.xml',
        'wizard/check_cycle_wizard_view.xml',
        'views/payment_report.xml',
        'views/report_check_cash_payment_receipt_templates.xml',
        'security/check_security.xml',
         

    ],
    'qweb': [],
    # only loaded in demonstration mode
    'demo': [],
    'application': True,

}
