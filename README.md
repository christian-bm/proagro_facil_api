# Proagro facil API

## Métodos

Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais comunicação de perda. |
| `POST` | Utilizado para criar uma nova comunicação de perda. |
| `PUT` | Atualiza dados de uma comunicação de perda. |
| `PATCH` | Atualiza dados de uma comunicação de perda. |
| `DELETE` | Remove uma comunicação de perda do sistema. |

#

## [``GET``] /api/losses/

-   Request (application/json)

    -   Body

-   Response 200 (application/json)

    -   Body
        ```
        {
            "count": 123,
            "next": "http://api.example.org/accounts/?page=4",
            "previous": "http://api.example.org/accounts/?page=2",
            "results": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "first_name": "string",
                    "last_name": "string",
                    "email": "user@example.com",
                    "cpf": "string",
                    "latitude": "string",
                    "longitude": "string",
                    "farming_type": "string",
                    "harvest_date": "2022-08-31",
                    "event_type": "chuva excessiva",
                    "create_at": "2022-08-31T17:30:44.595Z",
                    "update_at": "2022-08-31T17:30:44.595Z"
                },
                ...
            ]
        }
        ```
#
## [``POST``] /api/losses/

-   Request (application/json)

    -   Body
        ```
        {
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "cpf": "string",
            "latitude": "string",
            "longitude": "string",
            "farming_type": "string",
            "harvest_date": "2022-08-31",
            "event_type": "chuva excessiva"
        }
        ```
#
-   Response 201 (application/json)

    - Body
        ```
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "cpf": "string",
            "latitude": "string",
            "longitude": "string",
            "farming_type": "string",
            "harvest_date": "2022-08-31",
            "event_type": "chuva excessiva",
            "create_at": "2022-08-31T17:35:12.515Z",
            "update_at": "2022-08-31T17:35:12.515Z"
        }
        ```
#
## [``GET``] /api/losses/{loss_id}/

-   Request (application/json)

    -   Body

-   Response 200 (application/json)

    -   Body
        ```
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "cpf": "string",
            "latitude": "string",
            "longitude": "string",
            "farming_type": "string",
            "harvest_date": "2022-08-31",
            "event_type": "chuva excessiva",
            "create_at": "2022-08-31T17:34:23.343Z",
            "update_at": "2022-08-31T17:34:23.343Z"
        }
        ```
#
## [``PUT``] /api/losses/{loss_id}/

- Request (application/json)

    - Body (obrigatorio)
        ```
        {
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "cpf": "string",
            "latitude": "string",
            "longitude": "string",
            "farming_type": "string",
            "harvest_date": "2022-08-31",
            "event_type": "chuva excessiva"
        }
        ```

-   Response 200 (application/json)

    -   Body
        ```
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "cpf": "string",
            "latitude": "string",
            "longitude": "string",
            "farming_type": "string",
            "harvest_date": "2022-08-31",
            "event_type": "chuva excessiva",
            "create_at": "2022-08-31T17:34:23.343Z",
            "update_at": "2022-08-31T17:34:23.343Z"
        }
        ```
#
## [``PATCH``] /api/losses/{loss_id}/

- Request (application/json)

    - Body
        ```
        {
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "cpf": "string",
            "latitude": "string",
            "longitude": "string",
            "farming_type": "string",
            "harvest_date": "2022-08-31",
            "event_type": "chuva excessiva"
        }
        ```

-   Response 200 (application/json)

    -   Body
        ```
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "cpf": "string",
            "latitude": "string",
            "longitude": "string",
            "farming_type": "string",
            "harvest_date": "2022-08-31",
            "event_type": "chuva excessiva",
            "create_at": "2022-08-31T17:34:23.343Z",
            "update_at": "2022-08-31T17:34:23.343Z"
        }
        ```
#
## [``DELETE``] /api/losses/{loss_id}/

-   Request (application/json)

    -   Body

-   Response 204 (application/json)

    -   Body
#
## [``GET``] /api/losses/cpf/{cpf}/

-   Request (application/json)

    -   Body

-   Response 200 (application/json)

    -   Body
        ```
        {
            "count": 123,
            "next": "http://api.example.org/accounts/?page=4",
            "previous": "http://api.example.org/accounts/?page=2",
            "results": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "first_name": "string",
                    "last_name": "string",
                    "email": "user@example.com",
                    "cpf": "string",
                    "latitude": "string",
                    "longitude": "string",
                    "farming_type": "string",
                    "harvest_date": "2022-08-31",
                    "event_type": "chuva excessiva",
                    "create_at": "2022-08-31T17:30:44.595Z",
                    "update_at": "2022-08-31T17:30:44.595Z"
                },
                ...
            ]
        }
        ```
