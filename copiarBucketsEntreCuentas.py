def copiar_objetos(bucket_origen, region_origen, 
                   bucket_destino, region_destino, prefijo=""):
    import boto3
    from decouple import config

    cuentaOrigen = 'IDcuentaORIGEN'
    cuentaDestino = 'IDcuentaDESTINO'

    # Configuración de la sesión y cliente S3 para la cuenta de origen
    session_origen = boto3.Session(region_name=region_origen, profile_name=cuentaOrigen)
    s3 = session_origen.client('s3')


    # Configuración de la sesión y cliente S3 para la cuenta de destino

    session_destino = boto3.Session(region_name=region_destino, profile_name=cuentaDestino)
    s3_dest = session_destino.client('s3')

    # Listar y copiar
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_origen, Prefix=prefijo):
        for obj in page.get('Contents', []):
            copy_source = {'Bucket': bucket_origen, 'Key': obj['Key']}
            s3_dest.copy(copy_source, bucket_destino, obj['Key'])