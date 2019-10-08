# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

##############################################################################
#
#
#    Copyright (C) 2018-TODAY .
#    Author: Eng.Ramadan Khalil (<rkhalil1990@gmail.com>)
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
##############################################################################

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError,UserError



class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    draft_number=fields.Char(string='Draft Number')

