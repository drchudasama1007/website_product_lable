from odoo import api, fields, models, _

class ProductLabel(models.Model):
    _name = "product.label"

    name = fields.Char("Label Name")
    bg_color = fields.Char("HTML Background Color(eg, #FF0000)")
    font_color = fields.Char("HTML Font Color(eg, #000000)")


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_label_id = fields.Many2one(comodel_name="product.label", string="Product label")
