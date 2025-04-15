import csv

def main():

    PRODUCT_ID_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2

    products_dict = read_dictionary("products.csv", PRODUCT_ID_INDEX)

    aggregated_requests = {}
    # for key, value in products_dict.items():
    #      print(f"{key}: {value}")

    with open("request.csv", "rt") as csv_file:
         reader = csv.reader(csv_file)
         next(reader)
         for row in reader:
              product_id = row[0]
              requested_quantity = int(row[1])

              if product_id in aggregated_requests:
                   aggregated_requests[product_id] += requested_quantity
              else:
                   aggregated_requests[product_id] = requested_quantity

    for product_id, total_quantity in aggregated_requests.items():
            if product_id in products_dict:
                product = products_dict[product_id]
                product_name = product[PRODUCT_NAME_INDEX]
                product_price = float(product[PRODUCT_PRICE_INDEX])

                print(f"Product Name: {product_name}, Quantity: {total_quantity}, Price: {product_price:.2f}")
            else:
                print(f"Product ID {product_id} not found in products_dict.")

def read_dictionary(filename, key_column_index):
      """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
      dictionary = {}

      with open(filename, "rt") as csv_file:
           reader = csv.reader(csv_file)
           next(reader)
           for row_list in reader:
                if len(row_list) != 0:
                     key = row_list[key_column_index]
                     dictionary[key] = row_list
           return dictionary
      

if __name__ == "__main__":
     main()