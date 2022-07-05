---
title: attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - attachments
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | ID of the environment group attachment. |
| `createdAt` | `string` | Output only. The time at which the environment group attachment was created as milliseconds since epoch. |
| `environment` | `string` | Required. ID of the attached environment. |
| `environmentGroupId` | `string` | Output only. ID of the environment group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_envgroups_attachments_get` | `SELECT` | `name` | Gets an environment group attachment. |
| `organizations_envgroups_attachments_list` | `SELECT` | `parent` | Lists all attachments of an environment group. |
| `organizations_instances_attachments_get` | `SELECT` | `name` | Gets an attachment. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_attachments_list` | `SELECT` | `parent` | Lists all attachments to an instance. **Note:** Not supported for Apigee hybrid. |
| `organizations_envgroups_attachments_create` | `INSERT` | `parent` | Creates a new attachment of an environment to an environment group. |
| `organizations_instances_attachments_create` | `INSERT` | `parent` | Creates a new attachment of an environment to an instance. **Note:** Not supported for Apigee hybrid. |
| `organizations_envgroups_attachments_delete` | `DELETE` | `name` | Deletes an environment group attachment. |
| `organizations_instances_attachments_delete` | `DELETE` | `name` | Deletes an attachment. **Note:** Not supported for Apigee hybrid. |
