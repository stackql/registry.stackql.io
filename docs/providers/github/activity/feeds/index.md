---
title: feeds
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
<tr><td><b>Name</b></td><td><code>github.activity.feeds</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.feeds</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `user_url` | `string` |  |
| `current_user_organization_url` | `string` |  |
| `current_user_organization_urls` | `array` |  |
| `current_user_public_url` | `string` |  |
| `current_user_url` | `string` |  |
| `_links` | `object` |  |
| `current_user_actor_url` | `string` |  |
| `security_advisories_url` | `string` |  |
| `timeline_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_feeds` | `` | GitHub provides several timeline resources in [Atom](http://en.wikipedia.org/wiki/Atom_(standard)) format. The Feeds API lists all the feeds available to the authenticated user:<br /><br />*   **Timeline**: The GitHub global public timeline<br />*   **User**: The public timeline for any user, using [URI template](https://docs.github.com/rest/overview/resources-in-the-rest-api#hypermedia)<br />*   **Current user public**: The public timeline for the authenticated user<br />*   **Current user**: The private timeline for the authenticated user<br />*   **Current user actor**: The private timeline for activity created by the authenticated user<br />*   **Current user organizations**: The private timeline for the organizations the authenticated user is a member of.<br />*   **Security advisories**: A collection of public announcements that provide information about security-related vulnerabilities in software on GitHub.<br /><br />**Note**: Private feeds are only returned when [authenticating via Basic Auth](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication) since current feed URIs use the older, non revocable auth tokens. | SELECT |
