from .agent_based_api.v1 import *

def discover_bvbrc_solr(section):
    for port, _status, _elap in section:
        yield Service(item=port)

def check_bvbrc_solr(item, section):
    for port, status, elap in section:
        if port == item:
            f_elap = float(elap)
            if status == "OK":
                s = State.OK
            else:
                s = State.CRIT

            yield Result(state = s, summary = "elap {f_elap}")
            return

register.check_plugin(
    name = "bvbrc_solr",
    service_name = "BV-BRC Solr Check",
    discovery_function = discover_bvbrc_solr,
    check_function = check_bvbrc_solr,
    )
