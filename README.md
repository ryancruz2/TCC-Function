# TCC-Function

This repository contains a project for an Azure Function HttpTrigger that makes a request to an external API and populates the obtained data into both a PostgreSQL database and an Azure Cognitive Search index. The project is configured with CI/CD to facilitate the deployment process to Azure.

## Features

- Makes a request to an external API to fetch relevant data.
- Stores the obtained data in a PostgreSQL database.
- Populates an Azure Cognitive Search index with the obtained data.
- Configured with CI/CD for automatic deployment to Azure.

## Configuration

Before running the Azure Function, follow the configuration steps below:

1. Make sure you have an Azure account and have created a PostgreSQL database.
2. Create an index in Azure Cognitive Search and define the necessary fields to store the data.
3. In the `local.settings.json` file, set the following environment variables:
   - `AzureWebJobsStorage`: The connection string for Azure Storage.
   - `PostgreSQLConnectionString`: The connection string for the PostgreSQL database.
   - `CognitiveSearchServiceName`: The name of the Azure Cognitive Search service.
   - `CognitiveSearchAdminApiKey`: The admin API key for Azure Cognitive Search.
4. In the `host.json` file, review and configure additional settings if needed.
5. Commit the changes to the repository to trigger the CI/CD pipeline and deploy the Azure Function to Azure.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements, bug fixes, or new features.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
