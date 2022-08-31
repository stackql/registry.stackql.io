---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - security
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.application</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Application_CreateOrUpdate` | `INSERT` | `api-version, applicationId, subscriptionId` | Creates or update a security application on the given subscription. |
| `Application_Delete` | `DELETE` | `api-version, applicationId, subscriptionId` | Delete an Application over a given scope |
| `Application_Get` | `EXEC` | `api-version, applicationId, subscriptionId` | Get a specific application for the requested scope by applicationId |
