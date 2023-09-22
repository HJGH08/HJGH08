from odoo import models, fields

class FingerprintRegistration(models.Model):
    _name = 'fingerprint.registration'
    _description = 'Fingerprint Registration'

    name = fields.Char(string="Name", required=True)
    fingerprint_data = fields.Binary(string="Fingerprint Data", required=True)
    user_id = fields.Many2one('res.users', string="User", required=True)

    # Otros campos y métodos del modelo

    def unlink(self):
        # Aquí puedes agregar lógica personalizada antes de eliminar el registro.
        # Por ejemplo, puedes realizar una verificación o realizar alguna acción adicional.

        # Llama al método original de eliminación para eliminar el registro
        return super(FingerprintRegistration, self).unlink()

