# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': 'Odoo POS Restaurant (Enterprise)',
    'version': '1.2.3',
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'summary': 'Odoo POS Restaurant',
    'description': "Odoo POS Restaurant",
    'category': 'Point Of Sale',
    'website': 'http://www.acespritech.com',
    'depends': ['base', 'web', 'bus', 'pos_restaurant', 'mrp',
        'sale_management', 'barcodes', 'purchase', 'hr_attendance', 'account'
    ],
    'price': 500.00,
    'currency': 'EUR',
    'images': [
        'static/description/main_screenshot.png',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/dummy_data.xml',
        'data/pos_cache_data.xml',
        'views/flexibite.xml',
        'views/res_config_settings.xml',
        'views/generate_product_ean13_view.xml',
        'views/point_of_sale.xml',
        'views/pos_config.xml',
        'views/res_config_settings.xml',
        'views/sale_view.xml',
        'views/pos_cache_views.xml',
        'views/product_view.xml',
        'views/account_view.xml',
        'views/res_company_view.xml',        
        'views/res_partner_view.xml',
        'views/gift_card.xml',
        'views/voucher_view.xml',
        'views/voucher_code_sequence.xml',
        'views/res_users_view.xml',
        'views/pos_sales_report_template.xml',
        'views/pos_sales_report_pdf_template.xml',
        'views/sales_details_pdf_template.xml',
        'views/sales_details_template.xml',
        'views/front_sales_report_pdf_template.xml',
        'views/front_sales_thermal_report_template.xml',
        'views/pos_report.xml',
        'reports.xml',
        'views/front_inventory_session_pdf_report_template.xml',
        'views/front_inventory_session_thermal_report_template.xml',
        'views/front_inventory_location_pdf_report_template.xml',
        'views/front_inventory_location_thermal_report_template.xml',
        'wizard/set_product_valid_days.xml',
        'wizard/wizard_pos_sale_report_view.xml',
        'wizard/wizard_sales_details_view.xml',
        'wizard/wizard_pos_x_report.xml',
        'views/pos_promotion_view.xml',
        'views/wallet_management_view.xml',
        'views/modifier_view.xml',
        'views/report_item_table_order.xml',
        'views/report_table_order.xml',
        'views/report_item_table_order1.xml',
        'views/report_table_order_receipt.xml',
        'views/pos_z_report_template.xml',
        'views/customer_display.xml',
        'views/stock_location_views.xml',
        'views/pos_store_view.xml',
        'views/delivery_order_screen.xml',
        'views/non_moving_product_report.xml',
        'wizard/non_moving_stock.xml',
        'wizard/wizard_pos_modify_payment_method.xml',
        'report/grp_category_product_expiry_report_template.xml',
        'wizard/product_expiry_report_wizard_view.xml',
        'views/product_expiry_report_view.xml',
        'data/send_mail.xml',

        # Direct Login Pull
        'views/webclient_templates.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
