---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
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
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.connectors.connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the Connection. Format: projects/{project}/locations/{location}/connections/{connection} |
| `description` | `string` | Optional. Description of the resource. |
| `serviceDirectory` | `string` | Output only. The name of the Service Directory service name. Used for Private Harpoon to resolve the ILB address. e.g. "projects/cloud-connectors-e2e-testing/locations/us-central1/namespaces/istio-system/services/istio-ingressgateway-connectors" |
| `authConfig` | `object` | AuthConfig defines details of a authentication type. |
| `egressBackends` | `array` | Output only. Outbound domains/hosts needs to be allowlisted. |
| `status` | `object` | ConnectionStatus indicates the state of the connection. |
| `envoyImageLocation` | `string` | Output only. GCR location where the envoy image is stored. formatted like: gcr.io/{bucketName}/{imageName} |
| `updateTime` | `string` | Output only. Updated time. |
| `configVariables` | `array` | Optional. Configuration for configuring the connection with an external system. |
| `suspended` | `boolean` | Optional. Suspended indicates if a user has suspended a connection or not. |
| `labels` | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `serviceAccount` | `string` | Optional. Service account needed for runtime plane to access GCP resources. |
| `connectorVersion` | `string` | Required. Connector version on which the connection is created. The format is: projects/*/locations/global/providers/*/connectors/*/versions/* |
| `imageLocation` | `string` | Output only. GCR location where the runtime image is stored. formatted like: gcr.io/{bucketName}/{imageName} |
| `lockConfig` | `object` | Determines whether or no a connection is locked. If locked, a reason must be specified. |
| `createTime` | `string` | Output only. Created time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_connections_get` | `SELECT` | `name` | Gets details of a single Connection. |
| `projects_locations_connections_list` | `SELECT` | `parent` | Lists Connections in a given project and location. |
| `projects_locations_connections_create` | `INSERT` | `parent` | Creates a new Connection in a given project and location. |
| `projects_locations_connections_delete` | `DELETE` | `name` | Deletes a single Connection. |
| `projects_locations_connections_patch` | `EXEC` | `name` | Updates the parameters of a single Connection. |
