# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Overlay for Poland - Accounting',
    'version' : '1.0',
    'author': 'myOdoo.pl',
    'website': 'https://myodoo.pl',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
    This is the overaly module to manage the accounting chart and taxes for Poland in Odoo.

    """,
    'depends' : [
        'account',
        'l10n_pl',
    ],
    'data': [    
        'data/account_account_update.xml',   
        'data/accounting_tags.xml',
        'data/account_tax_report_data_update.xml',
        'data/account_fiscal_position_data_update.xml',
        'data/account_tax_data_update.xml',
        'data/account_tax_group_data_update.xml',   
    ],
 
}
