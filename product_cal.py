# Python program to calculate raw material usage with multiple raw materials

# Function to calculate maximum products and remaining raw materials
def calculate_products(raw_materials_available, raw_materials_per_product, products_to_make=None):
    # Calculate maximum number of products that can be made based on the limiting raw material
    max_products_list = [raw_materials_available[i] // raw_materials_per_product[i] for i in range(len(raw_materials_available))]
    max_products = min(max_products_list)  # Maximum based on the limiting factor

    # Calculate remaining raw material after producing specified products
    if products_to_make is None:
        products_to_make = max_products
        
    remaining_materials = [raw_materials_available[i] - (products_to_make * raw_materials_per_product[i]) for i in range(len(raw_materials_available))]
    
    return max_products, remaining_materials

# User input for raw materials
num_materials = int(input("Enter the number of raw materials: "))
raw_materials_available = []
raw_materials_per_product = []

# Collecting raw material data from the user
for i in range(num_materials):
    available = float(input(f"Enter total raw material available for material {i+1} (in kg): "))
    required = float(input(f"Enter raw material required per product for material {i+1} (in kg): "))
    raw_materials_available.append(available)
    raw_materials_per_product.append(required)

# Optional number of products to make
products_to_make = input("Enter the number of products you want to make (optional, leave blank for maximum): ")

# Convert the input to None if blank, otherwise to integer
products_to_make = int(products_to_make) if products_to_make else None

# Get the maximum products and remaining materials
max_products, remaining_materials = calculate_products(raw_materials_available, raw_materials_per_product, products_to_make)

# Output the results
print(f"\nMaximum products you can make: {max_products}")
print("Remaining raw materials (in kg):")
for i in range(num_materials):
    print(f"Material {i+1}: {remaining_materials[i]}")
