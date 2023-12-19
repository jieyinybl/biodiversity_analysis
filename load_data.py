import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
db_username = 'metabase'
db_password = 'metabase_password'
db_host = 'localhost'
db_port = '6543'
db_name = 'metabase'

# SQLAlchemy engine for PostgreSQL
engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# The file path to your large dataset
file_path = '.data/0030197-231120084113126.csv'

# Specify the chunk size depending on your memory capacity
chunk_size = 50000  # Adjust this number as needed

# Specify the columns you want to load into the database
columns_to_load = ['species', 'countryCode', 'taxonKey', 'speciesKey']

# Initialize a counter for the total number of rows loaded
total_rows_loaded = 0

# Iterate over the CSV file in chunks
for chunk in pd.read_csv(file_path, chunksize=chunk_size, sep='\t', usecols=columns_to_load):
    # Append the chunk to the database table
    chunk.to_sql('occurrence', engine, if_exists='append', index=False)
    # Update the total number of rows loaded
    total_rows_loaded += len(chunk)
    # Print out the number of rows loaded from the current chunk
    print(f"Loaded {len(chunk)} rows. Total rows loaded: {total_rows_loaded}")

print("Data loading complete!")
