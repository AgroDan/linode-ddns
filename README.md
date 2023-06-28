# linode-ddns

I wrote this script to code up a quick little Dynamic DNS script for Linode. Since I use Linode for DNS, I wrote something to poll it occasionally and update with my IP address so I can have a dynamic DNS service without using a freebie one. You're free to use this for yourself if this helps.

## How to Use
Create your own `config.py` script by copying it from `config-sample.py`

```sh
cp config-sample.py config.py
```

Then add documentation appropriately.

```
TOKEN = Your Linode API token.
DOMAIN_ID = The Domain ID of the domain you are editing. You can find this from their web portal. It shows in the URL of the link.
RECORD_ID = This is the record that you want to update. You can find this by using the get_record_ids() function.
```

