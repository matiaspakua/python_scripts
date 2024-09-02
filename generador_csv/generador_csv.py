import csv
import random
import uuid
import faker

def generate_bank_accounts(num_records, file_name='bank_accounts.csv'):
    # Columnas del archivo CSV
    columns = ['Account Number', 'Account Holder', 'Bank Name', 'Account Type', 
               'Balance', 'Currency', 'Branch Code', 'Branch Name', 
               'Account Status', 'Creation Date']

    # Inicializa Faker para generar datos aleatorios
    fake = faker.Faker()

    # Crear y escribir el archivo CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        
        for _ in range(num_records):
            # Generar datos aleatorios
            account_number = str(uuid.uuid4().int)[:12]  # Número de cuenta único de 12 dígitos
            account_holder = fake.name()
            bank_name = fake.company()
            account_type = random.choice(['Checking', 'Savings', 'Investment', 'Credit'])
            balance = round(random.uniform(0, 1000000), 2)  # Saldo entre 0 y 1,000,000
            currency = random.choice(['USD', 'EUR', 'GBP', 'JPY', 'AUD'])
            branch_code = str(random.randint(1000, 9999))  # Código de sucursal de 4 dígitos
            branch_name = fake.city()
            account_status = random.choice(['Active', 'Inactive', 'Suspended'])
            creation_date = fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d')
            
            # Escribir la fila en el archivo CSV
            writer.writerow({
                'Account Number': account_number,
                'Account Holder': account_holder,
                'Bank Name': bank_name,
                'Account Type': account_type,
                'Balance': balance,
                'Currency': currency,
                'Branch Code': branch_code,
                'Branch Name': branch_name,
                'Account Status': account_status,
                'Creation Date': creation_date
            })

    print(f'{num_records} bank account records have been written to {file_name}.')

# Especificar el número de registros a generar
num_records = 10000  # Puedes cambiar este valor según sea necesario
generate_bank_accounts(num_records)
