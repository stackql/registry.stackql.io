---
title: regulatory_compliance_assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - regulatory_compliance_assessments
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
<tr><td><b>Name</b></td><td><code>regulatory_compliance_assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.regulatory_compliance_assessments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `description` | `string` | The description of the regulatory compliance assessment |
| `failedResources` | `integer` | The given assessment's related resources count with failed state. |
| `skippedResources` | `integer` | The given assessment's related resources count with skipped state. |
| `assessmentDetailsLink` | `string` | Link to more detailed assessment results data. The response type will be according to the assessmentType field |
| `passedResources` | `integer` | The given assessment's related resources count with passed state. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `unsupportedResources` | `integer` | The given assessment's related resources count with unsupported state. |
| `state` | `string` | Aggregative state based on the assessment's scanned resources states |
| `assessmentType` | `string` | The expected type of assessment contained in the AssessmentDetailsLink |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegulatoryComplianceAssessments_List` | `SELECT` | `api-version, regulatoryComplianceControlName, regulatoryComplianceStandardName, subscriptionId` | Details and state of assessments mapped to selected regulatory compliance control |
| `RegulatoryComplianceAssessments_Get` | `EXEC` | `api-version, regulatoryComplianceAssessmentName, regulatoryComplianceControlName, regulatoryComplianceStandardName, subscriptionId` | Supported regulatory compliance details and state for selected assessment |
