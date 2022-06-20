---
title: purchases.subscriptions
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
<tr><td><b>Name</b></td><td><code>purchases.subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidpublisher.purchases.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `paymentState` | `integer` | The payment state of the subscription. Possible values are: 0. Payment pending 1. Payment received 2. Free trial 3. Pending deferred upgrade/downgrade Not present for canceled, expired subscriptions. |
| `promotionType` | `integer` | The type of promotion applied on this purchase. This field is only set if a promotion is applied when the subscription was purchased. Possible values are: 0. One time code 1. Vanity code |
| `userCancellationTimeMillis` | `string` | The time at which the subscription was canceled by the user, in milliseconds since the epoch. Only present if cancelReason is 0. |
| `orderId` | `string` | The order id of the latest recurring order associated with the purchase of the subscription. If the subscription was canceled because payment was declined, this will be the order id from the payment declined order. |
| `cancelSurveyResult` | `object` | Information provided by the user when they complete the subscription cancellation flow (cancellation reason survey). |
| `profileId` | `string` | The Google profile id of the user when the subscription was purchased. Only present for purchases made with 'Subscribe with Google'. |
| `priceCurrencyCode` | `string` | ISO 4217 currency code for the subscription price. For example, if the price is specified in British pounds sterling, price_currency_code is "GBP". |
| `startTimeMillis` | `string` | Time at which the subscription was granted, in milliseconds since the Epoch. |
| `expiryTimeMillis` | `string` | Time at which the subscription will expire, in milliseconds since the Epoch. |
| `externalAccountId` | `string` | User account identifier in the third-party service. Only present if account linking happened as part of the subscription purchase flow. |
| `profileName` | `string` | The profile name of the user when the subscription was purchased. Only present for purchases made with 'Subscribe with Google'. |
| `obfuscatedExternalAccountId` | `string` | An obfuscated version of the id that is uniquely associated with the user's account in your app. Present for the following purchases: * If account linking happened as part of the subscription purchase flow. * It was specified using https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedaccountid when the purchase was made. |
| `emailAddress` | `string` | The email address of the user when the subscription was purchased. Only present for purchases made with 'Subscribe with Google'. |
| `countryCode` | `string` | ISO 3166-1 alpha-2 billing country/region code of the user at the time the subscription was granted. |
| `promotionCode` | `string` | The promotion code applied on this purchase. This field is only set if a vanity code promotion is applied when the subscription was purchased. |
| `linkedPurchaseToken` | `string` | The purchase token of the originating purchase if this subscription is one of the following: 0. Re-signup of a canceled but non-lapsed subscription 1. Upgrade/downgrade from a previous subscription For example, suppose a user originally signs up and you receive purchase token X, then the user cancels and goes through the resignup flow (before their subscription lapses) and you receive purchase token Y, and finally the user upgrades their subscription and you receive purchase token Z. If you call this API with purchase token Z, this field will be set to Y. If you call this API with purchase token Y, this field will be set to X. If you call this API with purchase token X, this field will not be set. |
| `purchaseType` | `integer` | The type of purchase of the subscription. This field is only set if this purchase was not made using the standard in-app billing flow. Possible values are: 0. Test (i.e. purchased from a license testing account) 1. Promo (i.e. purchased using a promo code) |
| `autoResumeTimeMillis` | `string` | Time at which the subscription will be automatically resumed, in milliseconds since the Epoch. Only present if the user has requested to pause the subscription. |
| `cancelReason` | `integer` | The reason why a subscription was canceled or is not auto-renewing. Possible values are: 0. User canceled the subscription 1. Subscription was canceled by the system, for example because of a billing problem 2. Subscription was replaced with a new subscription 3. Subscription was canceled by the developer |
| `autoRenewing` | `boolean` | Whether the subscription will automatically be renewed when it reaches its current expiry time. |
| `developerPayload` | `string` | A developer-specified string that contains supplemental information about an order. |
| `obfuscatedExternalProfileId` | `string` | An obfuscated version of the id that is uniquely associated with the user's profile in your app. Only present if specified using https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid when the purchase was made. |
| `kind` | `string` | This kind represents a subscriptionPurchase object in the androidpublisher service. |
| `introductoryPriceInfo` | `object` | Contains the introductory price information for a subscription. |
| `priceChange` | `object` | Contains the price change information for a subscription that can be used to control the user journey for the price change in the app. This can be in the form of seeking confirmation from the user or tailoring the experience for a successful conversion. |
| `givenName` | `string` | The given name of the user when the subscription was purchased. Only present for purchases made with 'Subscribe with Google'. |
| `priceAmountMicros` | `string` | Price of the subscription, For tax exclusive countries, the price doesn't include tax. For tax inclusive countries, the price includes tax. Price is expressed in micro-units, where 1,000,000 micro-units represents one unit of the currency. For example, if the subscription price is €1.99, price_amount_micros is 1990000. |
| `acknowledgementState` | `integer` | The acknowledgement state of the subscription product. Possible values are: 0. Yet to be acknowledged 1. Acknowledged |
| `familyName` | `string` | The family name of the user when the subscription was purchased. Only present for purchases made with 'Subscribe with Google'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packageName, subscriptionId, token` | Checks whether a user's subscription purchase is valid and returns its expiry time. |
| `acknowledge` | `EXEC` | `packageName, subscriptionId, token` | Acknowledges a subscription purchase. |
| `cancel` | `EXEC` | `packageName, subscriptionId, token` | Cancels a user's subscription purchase. The subscription remains valid until its expiration time. |
| `defer` | `EXEC` | `packageName, subscriptionId, token` | Defers a user's subscription purchase until a specified future expiration time. |
| `refund` | `EXEC` | `packageName, subscriptionId, token` | Refunds a user's subscription purchase, but the subscription remains valid until its expiration time and it will continue to recur. |
| `revoke` | `EXEC` | `packageName, subscriptionId, token` | Refunds and immediately revokes a user's subscription purchase. Access to the subscription will be terminated immediately and it will stop recurring. |
