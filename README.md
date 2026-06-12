# 🔀 Dataverse OpenAPI to OpenCollection

# 📖 Introduction
This project uses GitHub action with [vacuum CLI](https://quobix.com/vacuum/commands/) to convert the Dataverse OpenAPI specification to an OpenCollection specification.

# ✅ Prerequisites
Your Dataverse instance must have the OpenAPI specification enabled. You can check if it's enabled by navigating to `https://your-dataverse-instance/openapi`.

Relevant discussion about OpenAPI specification in Harvard Dataverse:
 - [Use OpenAPI standard for Dataverse API's (Swagger) #5794](https://github.com/IQSS/dataverse/issues/5794)
 - [Add Swagger like UI to view and call APIs #11994](https://github.com/IQSS/dataverse/issues/11994)

To use this repository with [Bruno](https://www.usebruno.com/downloads), you will also need to install [Git](https://git-scm.com/install/).


# 🚀 Usage
1. Fork this repository.
2. Enable GitHub Actions in your forked repository.
3. Change the url in the `dv.txt` file to point to your Dataverse instance. For example, if your Dataverse instance is hosted at `https://demo.dataverse.org` (without the trailing slash), you would change the line in `dv.txt` to: ```https://demo.dataverse.org```.
4. Commit and push the changes to your forked repository.
5. The GitHub Action will automatically run and convert the Dataverse OpenAPI specification to an OpenCollection specification, and commit the changes to the main branch of your forked repository.

# ✨ Features

This repository is primarily designed for import into [Bruno](https://www.usebruno.com/) as a collection.

- Environments
  - In the `prod` environment, the `baseUrl` is set to `https://borealisdata.ca/api/`
  - In the `demo` environment, a `baseUrl` is set to `https://demo.borealisdata.ca/api/`.
  - This allows an easy switch between repositories while using the same API endpoint.
  - You can change the `baseUrl` values in `demo.yml`/`prod.yml` under dataverse_endpoints/environments/ if needed
- By default, every API request sent out will be sent with the Header 'X-Dataverse-Key', and the value is set to the secret variable `X_Dataverse_Key` in the respective environment.
  - It will work by leaving it empty with the endpoint that doesn't require authentication. 
  - But it does not work with the endpoint that requires authentication. 

# 🐶 Bruno
See the video below for instructions on importing this repository into Bruno and using it to work with the API endpoints.

https://github.com/user-attachments/assets/60499d97-3021-4323-a4b1-294d253e9377

# ⚖️ License
[MIT](LICENSE)
