---
title: integration_account_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_agreements
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>integration_account_agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_account_agreements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `tags` | `object` | The resource tags. |
| `hostPartner` | `string` | The integration account partner that is set as host partner for this agreement. |
| `changedTime` | `string` | The changed time. |
| `guestIdentity` | `object` | The integration account partner's business identity. |
| `hostIdentity` | `object` | The integration account partner's business identity. |
| `agreementType` | `string` | The agreement type. |
| `metadata` | `object` | The metadata. |
| `type` | `string` | Gets the resource type. |
| `guestPartner` | `string` | The integration account partner that is set as guest partner for this agreement. |
| `location` | `string` | The resource location. |
| `createdTime` | `string` | The created time. |
| `content` | `object` | The integration account agreement content. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationAccountAgreements_List` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets a list of integration account agreements. |
| `IntegrationAccountAgreements_CreateOrUpdate` | `INSERT` | `agreementName, api-version, integrationAccountName, resourceGroupName, subscriptionId` | Creates or updates an integration account agreement. |
| `IntegrationAccountAgreements_Delete` | `DELETE` | `agreementName, api-version, integrationAccountName, resourceGroupName, subscriptionId` | Deletes an integration account agreement. |
| `IntegrationAccountAgreements_Get` | `EXEC` | `agreementName, api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets an integration account agreement. |
| `IntegrationAccountAgreements_ListContentCallbackUrl` | `EXEC` | `agreementName, api-version, integrationAccountName, resourceGroupName, subscriptionId` | Get the content callback url. |
