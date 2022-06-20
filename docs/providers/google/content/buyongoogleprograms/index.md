---
title: buyongoogleprograms
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buyongoogleprograms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.buyongoogleprograms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `onlineSalesChannel` | `string` | The channels through which the merchant is selling. |
| `customerServiceVerifiedPhoneNumber` | `string` | Output only. The verified phone number specified for BuyOnGoogle program. It might be different than account level phone number. |
| `customerServicePendingPhoneRegionCode` | `string` | Two letter country code for the pending phone number, for example `CA` for Canadian numbers. See the [ISO 3166-1 alpha-2](https://wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) officially assigned codes. In order to update this field the customer_service_pending_phone_number must also be set. After verification this field becomes empty. |
| `participationStage` | `string` | Output only. The current participation stage for the program. |
| `customerServicePendingPhoneNumber` | `string` | The pending phone number specified for BuyOnGoogle program. It might be different than account level phone number. In order to update this field the customer_service_pending_phone_region_code must also be set. After verification this field becomes empty. |
| `customerServiceVerifiedEmail` | `string` | Output only. The customer service verified email. |
| `customerServicePendingEmail` | `string` | The customer service pending email. After verification this field becomes empty. |
| `customerServiceVerifiedPhoneRegionCode` | `string` | Output only. Two letter country code for the verified phone number, for example `CA` for Canadian numbers. See the [ISO 3166-1 alpha-2](https://wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) officially assigned codes. |
| `businessModel` | `array` | The business models in which merchant participates. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, regionCode` | Retrieves a status of the BoG program for your Merchant Center account. |
| `activate` | `EXEC` | `merchantId, regionCode` | Reactivates the BoG program in your Merchant Center account. Moves the program to the active state when allowed, e.g. when paused. Important: This method is only whitelisted for selected merchants. |
| `onboard` | `EXEC` | `merchantId, regionCode` | Onboards the BoG program in your Merchant Center account. By using this method, you agree to the [Terms of Service](https://merchants.google.com/mc/termsofservice/transactions/US/latest). Calling this method is only possible if the authenticated account is the same as the merchant id in the request. Calling this method multiple times will only accept Terms of Service if the latest version is not currently signed. |
| `patch` | `EXEC` | `merchantId, regionCode` | Updates the status of the BoG program for your Merchant Center account. |
| `pause` | `EXEC` | `merchantId, regionCode` | Pauses the BoG program in your Merchant Center account. Important: This method is only whitelisted for selected merchants. |
| `requestreview` | `EXEC` | `merchantId, regionCode` | Requests review and then activates the BoG program in your Merchant Center account for the first time. Moves the program to the REVIEW_PENDING state. Important: This method is only whitelisted for selected merchants. |
