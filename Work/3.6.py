import csv

def parse_csv(filename, select=None, types=None, has_header=True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        if has_header:
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]

            if types:
                row = [func(val) for func, val in zip(types, row) ]

            
            if has_header:
            # Make a dictionary
                record = dict(zip(headers, row))
            else:
                record=tuple(row)
            records.append(record)

    return records

records= parse_csv('Data/portfolio.csv', types=[str,int,float])
print(records)
records= parse_csv('Data/portfolio.csv', types=[str,int,float], select=['name','shares'])
print(records)
records= parse_csv('Data/prices.csv',types=[str,float], has_header=False)
print(records)