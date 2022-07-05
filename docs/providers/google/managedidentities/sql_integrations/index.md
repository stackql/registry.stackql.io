---
title: sql_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_integrations
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
<tr><td><b>Name</b></td><td><code>sql_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.managedidentities.sql_integrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique name of the SQL integration in the form of `projects/{project_id}/locations/global/domains/{domain_name}/sqlIntegrations/{sql_integration}` |
| `sqlInstance` | `string` | The full resource name of an integrated SQL instance |
| `state` | `string` | Output only. The current state of the SQL integration. |
| `updateTime` | `string` | Output only. The time the SQL integration was updated. |
| `createTime` | `string` | Output only. The time the SQL integration was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_domains_sqlIntegrations_get` | `SELECT` | `name` | Gets details of a single sqlIntegration. |
| `projects_locations_global_domains_sqlIntegrations_list` | `SELECT` | `parent` | Lists SqlIntegrations in a given domain. |
