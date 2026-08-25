==================
Mail Show Follower
==================

This module extends the functionality of mailing to show the document
followers in head of the mails. In the cc, only appear when:

1. The followers only count if are contacts or external users (Inner
   Followers will be discriminated)
2. The number of followers are more than 1.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module, you need to:

1. Go General settings/Mail/Show Followers on mails/Show Internal Users
   CC and set if want to show or not internal users in cc details.
2. Go Settings/Users & Company select any user in 'Preferences' check or
   not the 'Show in CC' field if this user need to appear in the cc
   note.
3. Go General settings/Mail/Show Followers on mails/Text 'Sent to' and
   set the initial part of the message.
4. Go General settings/Mail/Show Followers on mails/Partner format and
   choose desired fields to show on CC recipients.
5. Go General settings/Mail/Show Followers on mails/Text 'Replies' and
   choose desired warn message
6. Go General settings/Mail/Show Followers in 'Models to exclude' enter
   the models you want to exclude from the CC note.

Usage
=====

To use this module, you need to:

1. Send an email from any document of odoo.

Credits
=======

Authors
-------

* Sygel
* Moduon

Contributors
------------

- Valentin Vinagre <valentin.vinagre@sygel.es>
- Lorenzo Battistini
- Eduardo de Miguel <edu@moduon.team>
- Vincent Van Rossem <vincent.vanrossem@camptocamp.com>

This module is a local Odoo 19 port of `mail_show_follower
<https://github.com/OCA/mail/tree/18.0/mail_show_follower>`_ from the OCA
``mail`` repository (18.0 branch), ported because no 19.0 version existed
upstream at the time of porting.
