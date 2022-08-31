---
title: tickets
hide_title: false
hide_table_of_contents: false
keywords:
  - tickets
  - support
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
<tr><td><b>Name</b></td><td><code>tickets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.support.tickets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the resource. |
| `name` | `string` | Name of the resource. |
| `description` | `string` | Detailed description of the question or issue. |
| `supportTicketId` | `string` | System generated support ticket Id that is unique. |
| `problemStartTime` | `string` | Time in UTC (ISO 8601 format) when the problem started. |
| `enrollmentId` | `string` | Enrollment Id associated with the support ticket. |
| `quotaTicketDetails` | `object` | Additional set of information required for quota increase support ticket for certain quota types, e.g.: Virtual machine cores. Get complete details about Quota payload support request along with examples at [Support quota request](https://aka.ms/supportrpquotarequestpayload). |
| `technicalTicketDetails` | `object` | Additional information for technical support ticket. |
| `problemClassificationDisplayName` | `string` | Localized name of problem classification. |
| `contactDetails` | `object` | Contact information associated with the support ticket. |
| `title` | `string` | Title of the support ticket. |
| `serviceId` | `string` | This is the resource Id of the Azure service resource associated with the support ticket. |
| `createdDate` | `string` | Time in UTC (ISO 8601 format) when the support ticket was created. |
| `serviceLevelAgreement` | `object` | Service Level Agreement details for a support ticket. |
| `severity` | `string` | A value that indicates the urgency of the case, which in turn determines the response time according to the service level agreement of the technical support plan you have with Azure. Note: 'Highest critical impact', also known as the 'Emergency - Severe impact' level in the Azure portal is reserved only for our Premium customers. |
| `serviceDisplayName` | `string` | Localized name of the Azure service. |
| `status` | `string` | Status of the support ticket. |
| `type` | `string` | Type of the resource 'Microsoft.Support/supportTickets'. |
| `require24X7Response` | `boolean` | Indicates if this requires a 24x7 response from Azure. |
| `modifiedDate` | `string` | Time in UTC (ISO 8601 format) when the support ticket was last modified. |
| `supportEngineer` | `object` | Support engineer information. |
| `supportPlanType` | `string` | Support plan type associated with the support ticket. |
| `problemClassificationId` | `string` | Each Azure service has its own set of issue categories, also known as problem classification. This parameter is the unique Id for the type of problem you are experiencing. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SupportTickets_List` | `SELECT` | `subscriptionId` | Lists all the support tickets for an Azure subscription. You can also filter the support tickets by _Status_, _CreatedDate_, _ServiceId_, and _ProblemClassificationId_ using the $filter parameter. Output will be a paged result with _nextLink_, using which you can retrieve the next set of support tickets. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. |
| `SupportTickets_Create` | `INSERT` | `subscriptionId, supportTicketName` | Creates a new support ticket for Subscription and Service limits (Quota), Technical, Billing, and Subscription Management issues for the specified subscription. Learn the [prerequisites](https://aka.ms/supportAPI) required to create a support ticket.&lt;br/&gt;&lt;br/&gt;Always call the Services and ProblemClassifications API to get the most recent set of services and problem categories required for support ticket creation.&lt;br/&gt;&lt;br/&gt;Adding attachments is not currently supported via the API. To add a file to an existing support ticket, visit the [Manage support ticket](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest) page in the Azure portal, select the support ticket, and use the file upload control to add a new file.&lt;br/&gt;&lt;br/&gt;Providing consent to share diagnostic information with Azure support is currently not supported via the API. The Azure support engineer working on your ticket will reach out to you for consent if your issue requires gathering diagnostic information from your Azure resources.&lt;br/&gt;&lt;br/&gt;**Creating a support ticket for on-behalf-of**: Include _x-ms-authorization-auxiliary_ header to provide an auxiliary token as per [documentation](https://docs.microsoft.com/azure/azure-resource-manager/management/authenticate-multi-tenant). The primary token will be from the tenant for whom a support ticket is being raised against the subscription, i.e. Cloud solution provider (CSP) customer tenant. The auxiliary token will be from the Cloud solution provider (CSP) partner tenant. |
| `SupportTickets_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Check the availability of a resource name. This API should be used to check the uniqueness of the name for support ticket creation for the selected subscription. |
| `SupportTickets_Get` | `EXEC` | `subscriptionId, supportTicketName` | Get ticket details for an Azure subscription. Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. |
| `SupportTickets_Update` | `EXEC` | `subscriptionId, supportTicketName` | This API allows you to update the severity level, ticket status, and your contact information in the support ticket.&lt;br/&gt;&lt;br/&gt;Note: The severity levels cannot be changed if a support ticket is actively being worked upon by an Azure support engineer. In such a case, contact your support engineer to request severity update by adding a new communication using the Communications API.&lt;br/&gt;&lt;br/&gt;Changing the ticket status to _closed_ is allowed only on an unassigned case. When an engineer is actively working on the ticket, send your ticket closure request by sending a note to your engineer. |
