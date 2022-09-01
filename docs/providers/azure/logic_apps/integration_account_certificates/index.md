---
title: integration_account_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_certificates
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
<tr><td><b>Name</b></td><td><code>integration_account_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_account_certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `publicCertificate` | `string` | The public certificate. |
| `key` | `object` | The reference to the key vault key. |
| `metadata` | `object` | The metadata. |
| `type` | `string` | Gets the resource type. |
| `createdTime` | `string` | The created time. |
| `changedTime` | `string` | The changed time. |
| `tags` | `object` | The resource tags. |
| `location` | `string` | The resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationAccountCertificates_List` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets a list of integration account certificates. |
| `IntegrationAccountCertificates_CreateOrUpdate` | `INSERT` | `api-version, certificateName, integrationAccountName, resourceGroupName, subscriptionId` | Creates or updates an integration account certificate. |
| `IntegrationAccountCertificates_Delete` | `DELETE` | `api-version, certificateName, integrationAccountName, resourceGroupName, subscriptionId` | Deletes an integration account certificate. |
| `IntegrationAccountCertificates_Get` | `EXEC` | `api-version, certificateName, integrationAccountName, resourceGroupName, subscriptionId` | Gets an integration account certificate. |
