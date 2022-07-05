---
title: envgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - envgroups
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
<tr><td><b>Name</b></td><td><code>envgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.envgroups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | ID of the environment group. |
| `hostnames` | `array` | Required. Host names for this environment group. |
| `lastModifiedAt` | `string` | Output only. The time at which the environment group was last updated as milliseconds since epoch. |
| `state` | `string` | Output only. State of the environment group. Values other than ACTIVE means the resource is not ready to use. |
| `createdAt` | `string` | Output only. The time at which the environment group was created as milliseconds since epoch. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_envgroups_get` | `SELECT` | `name` | Gets an environment group. |
| `organizations_envgroups_list` | `SELECT` | `parent` | Lists all environment groups. |
| `organizations_envgroups_create` | `INSERT` | `parent` | Creates a new environment group. |
| `organizations_envgroups_delete` | `DELETE` | `name` | Deletes an environment group. |
| `organizations_envgroups_patch` | `EXEC` | `name` | Updates an environment group. |
