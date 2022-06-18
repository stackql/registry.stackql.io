---
title: promotions
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
<tr><td><b>Name</b></td><td><code>promotions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.promotions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Required. Output only. The REST promotion id to uniquely identify the promotion. Content API methods that operate on promotions take this as their promotionId parameter. The REST ID for a promotion is of the form channel:contentLanguage:targetCountry:promotionId The channel field will have a value of "online", "in_store", or "online_in_store". |
| `freeGiftDescription` | `string` | Free gift description for the promotion. |
| `getThisQuantityDiscounted` | `integer` | The number of items discounted in the promotion. |
| `minimumPurchaseAmount` | `object` | The price represented as a number and currency. |
| `moneyBudget` | `object` | The price represented as a number and currency. |
| `itemId` | `array` | Product filter by item id for the promotion. |
| `brand` | `array` | Product filter by brand for the promotion. |
| `itemGroupIdExclusion` | `array` | Product filter by item group id exclusion for the promotion. |
| `promotionEffectiveDates` | `string` | Required. String representation of the promotion effective dates. |
| `moneyOffAmount` | `object` | The price represented as a number and currency. |
| `limitQuantity` | `integer` | Maximum purchase quantity for the promotion. |
| `redemptionChannel` | `array` | Required. Redemption channel for the promotion. At least one channel is required. |
| `genericRedemptionCode` | `string` | Generic redemption code for the promotion. To be used with the above field. |
| `productType` | `array` | Product filter by product type for the promotion. |
| `freeGiftValue` | `object` | The price represented as a number and currency. |
| `targetCountry` | `string` | Required. The target country used as part of the unique identifier. |
| `promotionDestinationIds` | `array` | Destination ID for the promotion. |
| `contentLanguage` | `string` | Required. The content language used as part of the unique identifier. |
| `freeGiftItemId` | `string` | Free gift item id for the promotion. |
| `brandExclusion` | `array` | Product filter by brand exclusion for the promotion. |
| `productApplicability` | `string` | Required. Applicability of the promotion to either all products or only specific products. |
| `shippingServiceNames` | `array` | Shipping service names for thse promotion. |
| `couponValueType` | `string` | Required. Coupon value type for the promotion. |
| `limitValue` | `object` | The price represented as a number and currency. |
| `promotionId` | `string` | Required. The user provided promotion id to uniquely identify the promotion. |
| `offerType` | `string` | Required. Type of the promotion. |
| `percentOff` | `integer` | The percentage discount offered in the promotion. |
| `orderLimit` | `integer` | Order limit for the promotion. |
| `itemIdExclusion` | `array` | Product filter by item id exclusion for the promotion. |
| `itemGroupId` | `array` | Product filter by item group id for the promotion. |
| `minimumPurchaseQuantity` | `integer` | Minimum purchase quantity for the promotion. |
| `longTitle` | `string` | Long title for the promotion. |
| `productTypeExclusion` | `array` | Product filter by product type exclusion for the promotion. |
| `promotionDisplayDates` | `string` | String representation of the promotion display dates. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `id, merchantId` | Retrieves a promotion from your Merchant Center account. |
| `create` | `INSERT` | `merchantId` | Inserts a promotion for your Merchant Center account. If the promotion already exists, then it will update the promotion instead. |
