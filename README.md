# 🔀 Dataverse OpenAPI to OpenCollection

# 📖 Introduction
This project uses GitHub action with [vacuum CLI](https://quobix.com/vacuum/commands/) to convert the Dataverse OpenAPI specification to an OpenCollection specification.

# ✅ Prerequisites
Your Dataverse instance must have the OpenAPI specification enabled. You can check if it's enabled by navigating to `https://your-dataverse-instance/openapi`.

Relevant discussion about OpenAPI specification in Harvard Dataverse:
 - [Use OpenAPI standard for Dataverse API's (Swagger) #5794](https://github.com/IQSS/dataverse/issues/5794)
 - [Add Swagger like UI to view and call APIs #11994](https://github.com/IQSS/dataverse/issues/11994)

# 🚀 Usage
1. Fork this repository.
2. Enable GitHub Actions in your forked repository.
3. Change the url in the `dv.txt` file to point to your Dataverse instance. For example, if your Dataverse instance is hosted at `https://demo.dataverse.org` (without the trailing slash), you would change the line in `dv.txt` to:

    ```https://demo.dataverse.org```

4. Commit and push the changes to your forked repository.
5. The GitHub Action will automatically run and convert the Dataverse OpenAPI specification to an OpenCollection specification, and commit the changes to the main branch of your forked repository.

# ✨ Features

This repository is mainly designed for importing to [Bruno](https://www.usebruno.com/).

- Under the `prod` in Environments, the `baseUrl` is set to `https://borealisdata.ca/api/` (which you can change to another Dataverse instance).
- Another `demo` environment is also created with the `baseUrl` set to `https://demo.borealisdata.ca/api/`.
- The Header 'X-Dataverse-Key' is added to all the endpoints, and the value is set to the secret variable `API_TOKEN` in the environment.
  - It will work with leaving it empty with the endpoint that doesn't require authentication. 
  - But does not work with the endpoint that requires authentication.

# 🐶 Bruno
See the below video for how to import this repository to Bruno and use it to test the API endpoints.

https://github.com/user-attachments/assets/60499d97-3021-4323-a4b1-294d253e9377

# ⚖️ License
[MIT](LICENSE)
