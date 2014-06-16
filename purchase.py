# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
from openerp.tools.translate import _
from datetime import date
from datetime import datetime
from openerp import netsvc


class purchase_order(osv.osv):
	_name = 'purchase.order'
	_inherit = 'purchase.order'

	_columns = {
		'recommendation_ids': fields.one2many('purchase.order.recommendation','order_id','Recomendaciones'),
		}


	def lote_recommendations(self, cr, uid, ids, context=None):
		# import pdb;pdb.set_trace()
		purchase_obj = self.browse(cr,uid,ids)
		if purchase_obj[0].partner_id.id and purchase_obj[0].lote_id.id:
			for product in purchase_obj[0].lote_id.product_ids:
				vals_recommendation = {
					'order_id': purchase_obj[0].id,
					'product_id': product.id,
					}
				return_id = self.pool.get('purchase.order.recommendation').create(cr,uid,vals_recommendation)
		return None


purchase_order()

class purchase_order_recomendations(osv.osv):
	_name = 'purchase.order.recommendation'
	_description = 'Recomendations to POs'

	_columns = {
		'order_id': fields.many2one('purchase.order','Pedido'),
		'product_id': fields.many2one('product.product','Producto'),
		'product_new': fields.related('product_id','producto_nuevo',type='boolean',string='Producto Nuevo'),
		}

purchase_order_recomendations()

# vim:expandtab:smartindent:tabstop=4:softtabstop4:shiftwidth=4:

