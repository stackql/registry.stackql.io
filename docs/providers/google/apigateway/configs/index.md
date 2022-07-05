---
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigateway.configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the API Config. Format: projects/{project}/locations/global/apis/{api}/configs/{api_config} |
| `serviceConfigId` | `string` | Output only. The ID of the associated Service Config ( https://cloud.google.com/service-infrastructure/docs/glossary#config). |
| `state` | `string` | Output only. State of the API Config. |
| `openapiDocuments` | `array` | Optional. OpenAPI specification documents. If specified, grpc_services and managed_service_configs must not be included. |
| `displayName` | `string` | Optional. Display name. |
| `labels` | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `createTime` | `string` | Output only. Created time. |
| `gatewayServiceAccount` | `string` | Immutable. The Google Cloud IAM Service Account that Gateways serving this config should use to authenticate to other services. This may either be the Service Account's email (`{ACCOUNT_ID}@{PROJECT}.iam.gserviceaccount.com`) or its full resource name (`projects/{PROJECT}/accounts/{UNIQUE_ID}`). This is most often used when the service is a GCP resource such as a Cloud Run Service or an IAP-secured service. |
| `updateTime` | `string` | Output only. Updated time. |
| `grpcServices` | `array` | Optional. gRPC service definition files. If specified, openapi_documents must not be included. |
| `managedServiceConfigs` | `array` | Optional. Service Configuration files. At least one must be included when using gRPC service definitions. See https://cloud.google.com/endpoints/docs/grpc/grpc-service-config#service_configuration_overview for the expected file contents. If multiple files are specified, the files are merged with the following rules: * All singular scalar fields are merged using "last one wins" semantics in the order of the files uploaded. * Repeated fields are concatenated. * Singular embedded messages are merged using these rules for nested fields. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_configs_get` | `SELECT` | `name` | Gets details of a single ApiConfig. |
| `projects_locations_apis_configs_list` | `SELECT` | `parent` | Lists ApiConfigs in a given project and location. |
| `projects_locations_apis_configs_create` | `INSERT` | `parent` | Creates a new ApiConfig in a given project and location. |
| `projects_locations_apis_configs_delete` | `DELETE` | `name` | Deletes a single ApiConfig. |
| `projects_locations_apis_configs_patch` | `EXEC` | `name` | Updates the parameters of a single ApiConfig. |
