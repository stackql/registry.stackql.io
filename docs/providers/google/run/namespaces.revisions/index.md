---
title: namespaces.revisions
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
<tr><td><b>Name</b></td><td><code>namespaces.revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.namespaces.revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `spec` | `object` | RevisionSpec holds the desired state of the Revision (from the client). |
| `status` | `object` | RevisionStatus communicates the observed state of the Revision (from the controller). |
| `apiVersion` | `string` | The API version for this call such as "serving.knative.dev/v1". |
| `kind` | `string` | The kind of this resource, in this case "Revision". |
| `metadata` | `object` | k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `namespacesId, revisionsId` | Get information about a service. |
| `list` | `SELECT` | `namespacesId` | List revisions. |
| `delete` | `DELETE` | `namespacesId, revisionsId` | Delete a service. This will cause the Service to stop serving traffic and will delete the child entities like Routes, Configurations and Revisions. |
