---
title: people
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
<tr><td><b>Name</b></td><td><code>people</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.people.people</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ageRanges` | `array` | Output only. The person's age ranges. |
| `calendarUrls` | `array` | The person's calendar URLs. |
| `nicknames` | `array` | The person's nicknames. |
| `resourceName` | `string` | The resource name for the person, assigned by the server. An ASCII string with a max length of 27 characters, in the form of `people/{person_id}`. |
| `events` | `array` | The person's events. |
| `relationshipInterests` | `array` | Output only. **DEPRECATED**: No data will be returned The person's relationship interests. |
| `urls` | `array` | The person's associated URLs. |
| `userDefined` | `array` | The person's user defined data. |
| `organizations` | `array` | The person's past or current organizations. |
| `names` | `array` | The person's names. This field is a singleton for contact sources. |
| `birthdays` | `array` | The person's birthdays. This field is a singleton for contact sources. |
| `relationshipStatuses` | `array` | Output only. **DEPRECATED**: No data will be returned The person's relationship statuses. |
| `genders` | `array` | The person's genders. This field is a singleton for contact sources. |
| `coverPhotos` | `array` | Output only. The person's cover photos. |
| `clientData` | `array` | The person's client data. |
| `relations` | `array` | The person's relations. |
| `fileAses` | `array` | The person's file-ases. |
| `ageRange` | `string` | Output only. **DEPRECATED** (Please use `person.ageRanges` instead) The person's age range. |
| `taglines` | `array` | Output only. **DEPRECATED**: No data will be returned The person's taglines. |
| `residences` | `array` | **DEPRECATED**: (Please use `person.locations` instead) The person's residences. |
| `locations` | `array` | The person's locations. |
| `skills` | `array` | The person's skills. |
| `memberships` | `array` | The person's group memberships. |
| `photos` | `array` | Output only. The person's photos. |
| `imClients` | `array` | The person's instant messaging clients. |
| `etag` | `string` | The [HTTP entity tag](https://en.wikipedia.org/wiki/HTTP_ETag) of the resource. Used for web cache validation. |
| `emailAddresses` | `array` | The person's email addresses. For `people.connections.list` and `otherContacts.list` the number of email addresses is limited to 100. If a Person has more email addresses the entire set can be obtained by calling GetPeople. |
| `phoneNumbers` | `array` | The person's phone numbers. For `people.connections.list` and `otherContacts.list` the number of phone numbers is limited to 100. If a Person has more phone numbers the entire set can be obtained by calling GetPeople. |
| `miscKeywords` | `array` | The person's miscellaneous keywords. |
| `addresses` | `array` | The person's street addresses. |
| `locales` | `array` | The person's locale preferences. |
| `metadata` | `object` | The metadata about a person. |
| `braggingRights` | `array` | **DEPRECATED**: No data will be returned The person's bragging rights. |
| `biographies` | `array` | The person's biographies. This field is a singleton for contact sources. |
| `sipAddresses` | `array` | The person's SIP addresses. |
| `externalIds` | `array` | The person's external IDs. |
| `interests` | `array` | The person's interests. |
| `occupations` | `array` | The person's occupations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `peopleId` | Provides information about a person by specifying a resource name. Use `people/me` to indicate the authenticated user. The request returns a 400 error if 'personFields' is not specified. |
| `batchCreateContacts` | `EXEC` |  | Create a batch of new contacts and return the PersonResponses for the newly created contacts. Limited to 10 parallel requests per user. |
| `batchDeleteContacts` | `EXEC` |  | Delete a batch of contacts. Any non-contact data will not be deleted. Limited to 10 parallel requests per user. |
| `batchUpdateContacts` | `EXEC` |  | Update a batch of contacts and return a map of resource names to PersonResponses for the updated contacts. Limited to 10 parallel requests per user. |
| `createContact` | `EXEC` |  | Create a new contact and return the person resource for that contact. The request returns a 400 error if more than one field is specified on a field that is a singleton for contact sources: * biographies * birthdays * genders * names |
| `deleteContact` | `EXEC` | `peopleId` | Delete a contact person. Any non-contact data will not be deleted. |
| `deleteContactPhoto` | `EXEC` | `peopleId` | Delete a contact's photo. |
| `getBatchGet` | `EXEC` |  | Provides information about a list of specific people by specifying a list of requested resource names. Use `people/me` to indicate the authenticated user. The request returns a 400 error if 'personFields' is not specified. |
| `listDirectoryPeople` | `EXEC` |  | Provides a list of domain profiles and domain contacts in the authenticated user's domain directory. When the `sync_token` is specified, resources deleted since the last sync will be returned as a person with `PersonMetadata.deleted` set to true. When the `page_token` or `sync_token` is specified, all other request parameters must match the first call. Writes may have a propagation delay of several minutes for sync requests. Incremental syncs are not intended for read-after-write use cases. See example usage at [List the directory people that have changed](/people/v1/directory#list_the_directory_people_that_have_changed). |
| `searchContacts` | `EXEC` |  | Provides a list of contacts in the authenticated user's grouped contacts that matches the search query. The query matches on a contact's `names`, `nickNames`, `emailAddresses`, `phoneNumbers`, and `organizations` fields that are from the CONTACT source. **IMPORTANT**: Before searching, clients should send a warmup request with an empty query to update the cache. See https://developers.google.com/people/v1/contacts#search_the_users_contacts |
| `searchDirectoryPeople` | `EXEC` |  | Provides a list of domain profiles and domain contacts in the authenticated user's domain directory that match the search query. |
| `updateContact` | `EXEC` | `peopleId` | Update contact data for an existing contact person. Any non-contact data will not be modified. Any non-contact data in the person to update will be ignored. All fields specified in the `update_mask` will be replaced. The server returns a 400 error if `person.metadata.sources` is not specified for the contact to be updated or if there is no contact source. The server returns a 400 error with reason `"failedPrecondition"` if `person.metadata.sources.etag` is different than the contact's etag, which indicates the contact has changed since its data was read. Clients should get the latest person and merge their updates into the latest person. The server returns a 400 error if `memberships` are being updated and there are no contact group memberships specified on the person. The server returns a 400 error if more than one field is specified on a field that is a singleton for contact sources: * biographies * birthdays * genders * names |
| `updateContactPhoto` | `EXEC` | `peopleId` | Update a contact's photo. |
