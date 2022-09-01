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
| `billedAmount` | `object` | The amount. |
| `type` | `string` | Resource type. |
| `isMonthlyInvoice` | `boolean` | Specifies if the invoice is generated as part of monthly invoicing cycle or not. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement. |
| `invoicePeriodEndDate` | `string` | The end date of the billing period for which the invoice is generated. |
| `subTotal` | `object` | The amount. |
| `invoiceDate` | `string` | The date when the invoice was generated. |
| `invoiceType` | `string` | Invoice type. |
| `billingProfileId` | `string` | The ID of the billing profile for which the invoice is generated. |
| `totalAmount` | `object` | The amount. |
| `billingProfileDisplayName` | `string` | The name of the billing profile for which the invoice is generated. |
| `documents` | `array` | List of documents available to download such as invoice and tax receipt. |
| `taxAmount` | `object` | The amount. |
| `dueDate` | `string` | The due date for the invoice. |
| `azurePrepaymentApplied` | `object` | The amount. |
| `creditForDocumentId` | `string` | The Id of the invoice which got voided and this credit note was issued as a result. This field is applicable to the credit notes only. |
| `amountDue` | `object` | The amount. |
| `freeAzureCreditApplied` | `object` | The amount. |
| `payments` | `array` | List of payments. |
| `purchaseOrderNumber` | `string` | An optional purchase order number for the invoice. |
| `invoicePeriodStartDate` | `string` | The start date of the billing period for which the invoice is generated. |
| `status` | `string` | The current status of the invoice. |
| `subscriptionId` | `string` | The ID of the subscription for which the invoice is generated. |
| `rebillDetails` | `object` | Rebill details for an invoice. |
| `documentType` | `string` | The type of the document. |
| `creditAmount` | `object` | The amount. |
| `billedDocumentId` | `string` | The Id of the active invoice which is originally billed after this invoice was voided. This field is applicable to the void invoices only. |
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
