---
title: connector_application
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_application
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
<tr><td><b>Name</b></td><td><code>connector_application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.connector_application</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityConnectorApplication_CreateOrUpdate` | `INSERT` | `api-version, applicationId, resourceGroupName, securityConnectorName, subscriptionId` | Creates or update a security Application on the given security connector. |
| `SecurityConnectorApplication_Delete` | `DELETE` | `api-version, applicationId, resourceGroupName, securityConnectorName, subscriptionId` | Delete an Application over a given scope |
| `SecurityConnectorApplication_Get` | `EXEC` | `api-version, applicationId, resourceGroupName, securityConnectorName, subscriptionId` | Get a specific application for the requested scope by applicationId |
