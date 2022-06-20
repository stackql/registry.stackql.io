---
title: projects.locations.services
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>projects.locations.services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.projects.locations.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `apiVersion` | `string` | The API version for this call such as "serving.knative.dev/v1". |
| `kind` | `string` | The kind of resource, in this case "Service". |
| `metadata` | `object` | k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | ServiceSpec holds the desired state of the Route (from the client), which is used to manipulate the underlying Route and Configuration(s). |
| `status` | `object` | The current state of the Service. Output only. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, servicesId` | Get information about a service. |
| `list` | `SELECT` | `locationsId, projectsId` | List services. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a service. |
| `delete` | `DELETE` | `locationsId, projectsId, servicesId` | Delete a service. This will cause the Service to stop serving traffic and will delete the child entities like Routes, Configurations and Revisions. |
| `getIamPolicy` | `EXEC` | `locationsId, projectsId, servicesId` | Get the IAM Access Control policy currently in effect for the given Cloud Run service. This result does not include any inherited policies. |
| `replaceService` | `EXEC` | `locationsId, projectsId, servicesId` | Replace a service. Only the spec and metadata labels and annotations are modifiable. After the Update request, Cloud Run will work to make the 'status' match the requested 'spec'. May provide metadata.resourceVersion to enforce update from last read for optimistic concurrency control. |
| `setIamPolicy` | `EXEC` | `locationsId, projectsId, servicesId` | Sets the IAM Access control policy for the specified Service. Overwrites any existing policy. |
| `testIamPermissions` | `EXEC` | `locationsId, projectsId, servicesId` | Returns permissions that a caller has on the specified Project. There are no permissions required for making this API call. |
