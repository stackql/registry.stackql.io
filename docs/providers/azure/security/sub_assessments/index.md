---
title: sub_assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_assessments
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
<tr><td><b>Name</b></td><td><code>sub_assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.sub_assessments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `description` | `string` | Human readable description of the assessment status |
| `additionalData` | `object` | Details of the sub-assessment |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `remediation` | `string` | Information on how to remediate this sub-assessment |
| `timeGenerated` | `string` | The date and time the sub-assessment was generated |
| `resourceDetails` | `object` | Details of the resource that was assessed |
| `displayName` | `string` | User friendly display name of the sub-assessment |
| `impact` | `string` | Description of the impact of this sub-assessment |
| `category` | `string` | Category of the sub-assessment |
| `status` | `object` | Status of the sub-assessment |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SubAssessments_List` | `SELECT` | `api-version, assessmentName, scope` | Get security sub-assessments on all your scanned resources inside a scope |
| `SubAssessments_ListAll` | `SELECT` | `api-version, scope` | Get security sub-assessments on all your scanned resources inside a subscription scope |
| `SubAssessments_Get` | `EXEC` | `api-version, assessmentName, scope, subAssessmentName` | Get a security sub-assessment on your scanned resource |
