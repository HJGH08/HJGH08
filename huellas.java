import com.digitalpersona.onetouch.*;
import com.digitalpersona.onetouch.processing.*;

public class FingerprintRegistration {

    public static void main(String[] args) {
        try {
            // Inicializar el motor de huellas digitales
            DPFPGlobal.initialize();

            // Crear un objeto de captura de huellas
            DPFPEnrollment enrollment = DPFPGlobal.getEnrollmentFactory().createEnrollment();

            System.out.println("Coloca tu dedo en el escáner para registrar la huella...");

            while (enrollment.getFeaturesNeeded() > 0) {
                // Capturar la imagen de la huella
                DPFPFeatureSet features = DPFPGlobal.getFeatureSetFactory().createFeatureSet();
                // Aquí deberías obtener los datos de la huella desde tu escáner
                // Por ejemplo: features = captureFingerprint();

                if (features != null) {
                    try {
                        // Agregar la huella al proceso de registro
                        enrollment.addFeatures(features);
                    } catch (DPFPImageQualityException e) {
                        System.err.println("Calidad de imagen insuficiente. Vuelve a intentarlo.");
                    }
                }
            }

            // Finalizar el proceso de registro
            DPFPVerificationResult verificationResult = enrollment.getTemplateStatus();
            if (verificationResult == DPFPVerificationResult.vrfTemplateStatus) {
                // Huella registrada con éxito
                DPFPFeatureSet template = enrollment.getTemplate();
                // Aquí puedes guardar el template en tu base de datos o hacer lo que necesites
                System.out.println("Huella registrada exitosamente.");
            } else {
                System.err.println("Registro de huella fallido. Intenta nuevamente.");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
