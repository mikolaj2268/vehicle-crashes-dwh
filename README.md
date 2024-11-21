# Montgomery County Vehicle Crashes Data Warehouse

Full ETL Python pipeline configured with SQL Server database.

## Overview

This project involves building a data warehouse for analyzing vehicle crashes data
in Montgomery County. The data warehouse consolidates data from various sources to enable
efficient querying and reporting for analytical purposes.

## Data Sources

### Montgomery County Open Data

- [Incidents Data](https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Incidents-Data/bhju-22kf/about_data)
- [Drivers Data](https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Drivers-Data/mmzv-x632/about_data)
- [Non-motorists Data](https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Non-Motorists-Data/n7fk-dce5)

*Warning:* Deprecated API, ETL works only on the 'emergency' branch with data being loaded from flat files.

### fueleconomy.gov

- [Vehicles](https://www.fueleconomy.gov/feg/ws/index.shtml)

### Open Meteo

- [Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api)

### Geographical Data

- [Zipcodes](https://catalog.data.gov/dataset/zipcodes)

## Architecture

The architecture consists of:

- **ETL Pipeline**: A full ETL process implemented in Python to extract, transform, and load data.
- **Database**: Configured with SQL Server to store the data warehouse.
- **Data Warehouse**: Structured to enable efficient data analysis and reporting.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mikolaj2268/vehicle-crashes-dwh.git
   ```

2. Set up the SQL Server database:

   - Install SQL Server.
   - Create a new database for the data warehouse.

3. Run the ETL pipeline:

   - Navigate to the project directory:

     ```bash
     cd vehicle-crashes-dwh
     ```

   - Install required Python packages:

     ```bash
     pip install -r requirements.txt
     ```

   - Run the ETL script:

     ```bash
     python etl_pipeline.py
     ```

   *Note:* Ensure you are on the 'emergency' branch if you need to load data from flat files due to deprecated APIs.

## Usage

- Use SQL queries to analyze the vehicle crash data.
- Connect BI tools to the data warehouse for advanced analytics.
- Sample queries are provided in the `queries` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact:

- **Author**: Mikołaj
- **GitHub**: [mikolaj2268](https://github.com/mikolaj2268)
