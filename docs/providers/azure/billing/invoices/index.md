---
title: invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - invoices
  - billing
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
<tr><td><b>Name</b></td><td><code>invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.invoices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `creditForDocumentId` | `string` | The Id of the invoice which got voided and this credit note was issued as a result. This field is applicable to the credit notes only. |
| `invoicePeriodStartDate` | `string` | The start date of the billing period for which the invoice is generated. |
| `subscriptionId` | `string` | The ID of the subscription for which the invoice is generated. |
| `billingProfileDisplayName` | `string` | The name of the billing profile for which the invoice is generated. |
| `isMonthlyInvoice` | `boolean` | Specifies if the invoice is generated as part of monthly invoicing cycle or not. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement. |
| `invoiceDate` | `string` | The date when the invoice was generated. |
| `creditAmount` | `object` | The amount. |
| `billedAmount` | `object` | The amount. |
| `billingProfileId` | `string` | The ID of the billing profile for which the invoice is generated. |
| `documents` | `array` | List of documents available to download such as invoice and tax receipt. |
| `taxAmount` | `object` | The amount. |
| `totalAmount` | `object` | The amount. |
| `freeAzureCreditApplied` | `object` | The amount. |
| `dueDate` | `string` | The due date for the invoice. |
| `type` | `string` | Resource type. |
| `azurePrepaymentApplied` | `object` | The amount. |
| `rebillDetails` | `object` | Rebill details for an invoice. |
| `invoiceType` | `string` | Invoice type. |
| `billedDocumentId` | `string` | The Id of the active invoice which is originally billed after this invoice was voided. This field is applicable to the void invoices only. |
| `purchaseOrderNumber` | `string` | An optional purchase order number for the invoice. |
| `payments` | `array` | List of payments. |
| `documentType` | `string` | The type of the document. |
| `invoicePeriodEndDate` | `string` | The end date of the billing period for which the invoice is generated. |
| `amountDue` | `object` | The amount. |
| `status` | `string` | The current status of the invoice. |
| `subTotal` | `object` | The amount. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Invoices_ListByBillingAccount` | `SELECT` | `billingAccountName, periodEndDate, periodStartDate` | Lists the invoices for a billing account for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName, periodEndDate, periodStartDate` | Lists the invoices for a billing profile for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_ListByBillingSubscription` | `SELECT` | `periodEndDate, periodStartDate, subscriptionId` | Lists the invoices for a subscription. |
| `Invoices_DownloadBillingSubscriptionInvoice` | `EXEC` | `downloadToken, invoiceName, subscriptionId` | Gets a URL to download an invoice. |
| `Invoices_DownloadInvoice` | `EXEC` | `billingAccountName, downloadToken, invoiceName` | Gets a URL to download an invoice. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_DownloadMultipleBillingProfileInvoices` | `EXEC` | `billingAccountName` | Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_DownloadMultipleBillingSubscriptionInvoices` | `EXEC` | `subscriptionId` | Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. |
| `Invoices_Get` | `EXEC` | `billingAccountName, invoiceName` | Gets an invoice by billing account name and ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_GetById` | `EXEC` | `invoiceName` | Gets an invoice by ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_GetBySubscriptionAndInvoiceId` | `EXEC` | `invoiceName, subscriptionId` | Gets an invoice by subscription ID and invoice ID. |
