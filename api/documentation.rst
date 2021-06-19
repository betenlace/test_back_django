=======================
    Recurso Usuario
=======================

Recurso POST
    
    .. http:post:: /api/user

    * ** Campos Obligatorios**

        :name: **(string)** Nombre del Usuario
        :doc: **(string)** Numero de identificacion 
        :profile: **(string)** Perfil del usuario

    * **Ejemplo de petición**

        .. sourcecode:: http

            POST /api/user HTTP/1.1
            Content-Type: application/json

            {
                "name": "Cuarentino",
                "doc": "1234567894",
                "profile": "admin"
            }
    
    * **Ejemplos de respuesta**

        .. sourcecode:: http

            HTTP/1.1 201 CREATED
            {
                "inserted":1
            }

    :status 201: Empresa creado
    :status 400: Cuerpo con estructura inválida