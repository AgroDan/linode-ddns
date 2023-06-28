#!/bin/env python

# Above shebang for the Synology NAS, modify for whatever
import requests
import config
import json

record_ids_url = f"https://api.linode.com/v4/domains/{config.DOMAIN_ID}/records"
record_url = f"https://api.linode.com/v4/domains/{config.DOMAIN_ID}/records/{config.RECORD_ID}"

def make_get_request(url: str) -> str:
    headers = {"Authorization": f"Bearer {config.TOKEN}"}
    r = requests.get(url, headers=headers)
    return r.text


def make_put_request(url: str, j: dict) -> str:
    """
    This will make the PUT request to the api

    Args:
        url (str): Whatever api endpoint we need to connect to
        j (dict): Whatever parameters we want to send

    Returns:
        str: the response
    """
    headers = {"Authorization": f"Bearer {config.TOKEN}"}
    r = requests.put(url, headers=headers, json=j)
    return r.text

def get_record_ids(url: str) -> str:
    j = json.loads(make_get_request(url))
    row = ""
    for rec in j["data"]:
        row += f'{rec["id"]} - {rec["name"]} - {rec["target"]}\n'
    
    return row

def get_current_target(url: str) -> str:
    """
    Gets current IP that the provided record is resolving to

    Args:
        url (str): this should be the `get_record_url` variable

    Returns:
        str: ip address of resolved IP
    """
    j = json.loads(make_get_request(url))
    return j["target"]

def get_my_ip() -> str:
    """
    This simply gets your current public IP address from ifconfig.me

    Returns:
        str: _description_
    """
    return requests.get("https://ifconfig.me").text

def update_ip(url: str) -> dict:
    """
    This will update the specific record

    Args:
        url (str): this is the records_id var

    Returns:
        dict: returns a json object
    """
    # the [remote_addr] will force the api to interpret the receiving request
    # ip as the target ip, perfect for exactly this.
    j = {
        "target": "[remote_addr]"
    }
    p = make_put_request(record_url, j)
    return json.loads(p)
    

if __name__ == "__main__":
    curr_ip = get_my_ip()
    
    try:
        # Get the current record
        rec_ip = get_current_target(record_url)
        
        if curr_ip == rec_ip:
            print("nochg")
        else:
            update_ip(record_url)
            print("good")
    except ConnectionError:
        print("badconn")