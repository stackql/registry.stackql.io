---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
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
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicedirectory.namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name for the namespace in the format `projects/*/locations/*/namespaces/*`. |
| `labels` | `object` | Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_namespaces_get` | `SELECT` | `name` | Gets a namespace. |
| `projects_locations_namespaces_list` | `SELECT` | `parent` | Lists all namespaces. |
| `projects_locations_namespaces_create` | `INSERT` | `parent` | Creates a namespace, and returns the new namespace. |
| `projects_locations_namespaces_delete` | `DELETE` | `name` | Deletes a namespace. This also deletes all services and endpoints in the namespace. |
| `projects_locations_namespaces_patch` | `EXEC` | `name` | Updates a namespace. |