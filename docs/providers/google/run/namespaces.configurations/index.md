---
title: namespaces.configurations
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
<tr><td><b>Name</b></td><td><code>namespaces.configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.namespaces.configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metadata` | `object` | k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| `spec` | `object` | ConfigurationSpec holds the desired state of the Configuration (from the client). |
| `status` | `object` | ConfigurationStatus communicates the observed state of the Configuration (from the controller). |
| `apiVersion` | `string` | The API version for this call such as "serving.knative.dev/v1". |
| `kind` | `string` | The kind of resource, in this case always "Configuration". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationsId, namespacesId` | Get information about a service. |
| `list` | `SELECT` | `namespacesId` | List configurations. |
