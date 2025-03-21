# herencia multiple:herencia múltiple porque una clase ("clase hija")
#  hereda características (atributos y métodos) de dos o más clases ("clases padre"). 
# Esto permite combinar funcionalidades de diferentes clases base en una sola clase, 
# creando así objetos que pueden realizar acciones y tener atributos provenientes de múltiples fuentes.
#  Por ejemplo, la clase "ReproductorAlmacenamiento" hereda de "ReproductorAudio" y "DispositivoAlmacenamiento", 
# lo que le permite reproducir audio y almacenar datos, combinando ambas funcionalidades.
class ReproductorAudio:
    def reproducir(self, archivo):
        return f"Reproduciendo: {archivo}"

class DispositivoAlmacenamiento:
    def almacenar(self, datos):
        return f"Almacenando datos: {datos}"

class ReproductorAlmacenamiento(ReproductorAudio, DispositivoAlmacenamiento):
    def gestionar_archivos(self, archivo, datos):
        reproduccion = self.reproducir(archivo)
        almacenamiento = self.almacenar(datos)
        return f"{reproduccion}\n{almacenamiento}"

# Crear una instancia de ReproductorAlmacenamiento
dispositivo_multifuncional = ReproductorAlmacenamiento()

# Usar métodos de ambas clases padre y el método propio
archivo_ejemplo = "cancion.mp3"
datos_ejemplo = {"nestorcito": "Banda sistemas 1", "duracion": "3:45"}
resultado = dispositivo_multifuncional.gestionar_archivos(archivo_ejemplo, datos_ejemplo)
print(resultado)