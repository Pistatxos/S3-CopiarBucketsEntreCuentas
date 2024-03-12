# S3-CopiarBucketsEntreCuentas
Puedes visitar el post en en tomonota.net

En esta repo te mostraré cómo copiar objetos de S3 de una cuenta de AWS a otra incluso en diferentes regiones de manera sencilla, como se  caracteriza TomoNota ;)

Para el que no conozca S3: Amazon Simple Storage Service (es de donde viene S3) es un servicio de almacenamiento de objetos que ofrece escalabilidad, disponibilidad de datos, seguridad y rendimiento. Es ideal para una amplia variedad de casos de uso, incluyendo sitios web, aplicaciones móviles, respaldo y restauración, archivado, aplicaciones empresariales, dispositivos IoT y análisis de big data, entre otros.

Para hacer la copia entre cuentas usaremos Cloudformation (un servicio de AWS que permite la creación y gestión de recursos a través de plantillas), y Python para llevar a cabo la copia entre cuentas.

Primero, ¿por qué plantillas? Porque una vez que eliminamos las plantillas, ¡también se eliminan los permisos asociados! Esto resulta en un proceso mucho más limpio y eficiente. Si estás interesado en profundizar sobre CloudFormation, te recomiendo visitar el post dedicado a este tema.

Pasos a seguir:
- Crear la plantilla para la "Cuenta Origen" y para ello necesitaremos la ID de la "Cuenta Destino".
- Crear la plantilla para la "Cuenta Destino" y para ello necesitaremos la ID de la "Cuenta Origen".
- Copiar los archivos con un script de python.

Empecemos!

Plantilla Origen:
Necesitarás la ID de la "Cuenta Destino". Aquí tienes un ejemplo de cómo crear una plantilla para la cuenta origen que configura las políticas del bucket para permitir el acceso a una cuenta específica:
Esta plantilla proporciona los permisos necesarios para listar y copiar archivos desde el bucket de origen. Puedes especificar rutas o archivos concretos según necesites. Para aplicar permisos a varios buckets, duplica BucketPolicy1 como BucketPolicy2, BucketPolicy3, etc., según lo necesites.


Plantilla Destino:
Aquí tienes un ejemplo para la cuenta destino, que básicamente invierte los roles de las cuentas en la plantilla anterior:
Esta plantilla da los permisos necesarios al bucket de destino que permite listar y copiar los archivos nuevos.


Script python para copiar:
El siguiente script Python utiliza la librería Boto3 para interactuar con AWS S3 y copiar objetos de un bucket a otro. Es importante configurar adecuadamente las sesiones para cada cuenta y especificar las regiones correspondientes.
Este código esta preparado para copiar los archivos, tenéis que adaptarlo adjuntando los datos necesarios
*Antes de ejecutar este script, asegúrate de tener configuradas las credenciales de AWS CLI para ambas cuentas. Si no sabes como puedes pasar por el post aws cli - Boto3 y credenciales en tomonota.net


Dale una estrella para seguir actualizando la repo.

Salu2!s