---
title: purchases.products
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
<tr><td><b>Name</b></td><td><code>purchases.products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidpublisher.purchases.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `developerPayload` | `string` | A developer-specified string that contains supplemental information about an order. |
| `quantity` | `integer` | The quantity associated with the purchase of the inapp product. |
| `consumptionState` | `integer` | The consumption state of the inapp product. Possible values are: 0. Yet to be consumed 1. Consumed |
| `purchaseToken` | `string` | The purchase token generated to identify this purchase. |
| `purchaseState` | `integer` | The purchase state of the order. Possible values are: 0. Purchased 1. Canceled 2. Pending |
| `orderId` | `string` | The order id associated with the purchase of the inapp product. |
| `regionCode` | `string` | ISO 3166-1 alpha-2 billing region code of the user at the time the product was granted. |
| `kind` | `string` | This kind represents an inappPurchase object in the androidpublisher service. |
| `obfuscatedExternalAccountId` | `string` | An obfuscated version of the id that is uniquely associated with the user's account in your app. Only present if specified using https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedaccountid when the purchase was made. |
| `purchaseType` | `integer` | The type of purchase of the inapp product. This field is only set if this purchase was not made using the standard in-app billing flow. Possible values are: 0. Test (i.e. purchased from a license testing account) 1. Promo (i.e. purchased using a promo code) 2. Rewarded (i.e. from watching a video ad instead of paying) |
| `obfuscatedExternalProfileId` | `string` | An obfuscated version of the id that is uniquely associated with the user's profile in your app. Only present if specified using https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid when the purchase was made. |
| `acknowledgementState` | `integer` | The acknowledgement state of the inapp product. Possible values are: 0. Yet to be acknowledged 1. Acknowledged |
| `productId` | `string` | The inapp product SKU. |
| `purchaseTimeMillis` | `string` | The time the product was purchased, in milliseconds since the epoch (Jan 1, 1970). |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `packageName, productId, token` | Checks the purchase and consumption status of an inapp item. |
| `acknowledge` | `EXEC` | `packageName, productId, token` | Acknowledges a purchase of an inapp item. |
