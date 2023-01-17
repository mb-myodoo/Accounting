# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


VAT_MAP = {
    #DOMESTIC
    #VAT 23%
    'l10n_pl.1_vs_kraj_23': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_KR23', '+Podstawa - Dostawa towarów/usług, kraj, 22% lub 23%'],
        100: ['P_S_KR23', '+Podatek - Dostawa towarów/usług, kraj, 22% lub 23%']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_KR23', '-Podstawa - Dostawa towarów/usług, kraj, 22% lub 23%'],
        100: ['P_S_KR23', '-Podatek - Dostawa towarów/usług, kraj, 22% lub 23%']
        }      
    },
    'l10n_pl.1_vz_kraj_23': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych']
        }      
    },
    #VAT 8%
    'l10n_pl.1_vs_kraj_8': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_KR8', '+Podstawa - Dostawa towarów/usług, kraj, 7% lub 8%'],
        100: ['P_S_KR8','+Podatek - Dostawa towarów/usług, kraj, 7% lub 8%']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_KR8', '-Podstawa - Dostawa towarów/usług, kraj, 7% lub 8%'],
        100: ['P_S_KR8', '-Podatek - Dostawa towarów/usług, kraj, 7% lub 8%']
        }      
    },
    'l10n_pl.1_vz_kraj_8': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych']
        }       
    },
    #VAT 5%
    'l10n_pl.1_vs_kraj_5': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_KR5', '+Podstawa - Dostawa towarów/usług, kraj, 3% lub 5%'],
        100: ['P_S_KR5', '+Podatek - Dostawa towarów/usług, kraj, 3% lub 5%']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_KR5', '-Podstawa - Dostawa towarów/usług, kraj, 3% lub 5%'],
        100: ['P_S_KR5', '-Podatek - Dostawa towarów/usług, kraj, 3% lub 5%']
        }      
    },
    'l10n_pl.1_vz_kraj_5': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych']
        }      
    },
    #VAT 0%
    'l10n_pl.1_vs_kraj_0': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_KR0', '+Podstawa - Dostawa towarów/usług, kraj, 0%'],
        100: []
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_KR0', '-Podstawa - Dostawa towarów/usług, kraj, 0%'],
        100: []
        }      
    },
    'l10n_pl.1_vz_kraj_0': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych'],
        100: []
        },
        'refund_repartition_line_ids' : {
        'base': ['N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych'],
        100: []
        }      
    }, 
    # #VAT 0% Zwrot podróżnych 
    # 'l10n_pl.1_vs_zwrot_podróżnych_0': { 
    #     'invoice_repartition_line_ids' : {
    #     'base': ['+Podstawa - W tym towary art 129'],
    #     'tax': []
    #     },
    #     'refund_repartition_line_ids' : {
    #     'base': ['-Podstawa - W tym towary art 129'],
    #     'tax': []
    #     }      
    # }, 
    #VAT ZW 
    'l10n_pl.1_vs_kraj_zw': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_KRZW', '+Podstawa - Dostawa towarów/usług, kraj, zwolnione'],
        100: []
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_KRZW', '-Podstawa - Dostawa towarów/usług, kraj, zwolnione'],
        100: []
        }      
    },
    'l10n_pl.1_vz_kraj_zw': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych']
        }       
    },
    #VAT SERVICE 23% 
    'l10n_pl.1_vs_kraj_usl_23': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_KR23', '+Podstawa - Dostawa towarów/usług, kraj, 22% lub 23%'],
        100: ['P_S_KR23', '+Podatek - Dostawa towarów/usług, kraj, 22% lub 23%']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_KR23', '-Podstawa - Dostawa towarów/usług, kraj, 22% lub 23%'],
        100: ['P_S_KR23', '-Podatek - Dostawa towarów/usług, kraj, 22% lub 23%']
        }      
    },
    'l10n_pl.1_vz_kraj_usl_23': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych']
        }          
    },
    
    #VEHICLE LEASING
    'l10n_pl.1_vp_leas_sale': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych'],
        60: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych'],
        40:[]
        },
        'refund_repartition_line_ids' : {
        'base': ['N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych'],
        60: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych'],
        40: []
        }          
    },
    'l10n_pl.1_vp_leas_purchase': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych'],
        60: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych'],
        40: []
        },
        'refund_repartition_line_ids' : {
        'base': ['N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych'],
        60: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych'],
        40: []
        }          
    },
    
    #STEEL TRADE
    'l10n_pl.1_vs_stal': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_DT-pod-nab', '+Podstawa - Dostawa towarów, podatnik nabywca'],
        100: []
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_DT-pod-nab', '-Podstawa - Dostawa towarów, podatnik nabywca'],
        100: []
        }          
    },
    'l10n_pl.1_vz_stal': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_Z_POZ', 'N_S_DT-pod-nab', '+Podstawa - Nabycie towarów i usług pozostałych', '+Podstawa - Dostawa towarów, podatnik nabywca'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_DT-pod-nab', '+Podatek - Dostawa towarów, podatnik nabywca']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_Z_POZ', 'N_S_DT-pod-nab', '-Podstawa - Nabycie towarów i usług pozostałych', '-Podstawa - Dostawa towarów, podatnik nabywca'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_DT-pod-nab', '-Podatek - Dostawa towarów, podatnik nabywca']
        }          
    },
    #UE
    #UE GOODS
    'l10n_pl.1_vs_unia': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_WDT', '+Podstawa - Wew-wspól dostawa towarów'],
        100: []
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_WDT', '-Podstawa - Wew-wspól dostawa towarów'],
        100: []
        }      
    }, 
    'l10n_pl.1_vz_unia': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_WNT', 'N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych', '+Podstawa - Wewn-wspól. nabycie towarów'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_WNT', '+Podatek - Podatek - Wewn-wspól. nabycie towarów']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_WNT', 'N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych', '-Podstawa - Wewn-wspól. nabycie towarów'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_WNT', '-Podatek - Podatek - Wewn-wspól. nabycie towarów']
        },     
    }, 
    #UE SERVICES
    'l10n_pl.1_vs_dostu': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_D-EX', 'N_S_D-UE' '+Podstawa - W tym usługi art 100.1.4'],
        100: []
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_D-EX', 'N_S_D-UE', '-Podstawa - W tym usługi art 100.1.4'],
        100: []
        }      
    }, 
    'l10n_pl.1_vz_unia': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_IUzUE', 'N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych', '+Podstawa - W tym nabycie wg art 28b'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_IUzUE', '+Podatek - W tym nabycie wg art 28b']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_IUzUE', 'N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych', '-Podstawa - W tym nabycie wg art 28b'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_IUzUE', '-Podatek - W tym nabycie wg art 28b']
        },     
    }, 
    
    #EXPORT
    #EX GOODS
    'l10n_pl.1_vs_eksp_tow': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_EXT', '+Podstawa - Eksport towarów'],
        100: []
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_EXT', '-Podstawa - Eksport towarów'],
        100: []
        }      
    }, 
    'l10n_pl.1_vz_imp_tow': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_IUpUE', 'N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych', '+Podstawa - Import towarów art. 33a'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_IUpUE', '+Podatek - Import towarów art. 33a']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_IUpUE', 'N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych', '-Podstawa - Import towarów art. 33a'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_IUpUE', '-Podatek - Import towarów art. 33a']
        },
    },
    #EX SERVICES
    'l10n_pl.1_vs_ekspu': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_D-EX', '+Podstawa - Dostawa towarów/usług, poza kraj'],
        100: []
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_D-EX', '-Podstawa - Dostawa towarów/usług, poza kraj'],
        100: []
        }      
    },
    'l10n_pl.1_vz_impu': { 
        'invoice_repartition_line_ids' : {
        'base': ['N_S_IUpUE', 'N_Z_POZ', '+Podstawa - Nabycie towarów i usług pozostałych', '+Podstawa - Import usług'],
        100: ['P_Z_POZ', '+Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_IUpUE', '+Podatek - Import usług']
        },
        'refund_repartition_line_ids' : {
        'base': ['N_S_IUpUE', 'N_Z_POZ', '-Podstawa - Nabycie towarów i usług pozostałych', '-Podstawa - Import usług'],
        100: ['P_Z_POZ', '-Podatek - Nabycie towarów i usług pozostałych'],
        -100: ['P_S_IUpUE', '-Podatek - Import usług']
        }
    }}

    
class AccountTax(models.Model):
    _inherit = 'account.tax'
    
    def update_tax(self):
        for tax_ref in VAT_MAP.keys():
            tax = self.env.ref(tax_ref)
            for line in tax.invoice_repartition_line_ids:
                if line.repartition_type == 'base':
                    tag_names = VAT_MAP[tax_ref]['invoice_repartition_line_ids'][line.repartition_type]
                else: 
                    tag_names = VAT_MAP[tax_ref]['invoice_repartition_line_ids'][line.factor_percent]
                line.tag_ids = [(6,0,self.env['account.account.tag'].search([('name', 'in', tag_names)]).ids)]
                  
            for line in tax.refund_repartition_line_ids:
                if line.repartition_type == 'base':
                    tag_names = VAT_MAP[tax_ref]['invoice_repartition_line_ids'][line.repartition_type]
                else: 
                    tag_names = VAT_MAP[tax_ref]['invoice_repartition_line_ids'][line.factor_percent]
                line.tag_ids = [(6,0,self.env['account.account.tag'].search([('name', 'in', tag_names)]).ids)]
                
            
             