---
title: managedconfigurationsforuser
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
<tr><td><b>Name</b></td><td><code>managedconfigurationsforuser</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidenterprise.managedconfigurationsforuser</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `enterpriseId, managedConfigurationForUserId, userId` | Retrieves details of a per-user managed configuration for an app for the specified user. |
| `list` | `SELECT` | `enterpriseId, userId` | Lists all the per-user managed configurations for the specified user. Only the ID is set. |
| `delete` | `DELETE` | `enterpriseId, managedConfigurationForUserId, userId` | Removes a per-user managed configuration for an app for the specified user. |
| `update` | `EXEC` | `enterpriseId, managedConfigurationForUserId, userId` | Adds or updates the managed configuration settings for an app for the specified user. If you support the Managed configurations iframe, you can apply managed configurations to a user by specifying an mcmId and its associated configuration variables (if any) in the request. Alternatively, all EMMs can apply managed configurations by passing a list of managed properties. |
