# Script python para generar csv de pruebas

## Descripción

Script en Python que genera un archivo CSV con detalles de cuentas bancarias. El script permite especificar el número de registros a generar. Los datos generados son aleatorios, pero los campos importantes como el número de cuenta y el saldo están presentes.

## Descripción del Script

Librerías Utilizadas:

* csv: Para manejar la creación y escritura del archivo CSV.
* random: Para generar datos aleatorios.
* uuid: Para generar números de cuenta únicos.
* faker: Para generar datos realistas y aleatorios como nombres, fechas, etc. Asegúrate de instalar esta librería con pip install faker.


Columnas:

 * Account Number: Número de cuenta único generado a partir de un UUID.
 * Account Holder: Nombre del titular de la cuenta generado aleatoriamente.
 * Bank Name: Nombre del banco.
 * Account Type: Tipo de cuenta (e.g., Checking, Savings).
 * Balance: Saldo de la cuenta, generado como un número decimal.
 * Currency: Moneda en la que está la cuenta.
 * Branch Code: Código de la sucursal.
 * Branch Name: Nombre de la sucursal.
 * Account Status: Estado de la cuenta (Activo, Inactivo, etc.).
 * Creation Date: Fecha de creación de la cuenta.
 * Número de Registros:

Puedes especificar el número de registros a generar cambiando el valor de num_records.

Salida:

El script genera un archivo CSV llamado bank_accounts.csv en el directorio actual.


## Ejecución
Para ejecutar este script, asegúrate de tener Python instalado junto con las librerías necesarias (faker). Puedes ejecutar el script en cualquier entorno de desarrollo de Python. El CSV resultante contendrá los datos que puedes utilizar para pruebas.