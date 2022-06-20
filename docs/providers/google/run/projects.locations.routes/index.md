---
title: projects.locations.routes
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
<tr><td><b>Name</b></td><td><code>projects.locations.routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.projects.locations.routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `object` | RouteStatus communicates the observed state of the Route (from the controller). |
| `apiVersion` | `string` | The API version for this call such as "serving.knative.dev/v1". |
| `kind` | `string` | The kind of this resource, in this case always "Route". |
| `metadata` | `object` | k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | RouteSpec holds the desired state of the Route (from the client). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, routesId` | Get information about a service. |
| `list` | `SELECT` | `locationsId, projectsId` | List routes. |
