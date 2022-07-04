---
title: zones_serverconfig
hide_title: false
hide_table_of_contents: false
keywords:
  - zones_serverconfig
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
<tr><td><b>Name</b></td><td><code>zones_serverconfig</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.zones_serverconfig</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `validNodeVersions` | `array` | List of valid node upgrade target versions, in descending order. |
| `channels` | `array` | List of release channel configurations. |
| `defaultClusterVersion` | `string` | Version of Kubernetes the service deploys by default. |
| `defaultImageType` | `string` | Default image type. |
| `validImageTypes` | `array` | List of valid image types. |
| `validMasterVersions` | `array` | List of valid master versions, in descending order. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_zones_getServerconfig` | `SELECT` | `projectId, zone` |