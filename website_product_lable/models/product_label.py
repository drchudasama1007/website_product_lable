from odoo import api, fields, models, _

class ProductLabel(models.Model):
    _name = "product.label"

    name = fields.Char("Label Name")
    bg_color = fields.Char("Background Color")
    font_color = fields.Char("Font Color")


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_label_id = fields.Many2one(comodel_name="product.label", string="Product label")
