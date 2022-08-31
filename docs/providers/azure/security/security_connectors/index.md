---
title: security_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - security_connectors
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
<tr><td><b>Name</b></td><td><code>security_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.security_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `environmentData` | `object` | The security connector environment data. |
| `environmentName` | `string` | The multi cloud resource's cloud name. |
| `hierarchyIdentifier` | `string` | The multi cloud resource identifier (account id in case of AWS connector, project number in case of GCP connector). |
| `hierarchyIdentifierTrialEndDate` | `string` | The date on which the trial period will end, if applicable. Trial period exists for 30 days after upgrading to payed offerings. |
| `location` | `string` | The geo-location where the resource lives |
| `offerings` | `array` | A collection of offerings for the security connector. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityConnectors_List` | `SELECT` | `api-version, subscriptionId` | Lists all the security connectors in the specified subscription. Use the 'nextLink' property in the response to get the next page of security connectors for the specified subscription. |
| `SecurityConnectors_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Lists all the security connectors in the specified resource group. Use the 'nextLink' property in the response to get the next page of security connectors for the specified resource group. |
| `SecurityConnectors_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, securityConnectorName, subscriptionId` | Creates or updates a security connector. If a security connector is already created and a subsequent request is issued for the same security connector id, then it will be updated. |
| `SecurityConnectors_Delete` | `DELETE` | `api-version, resourceGroupName, securityConnectorName, subscriptionId` | Deletes a security connector. |
| `SecurityConnectors_Get` | `EXEC` | `api-version, resourceGroupName, securityConnectorName, subscriptionId` | Retrieves details of a specific security connector |
| `SecurityConnectors_Update` | `EXEC` | `api-version, resourceGroupName, securityConnectorName, subscriptionId` | Updates a security connector |