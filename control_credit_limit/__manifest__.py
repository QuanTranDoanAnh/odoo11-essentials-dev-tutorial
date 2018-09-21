{
    'name': "Control the Credit Limit",
    'summary': "Allows a credit limit to be set for partners",
    'description': """
        This plugin can be used to limit the allowable credit for a partner can have. 
  All new credit transactions are checked against the credit limit and the accumulated owed credit to validate new sale
    """,
    'author': "QuanTDA1",
    'website': "http://www.bld.com.vn",
    'category': "Partner",
    'version': "1.0",
    'depends': ['account', 'sale'],
    'data': [
        'views/partner_credit_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}