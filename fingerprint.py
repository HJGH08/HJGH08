from odoo import models, fields, api


class Fingerprint(models.Model):
    _name = 'registro.huellas.fingerprint'
    _description = 'Modelo para el Registro de Huellas'

    # 'Modelo de Registro de Huellas'
    name = fields.Char(string='Nombre')
    fingerprint_data = fields.Binary(string='foto de la persona')
    fingerprint_dat = fields.Binary(string='foto')
    fingerprint_adata = fields.Binary(string='huella')
    huella_derecha = fields.Binary(string='pulgar derecho')
    huella_izquierda = fields.Binary(string='pulgar izquierdo')
    user_id = fields.Many2one('res.users', string='Usuario')

# 'Datos de la Huella

    def action_huella(self):
        for record in self:

            print(f"Procesando huella para el registro {record.name}")
# Lógica para procesar la huella
# Por ejemplo, enviarla a un servicio externo para verificación
# o realizar alguna acción basada en la huella registrada
