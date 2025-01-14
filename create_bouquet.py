import os

def create_bouquet(m3u_file_path, bouquet_name):
    try:
        # Read the M3U file
        with open(m3u_file_path, 'r', encoding='utf-8') as m3u_file:
            m3u_lines = m3u_file.readlines()

        # Extract service lines
        services = []
        for line in m3u_lines:
            line = line.strip()
            if line.startswith("http://") or line.startswith("https://"):
                # Extract the service identifier from the URL
                service = line.split('/')[-1]
                services.append(service)

        if not services:
            print("No services found in the M3U file.")
            return

        # Create bouquet file content
        bouquet_content = f"#NAME {bouquet_name}\n"
        for service in services:
            bouquet_content += f"#SERVICE {service}\n"

        # Define output file name
        output_file_name = f"userbouquet.{bouquet_name}.tv"

        # Write to bouquet file
        with open(output_file_name, 'w', encoding='utf-8') as bouquet_file:
            bouquet_file.write(bouquet_content)

        print(f"Bouquet file '{output_file_name}' created successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{m3u_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# User input
if __name__ == "__main__":
    m3u_path = input("Enter the path to the M3U file: ").strip()
    bouquet_name = input("Enter a name for the bouquet: ").strip()

    if not bouquet_name:
        print("Bouquet name cannot be empty.")
    elif not os.path.isfile(m3u_path):
        print("The provided M3U file path is invalid.")
    else:
        create_bouquet(m3u_path, bouquet_name)
