from .agent_based_api.v1 import *
import pprint

def discover_bvbrc_solr(section):
    for portnum, _status, _elap in section:
        port=f"port_{portnum}"
        yield Service(item=portnum)

def check_bvbrc_solr(item, section):
    for portnum, status, elap in section:
        port = f"port_{portnum}"
        if portnum == item:
            f_elap = float(elap)
            yield Metric(name="response_time", value=f_elap, boundaries=(0,10))
            if status == "OK":
                s = State.OK
            else:
                s = State.CRIT

            yield Result(state = s, summary = f"elap {f_elap}")
            return

register.check_plugin(
    name = "bvbrc_solr",
    service_name = "BVBRC Solr port %s",
    discovery_function = discover_bvbrc_solr,
    check_function = check_bvbrc_solr,
    )
