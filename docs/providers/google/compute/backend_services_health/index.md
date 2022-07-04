---
title: backend_services_health
hide_title: false
hide_table_of_contents: false
keywords:
  - backend_services_health
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
<tr><td><b>Name</b></td><td><code>backend_services_health</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.backend_services_health</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `healthStatus` | `array` | Health state of the backend instances or endpoints in requested instance or network endpoint group, determined based on configured health checks. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#backendServiceGroupHealth for the health of backend services. |
| `annotations` | `object` | Metadata defined as annotations on the network endpoint group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `backendServices_getHealth` | `SELECT` | `backendService, project` |