---
title: projects.locations.domainmappings
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
<tr><td><b>Name</b></td><td><code>projects.locations.domainmappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.projects.locations.domainmappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `status` | `object` | The current state of the Domain Mapping. |
| `apiVersion` | `string` | The API version for this call such as "domains.cloudrun.com/v1". |
| `kind` | `string` | The kind of resource, in this case "DomainMapping". |
| `metadata` | `object` | k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | The desired state of the Domain Mapping. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `domainmappingsId, locationsId, projectsId` | Get information about a service. |
| `list` | `SELECT` | `locationsId, projectsId` | List domain mappings. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new domain mapping. |
| `delete` | `DELETE` | `domainmappingsId, locationsId, projectsId` | Delete a service. This will cause the Service to stop serving traffic and will delete the child entities like Routes, Configurations and Revisions. |
